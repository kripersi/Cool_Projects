import tkinter as tk
from tkinter import messagebox
import random


def counter():
    '''счетчик кликов'''
    # цвета для кнопки
    colors = ['red', 'blue', '#82c1ed', '#1e8a15', '#c6f7f4',
              '#f7c6ef', '#ff00d5', '#fbff00', '#a8ab16', '#1ec96e']
    num = int(label.cget('text').replace('колво ', ''))
    # закрытие программы после 9 кликов по кнопке
    if num > 9:
        messagebox.showinfo(' ', 'слишком много кликов! *_*')
        quit()
    # изменение расположения кнопки и числа в счетчике
    label.config(text='колво ' + str(int(label.cget('text').replace('колво ', '')) + 1))
    btn.place(x=random.randint(20, 440), y=random.randint(30, 360))
    btn['bg'] = random.choice(colors)

# создание окна
win = tk.Tk()
win.geometry('500x400+300+270')
win.title("кликер с счетчиком")
win.config(background='#82c1ed')
win.resizable(False, False)

# надпись со счетчиком
label = tk.Label(win, text='колво 1', bg='#82c1ed', font=('Arial', 20))
label.pack()

# убегающая кнопка
btn = tk.Button(win, text='click!', bg='#5292bf', activebackground='#234d6b', font=('Arial', 12),
                command=lambda: counter())
btn.pack()

win.mainloop()
