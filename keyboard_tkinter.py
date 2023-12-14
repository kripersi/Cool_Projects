'''hello! programm: keyboard,
 developer: artem(kripersi) age: 14,
 date: 30.07.2023,
 libraries: tkinter
 Python V3.9
'''

import tkinter as tk


def save_doc():
    # записывание в файл
    input_entry1 = input_entry.get()
    with open('texttkinter.txt', 'a', encoding='utf-8') as file:
        file.write(input_entry1+'\n')
        print('save ok')


def caps():
    # увеличение либо уменьшение последней буквы
    input_entry1 = input_entry.get()
    if len(input_entry1)>=1:
        if input_entry1[-1].isupper():
            input_entry.delete(0,'end')
            input_entry.insert(0, input_entry1[:-1]+input_entry1[-1].lower())
        elif input_entry1[-1].islower():
            input_entry.delete(0, 'end')
            input_entry.insert(0, input_entry1[:-1] + input_entry1[-1].upper())


def delete_input():
    # удаление всех элементов
    input_entry.delete(0, 'end')


def del1():
    # удаление последнего элемента
    value = input_entry.get()
    input_entry.delete(0, 'end')
    input_entry.insert(0, value[:-1])


def make_button_del(simb_delete):
    # создание кнопки удаления
    return tk.Button(win, text=simb_delete, bd=1, bg='#525252',
                     width=5, height=3,
                     anchor='nw',
                     activebackground='grey',
                     fg='white',
                     font=('Courier 20', 10, 'bold'),
                     command=lambda: delete_input())


def add_entry(simb):
    # добавление символа в строку
    inputt = input_entry.get()
    input_entry.delete(0,'end')
    input_entry.insert(0, inputt+simb)


def make_button(letter):
    # создания кнопки с цифрами и буквами
    return tk.Button(win, text=letter,bd=1, bg='#525252',
                     width=5, height=3,
                     anchor='nw',
                     activebackground='grey',
                     fg='white',
                     font=('Courier 20', 10, 'bold'),
                     command=lambda: add_entry(letter))


# Создаем графическое окно
win = tk.Tk()
win.geometry('545x407+300+270')
win.title("клавиатура")
win.config(background='black')
win.resizable(False, False)

# Создаем поле для ввода ответа
input_entry = tk.Entry(win, font=("Arial", 20) )
input_entry.grid(row=0, column=0, columnspan=9, sticky='wens')


# создание кнопок
make_button('1').grid(row=2, column=0, stick='wens', padx=3, pady=3)
make_button('2').grid(row=2, column=1, stick='wens', padx=3, pady=3)
make_button('3').grid(row=2, column=2, stick='wens', padx=3, pady=3)
make_button('4').grid(row=2, column=3, stick='wens', padx=3, pady=3)
make_button('5').grid(row=2, column=4, stick='wens', padx=3, pady=3)
make_button('6').grid(row=2, column=5, stick='wens', padx=3, pady=3)
make_button('7').grid(row=2, column=6, stick='wens', padx=3, pady=3)
make_button('8').grid(row=2, column=7, stick='wens', padx=3, pady=3)
make_button('9').grid(row=2, column=8, stick='wens', padx=3, pady=3)
make_button('0').grid(row=2, column=9, stick='wens', padx=3, pady=3)
make_button('q').grid(row=3, column=0, stick='wens', padx=3, pady=3)
make_button('w').grid(row=3, column=1, stick='wens', padx=3, pady=3)
make_button('e').grid(row=3, column=2, stick='wens', padx=3, pady=3)
make_button('r').grid(row=3, column=3, stick='wens', padx=3, pady=3)
make_button('t').grid(row=3, column=4, stick='wens', padx=3, pady=3)
make_button('y').grid(row=3, column=5, stick='wens', padx=3, pady=3)
make_button('u').grid(row=3, column=6, stick='wens', padx=3, pady=3)
make_button('i').grid(row=3, column=7, stick='wens', padx=3, pady=3)
make_button('o').grid(row=3, column=8, stick='wens', padx=3, pady=3)
make_button('p').grid(row=3, column=9, stick='wens', padx=3, pady=3)
make_button('a').grid(row=4, column=0, stick='wens', padx=3, pady=3)
make_button('s').grid(row=4, column=1, stick='wens', padx=3, pady=3)
make_button('d').grid(row=4, column=2, stick='wens', padx=3, pady=3)
make_button('f').grid(row=4, column=3, stick='wens', padx=3, pady=3)
make_button('g').grid(row=4, column=4, stick='wens', padx=3, pady=3)
make_button('h').grid(row=4, column=5, stick='wens', padx=3, pady=3)
make_button('j').grid(row=4, column=6, stick='wens', padx=3, pady=3)
make_button('k').grid(row=4, column=7, stick='wens', padx=3, pady=3)
make_button('l').grid(row=4, column=8, stick='wens', padx=3, pady=3)
make_button(';').grid(row=4, column=9, stick='wens', padx=3, pady=3)
make_button('z').grid(row=5, column=0, stick='wens', padx=3, pady=3)
make_button('x').grid(row=5, column=1, stick='wens', padx=3, pady=3)
make_button('c').grid(row=5, column=2, stick='wens', padx=3, pady=3)
make_button('v').grid(row=5, column=3, stick='wens', padx=3, pady=3)
make_button('b').grid(row=5, column=4, stick='wens', padx=3, pady=3)
make_button('n').grid(row=5, column=5, stick='wens', padx=3, pady=3)
make_button('m').grid(row=5, column=6, stick='wens', padx=3, pady=3)
make_button(',').grid(row=5, column=7, stick='wens', padx=3, pady=3)
make_button('.').grid(row=5, column=8, stick='wens', padx=3, pady=3)
make_button('!').grid(row=5, column=9, stick='wens', padx=3, pady=3)
make_button(' ').grid(row=6, column=1, columnspan=6, stick='wens', padx=3, pady=3)
make_button('?').grid(row=6, column=9, stick='wens', padx=3, pady=3)

# кнопка удаления всех элементов
make_button_del('←').grid(row=6, column=8, stick='wens', padx=3, pady=3)

# создание кнопки caps которая увеличивает или уменьшает последнюю букву
btn_caps = tk.Button(win, text='caps', bd=1, bg='#525252', width=5, height=3, anchor='nw',
                     activebackground='grey',
                     fg='white',
                     font=('Courier 20', 10, 'bold'),
                     command=lambda: caps())
btn_caps.grid(row=6, column=0, stick='wens', padx=3, pady=3)

# создание кнопки которая удаляет последний символ
btn_del = tk.Button(win, text='←←', bd=1, bg='#525252', width=5, height=3, anchor='nw',
                     activebackground='grey',
                     fg='white',
                     font=('Courier 20', 10, 'bold'),
                     command=lambda: del1())
btn_del.grid(row=6, column=7, stick='wens', padx=3, pady=3)

# создание кнопки которая сохраняет текст в документ
btn_save = tk.Button(win, text='save', bd=1, bg='#525252', width=5, height=3, anchor='nw',
                     activebackground='grey',
                     fg='white',
                     font=('Courier 20', 10, 'bold'),
                     command=lambda: save_doc())
btn_save.grid(row=0, column=9, stick='wens', padx=3, pady=3)


win.grid_columnconfigure(1, minsize=5)
win.grid_columnconfigure(2, minsize=5)
win.grid_columnconfigure(3, minsize=5)

win.grid_rowconfigure(1, minsize=20)
win.grid_rowconfigure(2, minsize=20)
win.grid_rowconfigure(3, minsize=20)


win.mainloop()
