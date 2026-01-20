import cv2
import numpy as np

# Passport photo size (India) at 300 DPI
PHOTO_WIDTH = 413
PHOTO_HEIGHT = 531

def load_image(path):
    img = cv2.imread(path)
    if img is None:
        raise ValueError("Image not found")
    return img

def detect_main_face(gray_img, detector):
    faces = detector.detectMultiScale(
        gray_img,
        scaleFactor=1.1,
        minNeighbors=5,
        minSize=(120, 120)
    )
    if len(faces) == 0:
        raise ValueError("No face detected")
    return max(faces, key=lambda f: f[2] * f[3])

def crop_with_margin(image, face_box, margin_ratio=0.35):
    x, y, w, h = face_box
    margin = int(w * margin_ratio)

    x1 = max(0, x - margin)
    y1 = max(0, y - margin)
    x2 = min(image.shape[1], x + w + margin)
    y2 = min(image.shape[0], y + h + margin)

    return image[y1:y2, x1:x2]

def main():
    image_path = "person1.png"   

    image = load_image(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    face_detector = cv2.CascadeClassifier(
        "haarcascade_frontalface_default.xml"
    )

    face = detect_main_face(gray, face_detector)
    cropped = crop_with_margin(image, face)

    passport_photo = cv2.resize(
        cropped,
        (PHOTO_WIDTH, PHOTO_HEIGHT),
        interpolation=cv2.INTER_CUBIC
    )

    output_file = "person1.png"
    cv2.imwrite(output_file, passport_photo)

    print("✅ Passport photo saved as:", output_file)

if __name__ == "__main__":
    main()
