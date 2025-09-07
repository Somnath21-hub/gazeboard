import cv2
import mediapipe as mp
import pyautogui
import time
import threading
import tkinter as tk
from tkinter import messagebox
import speech_recognition as sr

# Disable PyAutoGUI failsafe
pyautogui.FAILSAFE = False

# Mediapipe FaceMesh
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(
    max_num_faces=1,
    refine_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Webcam
cam = cv2.VideoCapture(0)
screen_w, screen_h = pyautogui.size()

# Variables
prev_x, prev_y = 0, 0
smooth_factor = 0.2
last_blink_time = 0
blink_interval = 0.5
dragging = False
blink_start_time = None
long_blink_threshold = 0.5
typed_text = ""  # store typed letters

# Keyboard layout
keys = [
    "1234567890",
    "QWERTYUIOP",
    "ASDFGHJKL",
    "ZXCVBNM",
    ".,?!",
    ["SPACE", "BACK"]
]


def get_keyboard_size(frame_w, frame_h):
    max_row_len = max(len(row) if isinstance(row, str) else len(row) for row in keys)
    key_width = frame_w // (max_row_len + 3)
    key_height = frame_h // 12
    keyboard_start_y = frame_h - (len(keys) * (key_height + 5)) - 20
    return key_width, key_height, keyboard_start_y


def get_key_at_position(x, y, key_width, key_height, keyboard_start_y):
    row_y = keyboard_start_y
    for row in keys:
        col_x = 20
        for key in (row if isinstance(row, list) else list(row)):
            w = key_width
            if key == "SPACE":
                w = key_width * 4
            elif key == "BACK":
                w = key_width * 2

            if col_x < x < col_x+w and row_y < y < row_y+key_height:
                return key, (col_x, row_y, w, key_height)
            col_x += w + 5
        row_y += key_height + 5
    return None, None


def draw_keyboard(frame, key_width, key_height, keyboard_start_y, highlight_box=None):
    y = keyboard_start_y
    for row in keys:
        x = 20
        for key in (row if isinstance(row, list) else list(row)):
            w = key_width
            if key == "SPACE":
                w = key_width * 4
            elif key == "BACK":
                w = key_width * 2

            color = (255, 255, 255)
            thickness = 2
            if highlight_box and (x, y, w, key_height) == highlight_box:
                color = (0, 255, 0)
                thickness = 3

            cv2.rectangle(frame, (x, y), (x+w, y+key_height), color, thickness)
            cv2.putText(frame, key, (x+10, y+key_height//2+10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.7, color, 2)
            x += w + 5
        y += key_height + 5


def run_eye_keyboard():
    global prev_x, prev_y, last_blink_time, blink_start_time, dragging, typed_text

    while True:
        success, frame = cam.read()
        if not success:
            break

        frame = cv2.flip(frame, 1)
        frame_h, frame_w, _ = frame.shape
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = face_mesh.process(rgb_frame)

        key_width, key_height, keyboard_start_y = get_keyboard_size(frame_w, frame_h)
        highlight_box = None

        if result.multi_face_landmarks:
            landmarks = result.multi_face_landmarks[0].landmark
            try:
                iris = landmarks[476]
                x = int(iris.x * frame_w)
                y = int(iris.y * frame_h)

                screen_x = int((x / frame_w) * screen_w)
                screen_y = int((y / frame_h) * screen_h)
                screen_x = int(prev_x + (screen_x - prev_x) * smooth_factor)
                screen_y = int(prev_y + (screen_y - prev_y) * smooth_factor)
                prev_x, prev_y = screen_x, screen_y

                pyautogui.moveTo(screen_x, screen_y)
                cv2.circle(frame, (x, y), 5, (0, 0, 255), -1)

                key, box = get_key_at_position(x, y, key_width, key_height, keyboard_start_y)
                if key:
                    highlight_box = box

                left_eye = [landmarks[145], landmarks[159]]
                right_eye = [landmarks[374], landmarks[386]]
                left_ratio = abs(left_eye[0].y - left_eye[1].y)
                right_ratio = abs(right_eye[0].y - right_eye[1].y)

                if left_ratio < 0.025 and right_ratio < 0.025:
                    if blink_start_time is None:
                        blink_start_time = time.time()
                else:
                    if blink_start_time:
                        blink_duration = time.time() - blink_start_time
                        if blink_duration >= long_blink_threshold:
                            dragging = not dragging
                            if dragging:
                                pyautogui.mouseDown()
                            else:
                                pyautogui.mouseUp()
                        else:
                            current_time = time.time()
                            if current_time - last_blink_time < blink_interval:
                                pyautogui.rightClick()
                            else:
                                if key:
                                    if key == "SPACE":
                                        typed_text += " "
                                    elif key == "BACK":
                                        typed_text = typed_text[:-1]
                                    else:
                                        typed_text += key
                                else:
                                    pyautogui.click()
                            last_blink_time = current_time
                        blink_start_time = None

            except IndexError:
                continue

        draw_keyboard(frame, key_width, key_height, keyboard_start_y, highlight_box)

        cv2.putText(frame, "Typed: " + typed_text, (50, 50),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 255), 2)
        cv2.imshow("Eye Keyboard + Mouse", frame)

        if cv2.waitKey(1) == 27:
            break

    cam.release()
    cv2.destroyAllWindows()
    with open("typed_output.txt", "w") as f:
        f.write(typed_text)
    messagebox.showinfo("Finished", "Final typed text saved to typed_output.txt")


# --- Tkinter GUI ---
def start_program():
    threading.Thread(target=run_eye_keyboard, daemon=True).start()


def stop_program():
    cam.release()
    cv2.destroyAllWindows()
    root.quit()


# --- Voice Control ---
def voice_control():
    r = sr.Recognizer()
    mic = sr.Microphone()
    with mic as source:
        r.adjust_for_ambient_noise(source)
        while True:
            try:
                print("Say a command: start / exit")
                audio = r.listen(source)
                command = r.recognize_google(audio).lower()
                print("You said:", command)

                if "start" in command:
                    start_program()
                elif "exit" in command or "stop" in command:
                    stop_program()
                    break
            except sr.UnknownValueError:
                print("Didn't catch that. Say again.")
            except sr.RequestError:
                print("Speech recognition error")
                break


root = tk.Tk()
root.title("Eye Controlled Keyboard & Mouse")

start_btn = tk.Button(root, text="Start Eye Keyboard", command=start_program, width=30, height=2, bg="green", fg="white")
start_btn.pack(pady=20)

stop_btn = tk.Button(root, text="Stop & Exit", command=stop_program, width=30, height=2, bg="red", fg="white")
stop_btn.pack(pady=20)

# Run voice recognition in background
threading.Thread(target=voice_control, daemon=True).start()

root.mainloop()
