'''hello! programm: multiplication,
 developer: artem(kripersi) age: 14,
 date: 28.07.2023,
 libraries: random, tkinter
 Python V3.9
'''

import tkinter as tk
import random


def window():


    inform = inform1.get()

    win.destroy()
    def generate_example(inform):
        # Генерируем два случайных числа от 1 до 10 и операцию сложения или вычитания
        number1 = int(inform)
        number2 = random.randint(3, 9)
        operation = '*'
        # Создаем пример и сохраняем правильный ответ
        if operation == '*':
            example = f"{number1} * {number2}"
            answer = number1 * number2

        # Обновляем метку с примером
        example_label.config(text=example)

        # Сохраняем правильный ответ в глобальной переменной
        global correct_answer
        correct_answer = answer


    def check_answer(inform):
        # Получаем ответ пользователя
        user_answer = input_entry.get()

        pohvala = ['молодец!', 'правильно','так держать!','верно','невероятно!','топ!','ура, верно!','похвально']
        if len(user_answer)>0 and user_answer.isdigit():
            if int(user_answer) == correct_answer:
                result_label.config(text=random.choice(pohvala))
                generate_example(inform)
                input_entry.delete(0, 'end')
                prav.config(text ='верных: ' + str(int(prav.cget('text').replace('верных: ', '')) + 1))
            else:
                result_label.config(text="Неправильно!")
                neprav.config(text='неверных: ' + str(int(neprav.cget('text').replace('неверных: ', '')) + 1))
        else:
            result_label.config(text='вы не ввели ответ')

    def delete():
        input_entry.delete(0,'end')


    # Создаем графическое окно
    window = tk.Tk()
    window.geometry('600x300+700+100')
    window.title(f"Примеры на {inform}")
    window.config(background='#EE82EE')
    window.resizable(False, False)

    canvas = tk.Canvas(window, width=600, height=300, bg='#EE82EE', highlightthickness=0)
    canvas.place(x=0,y=130)
    canvas.create_oval(-10, 10, 90, 90, fill='#BA55D3', width=0)
    canvas.create_oval(-22, 60, 120, 170, fill='#9932CC', width=0)
    canvas.create_oval(60, 5, 120, 60, fill='#9370DB', width=0)
    canvas.create_oval(-10, 120, 70, 190, fill='#9370DB', width=0)
    canvas.create_oval(80, 180, 190, 80, fill='#BA55D3', width=0)

    canvas2 = tk.Canvas(window, width=315, height=300, bg='#EE82EE', highlightthickness=0)
    canvas2.place(x=460, y=0)
    canvas2.create_oval(10, 10, 120, 120, fill='#BA55D3', width=0)
    canvas2.create_oval(12,-20, 115, 80, fill='#9932CC', width=0)
    canvas2.create_oval(90, -20, 195, 90, fill='#9370DB', width=0)
    canvas2.create_oval(90, 90, 15, 160, fill='#9370DB', width=0)
    canvas2.create_oval(100, 100, 140, 140, fill='#9932CC', width=0)

    # Создаем метку с примером
    example_label = tk.Label(window,bg='#EE82EE', font=("Arial", 20))
    example_label.place(x=265,y=105)

    # Создаем поле для ввода ответа
    input_entry = tk.Entry(window, font=("Arial", 20))
    input_entry.place(x=150, y=150)

    # Создаем кнопку для проверки ответа
    check_button = tk.Button(window, text="Проверить",bg='#EE82EE', font=("Arial", 20),activebackground='#DA70D6',
                             command=lambda:check_answer(inform))
    check_button.place(x=220,y=195)

    check_button = tk.Button(window, text="удалить", bg='#BA55D3', font=("Arial", 10), activebackground='#DA70D6',
                             command=lambda: delete())
    check_button.place(x=383, y=208)

    # сколько верных ответов и неверных
    prav = tk.Label(window, text='верных: 0', bg='#FF00FF', font=('Arial', 10, 'bold'))
    prav.place(x=10, y=80)
    neprav = tk.Label(window, text='неверных: 0', bg='#FF00FF', font=('Arial', 10, 'bold'))
    neprav.place(x=10, y=105)

    # Создаем метку для вывода результата
    result_label = tk.Label(window,bg='#EE82EE', font=("Arial", 20))
    result_label.pack(pady=10)

    # Генерируем первый пример
    generate_example(inform)


def windows():
    informm = inform1.get()
    if len(informm) > 0 and informm.isdigit():
        window()
    else:
        lb1.config(text='вы не ввели ответ')


win = tk.Tk()  # создание окна
win.geometry('300x300+700+100')
win.title('таблица умножения')
win.config(background='#EE82EE')
win.resizable(False, False)

canvas = tk.Canvas(win, width=310,height=310, bg='#EE82EE')
canvas.pack()
canvas.create_oval(-10,-10,90,90, fill='#BA55D3', width=0)
canvas.create_oval(60,-5,120,60, fill='#9370DB', width=0)
canvas.create_oval(35,-8,85,50, fill='#4B0082', width=0)
canvas.create_oval(100,-14,190,80, fill='#9932CC', width=0)
canvas.create_oval(180,-13,310,60, fill='#9932CC', width=0)
canvas.create_oval(160,-7,260,90, fill='#4B0082', width=0)
# кружочки для красоты

lb1 = tk.Label(win, text='на какую цифру будем учить таблицу умножения?', bg='#EE82EE', font=('Arial',8, 'bold'))
lb1.place(x=10, y=90)
inform1 = tk.Entry(win)
inform1.place(x=90,y=120)

knopka = tk.Button(win, text='начать',bg='#EE82EE',activebackground='#DA70D6', command=lambda: windows())
knopka.place(x=130,y=150)



win.mainloop()
