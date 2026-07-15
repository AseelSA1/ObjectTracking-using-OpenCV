# Object-tracking-using-openCv
Object Detection with Real-time CSRT Tracking
An interactive computer vision project built using Python and OpenCV. This project consists of :

Interactive Real-time Tracking: Allows users to manually select any object in a live camera feed using a bounding box and tracks it in real-time using the advanced CSRT tracking algorithm.

✨ Features
Interactive Live Tracking: Users can draw a bounding box around any object (e.g., a face, a phone, or a pet) using the mouse, and the system will track it dynamically.

Stable Jupyter Notebook Rendering: Integrated with Matplotlib to display processed static images with correct RGB colors directly within the notebook, avoiding window freezing issues.

🛠️ Prerequisites & Installation
To ensure smooth execution and avoid package conflicts, it is highly recommended to run this project inside a clean virtual environment (like Anaconda).

Install the required libraries using the following command:

'''
Bash

/# Install the necessary libraries while bypassing corrupted cache files

pip install opencv-python matplotlib numpy --no-cache-dir

'''

🚀 How to Run
 Interactive Object Tracking (Live Video/Camera)
To ensure the interactive GUI windows perform smoothly without freezing, the tracking logic is separated into an independent script named tracker.py.

To run the tracking script using your active environment directly from your notebook, execute the following cell:
'''
Python
!python tracker.py
'''
🎮 Interactive Controls:
The live camera feed will open and pause on the first frame to let you select an object.

Click and drag your mouse to draw a bounding box around the object you want to track.

Press Enter or Space on your keyboard to initiate real-time tracking.

To safely close the tracking window and release the camera, press the ESC key.

📁 Project Structure

Plaintext

opencv-ex/

│
├── tracker.py              # Independent script for real-time tracking

└── README.md               # Project documentation (this file)

🧠 Algorithms Used

CSRT Tracker (Discriminative Correlation Filter with Channel and Spatial Reliability): A highly accurate tracking algorithm that excels at handling scale variations, rotations, and sudden movements in live video feeds.
