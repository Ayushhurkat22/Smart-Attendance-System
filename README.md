# Face Recognition-Based Attendance System

Welcome to the Face Recognition-Based Attendance System! This project leverages advanced computer vision and machine learning techniques to automate attendance marking with a touch of modern technology. Whether you're looking to streamline your classroom management or enhance security systems, this solution offers a robust and user-friendly approach.

## Project Overview

This system is designed to:

- **Capture Images**: Gather a set of images for each individual to create a robust dataset.
- **Train a Recognition Model**: Utilize these images to train a facial recognition model that can identify individuals accurately.
- **Mark Attendance**: Detect faces in real-time, recognize them, and record attendance with a timestamp. The system also provides voice feedback to confirm the attendance process.

## Features

- **Dynamic Image Capture**: Capture multiple images with ease and organize them into specific folders.
- **Real-Time Face Recognition**: Identify faces from a live video feed and record attendance.
- **Voice Feedback**: Get verbal confirmation of actions with adjustable speech rate.
- **Automated Attendance Logging**: Maintain a CSV file of attendance records, organized by the current date.

## Usage Instructions

### 1. Capturing Images

To begin, run the `Face_acquisition_and_detection.py` script. This will prompt you to enter a name prefix for the images, which will then be saved in an organized folder structure for each individual.

```python Face_acquisition_and_detection.py```

### 2. Training the Model

Once you have captured a sufficient number of images, use the `create_encodings.py` script to train the face recognition model. This script will process the images and save the trained model for future use.

```python create_encodings.py```

### 3. Recognizing Faces and Marking Attendance

With the model trained, run the `Face_recognition.py` script to start the attendance system. This will open a video feed, recognize faces in real-time, and log attendance into a CSV file.

```python Face_recognition.py```


## Project Structure

- **`create_encodings.py`**: Script for training the face recognition model. This processes captured images and saves the model.
- **`Face_acquisition_and_detection.py`**: Script for capturing images from the webcam and saving them in an organized manner.
- **`Face_recognition.py`**: Main script for real-time face recognition and attendance marking.
- **`requirements.txt`**: Lists the necessary Python packages for the project.

## Additional Information

- **CSV Files**: Attendance records are saved in CSV files named with the current date. Ensure you have appropriate permissions to create and write files in your working directory.
- **Camera Access**: Make sure your camera is connected and accessible to the scripts for image capture and real-time recognition.
