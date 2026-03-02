import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk, ImageFilter, ImageDraw
import numpy as np
import pickle
import os

# ================= LOAD MODEL =================
model = pickle.load(open("random_forest.pkl", "rb"))  # Or use best_model.pkl
scaler = pickle.load(open("scaler.pkl", "rb"))

# ================= FUNCTIONS =================
def predict_weather():
    try:
        # Get inputs
        precipitation = float(entry_precip.get())
        temp_max = float(entry_max.get())
        temp_min = float(entry_min.get())
        wind = float(entry_wind.get())
        month = int(entry_month.get())

        # Derived features
        avg_temp = (temp_max + temp_min) / 2
        temp_range = temp_max - temp_min

        # Feature array (same order as training)
        features = np.array([[precipitation, temp_max, temp_min, wind, avg_temp, temp_range, month]])
        scaled_features = scaler.transform(features)

        # Predict
        prediction = model.predict(scaled_features)
        result_lbl.config(text=f"Predicted Weather: {prediction[0]}", fg="#E6D8A2")

        print("Input Features:", features)
        print("Scaled Features:", scaled_features)
        print("Prediction:", prediction[0])

    except Exception as e:
        messagebox.showerror("Invalid Input", f"Error: {str(e)}")

def clear_fields():
    for e in entries:
        e.delete(0, tk.END)
    result_lbl.config(text="")

# ================= HOVER BUTTON =================
def luxury_button(parent, text, cmd, x):
    btn = tk.Label(
        parent, text=text, bg="#2A2A2A", fg="#C6B27C",
        font=("Segoe UI", 11, "bold"), width=18, height=2,
        cursor="hand2"
    )
    btn.place(x=x, y=0)
    btn.bind("<Enter>", lambda e: btn.config(bg="#343434"))
    btn.bind("<Leave>", lambda e: btn.config(bg="#2A2A2A"))
    btn.bind("<Button-1>", lambda e: cmd())

# ================= WINDOW =================
root = tk.Tk()
root.title("Luxury Weather Predictor")
root.geometry("1150x650")
root.resizable(False, False)

# ================= BACKGROUND =================
bg_path = "OIP.jpg"
if not os.path.exists(bg_path):
    messagebox.showerror("Error", f"Background image '{bg_path}' not found!")
    root.destroy()
else:
    bg_img = Image.open(bg_path).resize((1150,650))
    bg_photo = ImageTk.PhotoImage(bg_img)
    bg_label = tk.Label(root, image=bg_photo)
    bg_label.place(x=0, y=0, relwidth=1, relheight=1)

# ================= FROSTED GLASS CARD =================
card_x, card_y = 125, 55
card_width, card_height = 900, 540

card_bg = bg_img.crop((card_x, card_y, card_x + card_width, card_y + card_height))
card_bg = card_bg.filter(ImageFilter.GaussianBlur(15))

overlay_alpha = 50
overlay = Image.new("RGBA", (card_width, card_height), (40,40,40,overlay_alpha))
card_bg = Image.alpha_composite(card_bg.convert("RGBA"), overlay)

shadow = Image.new("RGBA", (card_width+20, card_height+20), (0,0,0,0))
shadow_draw = ImageDraw.Draw(shadow)
shadow_draw.rectangle((10,10, card_width+10, card_height+10), fill=(0,0,0,80))
shadow = shadow.filter(ImageFilter.GaussianBlur(12))
shadow_photo = ImageTk.PhotoImage(shadow)
shadow_label = tk.Label(root, image=shadow_photo, borderwidth=0, highlightthickness=0)
shadow_label.place(x=card_x-10, y=card_y-10)

card_photo = ImageTk.PhotoImage(card_bg)
card_label = tk.Label(root, image=card_photo, borderwidth=0)
card_label.place(x=card_x, y=card_y)

# ================= CONTENT FRAME =================
overlay_bg_color = "#282828"
content = tk.Frame(card_label, bg=overlay_bg_color)
content.place(relwidth=1, relheight=1)

# ================= WATERMARK =================
tk.Label(content, text="🌦️", font=("Segoe UI Emoji", 150), fg="#3D3D3D", bg=overlay_bg_color).place(relx=0.78, rely=0.28)

# ================= STYLE =================
style = ttk.Style()
style.theme_use("clam")
style.configure("TEntry", padding=10, relief="flat", fieldbackground="#3A3A3A", foreground="#E6E6E6")

# ================= HEADER =================
tk.Label(content, text="SEATTLE WEATHER PREDICTOR", font=("Segoe UI", 22, "bold"), fg="#E6D8A2", bg=overlay_bg_color).pack(pady=(0,6))
tk.Label(content, text="Luxury Climate Analytics Platform", font=("Segoe UI", 11), fg="#B0B0B0", bg=overlay_bg_color).pack(pady=(0,30))

# ================= FORM =================
form = tk.Frame(content, bg=overlay_bg_color)
form.pack()

def field(lbl, widget, r, c):
    tk.Label(form, text=lbl, font=("Segoe UI", 11), fg="#D0D0D0", bg=overlay_bg_color).grid(row=r, column=c, sticky="w", pady=(0,6))
    widget.grid(row=r+1, column=c, padx=22, pady=(0,20))

entry_precip = ttk.Entry(form, width=28)
entry_max = ttk.Entry(form, width=28)
entry_min = ttk.Entry(form, width=28)
entry_wind = ttk.Entry(form, width=28)
entry_month = ttk.Entry(form, width=28)
entries = [entry_precip, entry_max, entry_min, entry_wind, entry_month]

field("Precipitation", entry_precip, 0,0)
field("Max Temperature", entry_max, 0,1)
field("Min Temperature", entry_min, 2,0)
field("Wind", entry_wind, 2,1)
field("Month (1-12)", entry_month, 4,0)

# ================= BUTTONS =================
btn_frame = tk.Frame(content, bg=overlay_bg_color, width=500, height=50)
btn_frame.pack(pady=25)
btn_frame.pack_propagate(False)
luxury_button(btn_frame, "PREDICT", predict_weather, 40)
luxury_button(btn_frame, "CLEAR", clear_fields, 260)

# ================= RESULT =================
result_lbl = tk.Label(content, text="", font=("Segoe UI", 14, "bold"), bg=overlay_bg_color, fg="#E6D8A2")
result_lbl.pack(pady=8)

root.mainloop()