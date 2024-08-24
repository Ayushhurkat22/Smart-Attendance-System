import cv2
import os
import numpy as np
import pickle

def train_recognizer(image_folder="Images", model_file="trainer.yml"):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    recognizer = cv2.face.LBPHFaceRecognizer_create()

    label_ids = {}
    x_train = []
    y_labels = []

    for root, _, files in os.walk(image_folder):
        for file in files:
            if file.endswith(("jpg", "png")):
                path = os.path.join(root, file)
                label = os.path.basename(root).replace(" ", "-").lower()

                if label not in label_ids:
                    label_ids[label] = len(label_ids)

                img = cv2.imread(path)
                gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5)

                for (x, y, w, h) in faces:
                    x_train.append(gray[y:y+h, x:x+w])
                    y_labels.append(label_ids[label])

    recognizer.train(x_train, np.array(y_labels))
    recognizer.save(model_file)

    with open("labels.pickle", "wb") as f:
        pickle.dump(label_ids, f)

    print(f"Training complete. Model saved as {model_file}.")

if __name__ == "__main__":
    train_recognizer()
