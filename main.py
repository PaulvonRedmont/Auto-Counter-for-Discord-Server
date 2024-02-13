import pyautogui
import time
import tkinter
import math
import keyboard

running = False

numbers_counted = 0

iterations = 0

def count():
    global numbers_counted
    numbers_counted += 1
    pyautogui.write(f"{numbers_counted}")
    pyautogui.press('enter')
    time.sleep(1)

def toggle_program():
    global running
    running = not running


def main_loop():
    print("Program is running. Press 'Esc' to pause or resume.")
    while True:
        if running:
            # Put your program logic here
            print("Program is running...")
        else:
            print("Program is paused...")
        time.sleep(1)
        count()

# Register the toggle_program function to be called when 'Esc' key is pressed
keyboard.on_press_key("esc", lambda _: toggle_program())

# Start the main loop
main_loop()
