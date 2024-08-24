import cv2
import numpy as np
from datetime import datetime
import pyttsx3
import pickle
import csv

def speak(message, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(message)
    engine.runAndWait()

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer.yml")

with open("labels.pickle", "rb") as f:
    label_ids = pickle.load(f)
face_names = {v: k for k, v in label_ids.items()}

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

students_present = set()
now = datetime.now()
current_date = now.strftime("%Y-%m-%d")
csv_file_path = f'{current_date}.csv'

try:
    with open(csv_file_path, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        video_capture = cv2.VideoCapture(0)

        while True:
            ret, frame = video_capture.read()
            if not ret:
                break

            gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray_frame, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

            for (x, y, w, h) in faces:
                roi_gray = gray_frame[y:y+h, x:x+w]
                id_, conf = recognizer.predict(roi_gray)
                name = face_names.get(id_, "Unknown")

                if 45 <= conf <= 85 and name != "Unknown" and name not in students_present:
                    students_present.add(name)
                    current_time = now.strftime("%H:%M:%S")
                    writer.writerow([name, current_time])

                    greeting = "Good morning" if now.hour < 12 else "Good afternoon" if now.hour == 12 else "Good evening"
                    speak(f"{greeting}, {name}. Your attendance has been marked.")

                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
                cv2.putText(frame, name, (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (255, 255, 255), 2)

            cv2.imshow("Attendance System", frame)

            if cv2.getWindowProperty("Attendance System", cv2.WND_PROP_VISIBLE) < 1:
                print("Window closed by user. Exiting...")
                break

        video_capture.release()
        cv2.destroyAllWindows()

except IOError as e:
    print(f"An error occurred while accessing the CSV file: {e}")
