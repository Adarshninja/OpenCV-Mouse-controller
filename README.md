# 🖐️ Gesture-Controlled Virtual Mouse

A real-time virtual mouse system that allows users to control their computer using hand gestures through a webcam.

Built using Computer Vision and AI-based hand tracking without any paid APIs.

---

## 🚀 Project Overview

This project uses a webcam to detect hand landmarks and maps finger gestures to mouse actions such as:

- Cursor movement
- Left click
- Scrolling
- Pause mode

The goal was to understand how real-time Computer Vision systems work and how they can be integrated with system controls.

---

## ✨ Features

✅ Real-time hand tracking  
✅ Cursor movement using index finger  
✅ Click using fist gesture  
✅ Scroll using two fingers  
✅ Fully offline system  
✅ No paid APIs  

---

## 🛠️ Tech Stack

- Python  
- OpenCV  
- MediaPipe (Tasks API)  
- PyAutoGUI  

---

## 📸 How It Works

1. Webcam captures video frames.
2. MediaPipe detects hand landmarks.
3. Landmark coordinates are mapped to screen coordinates.
4. Gestures are recognized using logic.
5. PyAutoGUI performs mouse actions.

Pipeline:

Camera → Hand Detection → Gesture Logic → Mouse Control

---

## ⚙️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
