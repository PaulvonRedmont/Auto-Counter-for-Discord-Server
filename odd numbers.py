import pyautogui
import time
import keyboard

running = False
numbers_counted = 0
iterations = 0

def count():
    global numbers_counted
    global iterations
    if numbers_counted % 2 == 1:  # Check if the number is odd
        iterations += 1
        pyautogui.write(f"{numbers_counted}")
        pyautogui.press('enter')
        print(f"Just counted {numbers_counted}")
        time.sleep(1)
    numbers_counted += 1

def toggle_program():
    global running
    running = not running

def main_loop():
    print("Program is running. Press 'Esc' to pause or resume.")
    while True:
        if running:
            print("Program is running...")
            count()
        else:
            print("Program is paused...")
        time.sleep(1)

# Register the toggle_program function to be called when 'Esc' key is pressed
keyboard.on_press_key("esc", lambda _: toggle_program())

# Start the main loop
main_loop()
