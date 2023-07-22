'''hello! programm: calculator,
 developer: artem(kripersi) age: 14,
 date: 22.07.2023,
 libraries: math(sqrt), tkinter,
 Phyton V3.9
'''

import tkinter as tk
from math import sqrt


def add_digit(digit):
    value = calc.get()
    if value[0]=='0' and len(value)==1:
        value = value[1:]
    calc.delete(0, 'end')
    calc.insert(0, value + digit)
# добавление цифр в поле

def add_operation(operation):
    value = calc.get()
    if value[-1] in '+-=*/↑':
        value = value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, value + operation)
# добавление операций в поле

def calculate():
    value = calc.get()
    if value[-1] in '*/+-↑':
        value = value+value[:-1]
    calc.delete(0, tk.END)
    calc.insert(0, eval(value))
# калькулятор

def make_button(digit):
    return tk.Button(win, text=digit,bd=5, bg='#1E90FF',activebackground='#ADD8E6', fg='black', font=('Arial', 10, 'bold'),
                     command=lambda: add_digit(digit))
# функция для создания кнопок с цифрами

def make_operation_button(operation):
    return tk.Button(win, text=operation,bd=5, bg='#0000FF',activebackground='#ADD8E6', fg='black', font=('Arial', 10, 'bold'),
                     command=lambda: add_operation(operation))
# функция для создания кнопок операции

def make_calc_button(operation):
    return tk.Button(win, text=operation,bd=5, bg='#0000FF',activebackground='#ADD8E6', fg='black', font=('Arial', 10, 'bold'),
                     command=lambda: calculate())
# фунция для создания кнопки равно

def delet():
    calc.delete(0, 'end')
    calc.insert(0,0)
# удаление всех символов

def del1():
    value = calc.get()
    if len(value)==1:
        calc.delete(0, 'end')
        calc.insert(0,'0')
    else:
        calc.delete(0, 'end')
        calc.insert(0,value[:-1])

# удаление последнего символа

def stepen():
    value = eval(calc.get()) ** 2
    calc.delete(0, 'end')
    calc.insert(0, value)
# вычисление степени

def root():
    value = sqrt(eval(calc.get()))
    calc.delete(0, 'end')
    calc.insert(0, value)
# вычисление корня

# создание окна
win = tk.Tk()
win.geometry('305x300+700+100')
win.title('калькулятор')
win.config(background='#ADD8E6')

# добавление поля ввода
calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 20))
calc.insert(0, '0')
calc.grid(row=0, column=0, columnspan=4)

# цифры
make_button('1').grid(row=1, column=0, stick='wens', padx=4, pady=5)
make_button('2').grid(row=1, column=1, stick='wens', padx=4, pady=5)
make_button('3').grid(row=1, column=2, stick='wens', padx=4, pady=5)
make_button('4').grid(row=2, column=0, stick='wens', padx=4, pady=5)
make_button('5').grid(row=2, column=1, stick='wens', padx=4, pady=5)
make_button('6').grid(row=2, column=2, stick='wens', padx=4, pady=5)
make_button('7').grid(row=3, column=0, stick='wens', padx=4, pady=5)
make_button('8').grid(row=3, column=1, stick='wens', padx=4, pady=5)
make_button('9').grid(row=3, column=2, stick='wens', padx=4, pady=5)
make_button('0').grid(row=4, column=0, columnspan=2, stick='wens', padx=4, pady=5)

# операции
make_operation_button('+').grid(row=1, column=3, stick='wens', padx=4, pady=5)
make_operation_button('-').grid(row=2, column=3, stick='wens', padx=4, pady=5)
make_operation_button('/').grid(row=3, column=3, stick='wens', padx=4, pady=5)
make_operation_button('*').grid(row=4, column=3, stick='wens', padx=4, pady=5)

# сложные операции
tk.Button(win, text='↑',bd=5, bg='#0000FF', fg='white', font=('Arial', 10, 'bold'), command=lambda: stepen()).grid(row=5, column=2, stick='wens', padx=5, pady=10)
make_calc_button('=').grid(row=4, column=2, stick='wens', padx=4, pady=5)
tk.Button(win, text='C',bd=5, bg='#0000FF', fg='white', font=('Arial', 10, 'bold'), command=lambda: delet()).grid(row=5, column=0, stick='wens', padx=5, pady=10)
tk.Button(win, text='←',bd=5, bg='#0000FF', fg='white', font=('Arial', 10, 'bold'), command=lambda: del1()).grid(row=5, column=1, stick='wens', padx=5, pady=10)
tk.Button(win, text='√',bd=5, bg='#0000FF', fg='white', font=('Arial', 10, 'bold'), command=lambda: root()).grid(row=5, column=3, stick='wens', padx=5, pady=10)


win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=60)
win.grid_columnconfigure(3, minsize=30)
win.grid_rowconfigure(5, minsize=20)

win.mainloop()














