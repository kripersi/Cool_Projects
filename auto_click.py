# pip install pyautogui, pip install keyboard
# site for test: https://ningaro.github.io/browser-clicker/

import pyautogui
import keyboard

image = 'images/red_button.png'  # Insert your photo here

for i in range(1, 4):
    print(f'[ {4 - i} ] seconds left...')
    pyautogui.sleep(1)

while not keyboard.is_pressed('Esc'):  # Click on the ESC to stop the program
    try:
        button = pyautogui.locateCenterOnScreen(image, confidence=0.8)
        pyautogui.click(button.x, button.y)
    except Exception:
        print('Button Not Found')

    pyautogui.sleep(0.1)
