import tkinter as tk
from googletrans import Translator
from tkinter import ttk
import pyttsx3

# языки для перевода
vibor = ('en: English', 'ru: Russian', 'fr: France')


def delete():
    # удаление всех символов
    entry.delete('1.0', tk.END)
    entry.insert('1.0', '')

    entry1.delete('1.0', tk.END)
    entry1.insert('1.0', '')


def voice():
    # озвучка текста
    tts = pyttsx3.init()
    text_to_voice = entry1.get('1.0', tk.END)  # получение текста для озвучки
    tts.say(text_to_voice)
    tts.runAndWait()


def translate():
    # перевод текста
    gotranslate = Translator()
    text = entry.get('1.0', 'end')  # получение текста для перевода
    try:
        erors.config(text='')
        trans = gotranslate.translate(text, dest=str(combo.get()[:2]))
        entry1.delete('1.0', tk.END)
        entry1.insert('1.0', trans.text)
    except:
        erors.config(text='ошибка! Проверьте подключение к интернету \nлибо язык который вы выбрали')


# создание окна
win = tk.Tk()
win.geometry('360x400+900+270')
win.title("переводчик")
win.config(background='grey')
win.resizable(False, False)

# поля ввода и вывода
entry = tk.Text(win, font=("Arial", 20), height=3, width=20)
entry.place(x=30, y=30)

entry1 = tk.Text(win, font=("Arial", 20), height=3, width=20)
entry1.configure(state='normal')
entry1.place(x=30, y=210)

# кнопки для перевода,озвучивания и удаления текста
btn_trans = tk.Button(win, text='перевод\ntranslate', bd=1, bg='#525252', padx=45,
                      width=7, height=3,
                      anchor='center',
                      activebackground='grey',
                      fg='white',
                      font=('Courier 20', 10, 'bold'),
                      command=translate)
btn_trans.place(x=105, y=140)

btn_voice = tk.Button(win, text='озвучить\nvoice', bd=1, bg='#525252', padx=25,
                      width=1, height=3,
                      anchor='center',
                      activebackground='grey',
                      fg='white',
                      font=('Courier 20', 10, 'bold'),
                      command=voice)
btn_voice.place(x=265, y=140)

btn_del = tk.Button(win, text='удалить\ndelete', bd=1, bg='#525252', padx=25,
                    width=1, height=3,
                    anchor='center',
                    activebackground='grey',
                    fg='white',
                    font=('Courier 20', 10, 'bold'),
                    command=delete)
btn_del.place(x=35, y=140)

# пустая надпись для вывода ошибки если она будет
erors = tk.Label(win, text='', bg='grey', fg='red', font='Arial 10')
erors.place(x=40, y=320)

# выбор языка для перевода
tk.Label(win, text='перевод на ', bg='grey', font='Arial 13').place(x=60, y=3)

combo = ttk.Combobox(win, values=vibor)
combo.current(0)  # начальное значение
combo.place(x=160, y=5)

win.mainloop()
