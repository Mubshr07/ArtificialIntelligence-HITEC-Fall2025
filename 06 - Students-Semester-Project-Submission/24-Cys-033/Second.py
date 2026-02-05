from scipy.spatial import distance
from imutils import face_utils
from pygame import mixer
import imutils
import dlib
import cv2
import pygame

# ---------------- INITIALIZE AUDIO ----------------
pygame.init()
mixer.init()
mixer.music.load("alarm_wakeup_remix.mp3")

# ---------------- EYE ASPECT RATIO ----------------
def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

# ---------------- PARAMETERS ----------------
thresh = 0.25
frame_check = 20
flag = 0
alarm_on = False

# ---------------- FACE & LANDMARK MODELS ----------------
detect = dlib.get_frontal_face_detector()
predict = dlib.shape_predictor( "shape_predictor_68_face_landmarks.dat")

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["left_eye"]
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_68_IDXS["right_eye"]

# ---------------- CAMERA ----------------
cap = cv2.VideoCapture(0)

# ---------------- MAIN LOOP ----------------
while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = imutils.resize(frame, width=450)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    subjects = detect(gray, 0)

    for subject in subjects:
        shape = predict(gray, subject)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        leftEAR = eye_aspect_ratio(leftEye)
        rightEAR = eye_aspect_ratio(rightEye)
        ear = (leftEAR + rightEAR) / 2.0

        cv2.drawContours(frame, [cv2.convexHull(leftEye)], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [cv2.convexHull(rightEye)], -1, (0, 255, 0), 1)

        if ear < thresh:
            flag += 1

            if flag >= frame_check:
                cv2.putText(frame, "**************** ALERT ****************",
                            (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (0, 0, 255), 2)

                cv2.putText(frame, "**************** ALERT ****************",
                            (10, 325), cv2.FONT_HERSHEY_SIMPLEX,
                            0.7, (0, 0, 255), 2)

                if not alarm_on:
                    mixer.music.play(-1)
                    alarm_on = True
        else:
            flag = 0
            if alarm_on:
                mixer.music.stop()
                alarm_on = False

    cv2.imshow("Drowsiness Detection", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# ---------------- CLEANUP ----------------
cap.release()
cv2.destroyAllWindows()
mixer.quit()
