# Artificial Intelligence – HITEC University (Fall 2025)

Welcome to the official course repository for **Artificial Intelligence (CS-312)** at **HITEC University, Taxila**, during the **Fall 2025** semester! 🎓

This repository serves as a central hub for lab assignments, code submissions, and collaborative learning. All students enrolled in the course are required to follow the submission guidelines below to ensure smooth evaluation and organization.

---

## 📌 Important: Submission Workflow for Students

To submit your **Lab Codes**, please follow the steps **carefully and in order**. Any deviation may result in delayed or missed grading.

---

### ✅ Step-by-Step Submission Guide

#### 1. **Fork This Repository**
   - Click the **"Fork"** button (top-right corner of this page).
   - This creates a personal copy of the repository under your GitHub account.

#### 2. **Clone Your Fork Locally (Optional but Recommended)** Bash Commands
   ```bash
   git clone https://github.com/Mubshr07/ArtificialIntelligence-HITEC-Fall2025.git
   cd ArtificialIntelligence-HITEC-Fall2025
   ```

#### 3. **Create a New Branch**
   - **Branch name must be your HITEC registration number** (e.g., `24-CyS-123`).
   - Do **not** use spaces, special characters, or your name.
   - Example:
     ```bash
     git checkout -b 24-CyS-123
     ```

#### 4. **Create Your Submission Folder**
   - Inside the directory `04 - Students-Lab-Report-Submissions/`, create a **new folder** named **exactly** with your registration number.
     ```
     04 - Students-Lab-Report-Submissions/
     └── 24-CyS-123/
         ├── Lab1_search_algorithms.py
         ├── Lab2_tic_tac_toe.ipynb
         └── Lab3_Informed_Search_Algorithms.ipynb
     ```
   - **All your lab code files, Jupyter notebooks, and reports** for the semester should go into this folder.

#### 5. **Add, Commit, and Push Your Changes**
   - Stage your files:
     ```bash
     git add "04 - Students-Lab-Report-Submissions/24-CyS-123/*"
     ```
   - Write a **clear and descriptive commit message**:
     ```bash
     git commit -m "Lab 6 submission: Implemented A* search for pathfinding in grid world"
     ```
     > 💡 **Good commit messages** explain **what** was done and **why**. Avoid vague messages like "update" or "done".

   - Push to your fork:
     ```bash
     git push -u origin 24-CyS-123
     ```

#### 6. **Open a Pull Request (PR)**
   - Go to your fork on GitHub.
   - Click **"Contribute" → "Open pull request"**.
   - Ensure the PR is from your branch (e.g., `24-CyS-123`) **to the main branch** of the original repository (`Mubshr07:main`).
   - **Title your PR clearly**:
     ```
     [Lab 6] 24-CyS-123 – A* Search Implementation
     ```
   - In the description, briefly summarize your work and mention any challenges or extra features.
   - Click **"Create pull request"**.

> ⏰ **Deadline Note**: Pull requests submitted after the lab deadline will be marked **late**. Ensure your PR is opened **before** the due date.

---

## 📁 Repository Structure Overview

```
📁 01 - Course-Outline/
📁 02 - Lecture-Notes/
📁 03 - Sample-Code-Demos/
📁 04 - Students-Lab-Report-Submissions/   ← Your submissions go here
  ├── 24-CyS-001/
  ├── 24-CyS-002/
  ├── 24-CyS-003/
  ├── 24-CyS-004/
  ├── 24-CyS-005/
  └── ... (your reg# folder)
📁 05 - Students-OEL-Codes/
  ├── 24-CyS-001/
  ├── 24-CyS-002/
  ├── 24-CyS-003/
  ├── 24-CyS-004/
  ├── 24-CyS-005/
  └── ... (your reg# folder)
📁 05 - Students-Semester-Project-Submission/
  ├── 24-CyS-001/
  ├── 24-CyS-002/
  ├── 24-CyS-003/
  ├── 24-CyS-004/
  ├── 24-CyS-005/
  └── ... (your reg# folder)
📄 README.md
```

- **Do not modify folders outside `04 - Students-Lab-Report-Submissions`.**
- Only add content inside **your own registration-number folder**.

---

## 🛠️ Technical Requirements

- All code must be in **Python** (unless otherwise specified).
- Use **Jupyter Notebooks (.ipynb)** or **.py files** for code.
- Reports can be in **PDF** format (preferred) or well-commented notebooks.
- Include a `requirements.txt` if you use external libraries (e.g., `scikit-learn`, `numpy`).

---

## ❗ Common Mistakes to Avoid

❌ Submitting to the wrong folder  
❌ Using a branch name that is **not** your registration number  
❌ Uploading files directly to the root or other students' folders  
❌ Writing poor commit messages like "done" or "submit"  
❌ Creating a PR to your own fork instead of the original repo

---

## 📜 Academic Integrity

All work must be your **own**. Copying code or reports from classmates or online sources without attribution is **plagiarism** and will result in academic penalties. You may discuss concepts, but **implement and write independently**.

---

> ✨ **Happy Coding & Learning!**  
> — Instructor: Mr. Mubasher Iqbal  
> **Artificial Intelligence | HITEC University – Fall 2025**
---


