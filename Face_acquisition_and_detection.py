import cv2
import os
import pyttsx3

def speak(message, rate=150):
    engine = pyttsx3.init()
    engine.setProperty('rate', rate)
    engine.say(message)
    engine.runAndWait()

def capture_images(base_folder="Images", max_photos=100):
    name_prefix = input("Enter the name prefix for the images: ")
    output_folder = os.path.join(base_folder, name_prefix)
    os.makedirs(output_folder, exist_ok=True)

    speak(f"Hello {name_prefix}, your images are being captured. Please wait.", rate=120)

    cap = cv2.VideoCapture(0)

    try:
        for photo_count in range(1, max_photos + 1):
            ret, frame = cap.read()
            if not ret:
                print("Failed to capture a frame")
                continue

            cv2.imshow("Capturing Images", frame)
            image_path = os.path.join(output_folder, f"{name_prefix}_{photo_count}.jpg")
            cv2.imwrite(image_path, frame)
            print(f"Saved image {photo_count} as {image_path}")

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

    except cv2.error as e:
        print(f"OpenCV error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        speak(f"Image capture completed. {photo_count} images saved.", rate=120)

if __name__ == "__main__":
    capture_images()
