import cv2
import mediapipe as mp
import pyautogui
import numpy as np
import screen_brightness_control as sbc


# Initialize Mediapipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Initialize webcam
cap = cv2.VideoCapture(0)

# Screen dimensions
screen_width, screen_height = pyautogui.size()
frame_width, frame_height = 640, 480

# State variables
scrolling = False
dragging = False

def calculate_distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = cv2.flip(frame, 1)
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = hands.process(rgb_frame)

    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark

            # Extract landmarks for thumb and index fingers
            thumb_tip = landmarks[4]
            index_tip = landmarks[8]
            middle_tip = landmarks[12]

            thumb_x, thumb_y = int(thumb_tip.x * frame_width), int(thumb_tip.y * frame_height)
            index_x, index_y = int(index_tip.x * frame_width), int(index_tip.y * frame_height)
            middle_x, middle_y = int(middle_tip.x * frame_width), int(middle_tip.y * frame_height)

            # Map cursor position
            cursor_x = np.interp(index_x, [0, frame_width], [0, screen_width])
            cursor_y = np.interp(index_y, [0, frame_height], [0, screen_height])

            # Move cursor
            pyautogui.moveTo(cursor_x, cursor_y)

            # Calculate distances for gestures
            thumb_index_dist = calculate_distance((thumb_x, thumb_y), (index_x, index_y))
            thumb_middle_dist = calculate_distance((thumb_x, thumb_y), (middle_x, middle_y))

            # Left click gesture (thumb and index finger close)
            if thumb_index_dist < 40:
                pyautogui.click()

            # Right click gesture (thumb and middle finger close)
            if thumb_middle_dist < 40:
                pyautogui.click(button='right')

            # Scrolling (two fingers vertical movement)
            if abs(index_y - middle_y) > 40 and not scrolling:
                pyautogui.scroll(-5 if index_y > middle_y else 5)
                scrolling = True
            elif abs(index_y - middle_y) <= 40:
                scrolling = False

            # Drag and drop (index and thumb held close)
            if thumb_index_dist < 40 and not dragging:
                pyautogui.mouseDown()
                dragging = True
            elif thumb_index_dist >= 40 and dragging:
                pyautogui.mouseUp()
                dragging = False

            # Volume control (thumb-index horizontal movement)
            if abs(thumb_x - index_x) > 40:
                pyautogui.press('volumeup' if thumb_x > index_x else 'volumedown')

            #brightness control(index finger vertical moment)
            if abs(index_y - thumb_y) > 40:
                sbc.set_brightness(50 if index_y < thumb_y else 10)

                
            # Open/close folder (middle and index finger far apart or close)
            if abs(index_x - middle_x) > 60:
                pyautogui.hotkey('ctrl', 'o')  # Example: Open folder
            elif abs(index_x - middle_x) < 30:
                pyautogui.hotkey('ctrl', 'w')  # Example: Close folder

    cv2.imshow("Gesture Control Virtual Mouse", frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
