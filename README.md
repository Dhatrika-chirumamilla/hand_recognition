Gesture recognition using virtual mouse
Python-based gesture-controlled virtual mouse that allows you to control your computer cursor and perform actions like clicking, scrolling, dragging, volume control, brightness control, and even opening/closing folders — all using just your hand gestures detected via a webcam.

Features

Move Cursor – Control the mouse pointer using your index finger.

Left Click – Pinch your thumb and index finger.

Right Click – Pinch your thumb and middle finger.

Scrolling – Move your thumb up or down to scroll the page.

Drag and Drop – Hold pinch gesture to drag and release to drop.

Volume Control – Adjust volume using upward/downward gestures.

Brightness Control – Change screen brightness with gestures.

Open Folder – Special gesture to open a predefined folder.

Close Folder / Window – Special gesture to close active window.


Technologies Used:

Python 3.x

OpenCV – For capturing and processing video frames.

Mediapipe – For hand and finger landmark detection.

PyAutoGUI – For simulating mouse and keyboard actions.

Pynput – For additional keyboard controls.

OS module – For folder and file operations.

 Installation:

1. Clone the Repository

git clone https://github.com/yourusername/gesture-control-virtual-mouse.git
cd gesture-control-virtual-mouse


2. Install Dependencies

pip install opencv-python mediapipe pyautogui pynput screen-brightness-control

▶ How to Run

python virtual_mouse.py


Gestures Guide

Gesture	Action:
Index finger move	Move cursor
Thumb + Index pinch	Left click
Thumb + Middle pinch	Right click
Thumb up	Scroll up
Thumb down	Scroll down
Hold pinch	Drag
Release pinch	Drop
Special gesture 1	Open folder
Special gesture 2	Close folder

Future Improvements:
Add more gesture combinations.
Improve accuracy using machine learning models.

Multi-hand support for more actions.

