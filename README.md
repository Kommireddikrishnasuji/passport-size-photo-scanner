# 🛂passport-size-photo-scanner


# 📌About the Project

This project is a **Python-based passport-size photo scanner** built using **OpenCV**.  
It automatically detects the face from an input image, crops it properly, resizes it to passport dimensions, and generates a clean passport-size photo.

## 🔥 Features
- 👤 Face detection using OpenCV
- ✂️ Automatic cropping and centering
- 📏Passport-size resizing (India standard: 413 × 531 pixels)
- 💯Clean output image
- 🤖Fully automated (no user input during execution)

## 🚀Technologies Used
- 👨‍💻Python
- 👀OpenCV
- 🔢NumPy

## 📂 Project Structure

├── passport_photo.py
├── haarcascade_frontalface_default.xml
└── person1.png


## ▶️ How to Run
1. 📦Install dependencies: pip install opencv-python numpy.
2. 🖼️Place your input image as `person1.png` in the project folder.
3. ▶️Run the script:python passport_photo.py


## 📤Output
- The processed passport-size photo is saved as `person1.png`.

## 🎯Use Case
This project can be used in **online application websites, profile photo preparation tools, and learning image processing with OpenCV**.
