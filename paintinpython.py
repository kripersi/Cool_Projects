import tkinter as tk
from tkinter import ttk

infaa = [205, 1]  # начальная позиция


def delete_all():
    '''удаление всего'''
    global tochka
    tochka_x = infaa[0]
    tochka_y = int(infaa[1])
    try:
        tk.Label(win, text='', bg='white', padx=330,
                 pady=300,
                 font='Arial 5').place(x=204, y=0)
        tochka.destroy()
        tochka = tk.Label(win, text='0', bg='black', fg='white', padx=int(widht_line.get()),
                          pady=int(widht_line.get()),
                          font='Arial 5')
        tochka.place(x=int(tochka_x), y=tochka_y)
    except:
        errorlabel.config(text='ERROR: проверьте выбранное выше', bg='red', fg='white')


def pouring():
    '''заливка всего поля'''
    global tochka
    tochka_x = infaa[0]
    tochka_y = int(infaa[1])
    try:
        tk.Label(win, text='', bg=combo_color.get(), padx=330,
                 pady=300,
                 font='Arial 5').place(x=204, y=0)
        tochka.destroy()
        tochka = tk.Label(win, text='0', bg='black', fg='white', padx=int(widht_line.get()),
                          pady=int(widht_line.get()),
                          font='Arial 5')
        tochka.place(x=int(tochka_x), y=tochka_y)
    except:
        errorlabel.config(text='ERROR: проверьте выбранное выше', bg='red', fg='white')


def up():
    global tochka
    '''перемещение пера вверх'''
    tochka_x = infaa[0]
    tochka_y = int(infaa[1]) - 10
    try:
        errorlabel.config(text='', bg='grey', fg='white')
        if tochka_y > 0 and combo.get() == 'up' and widht_line.get().isdigit():
            # если точка находиться в пределах листа и оно поднято то переместить кисть
            tochka.destroy()
            tochka = tk.Label(win, text='0', bg='black', fg='white', padx=int(widht_line.get()),
                              pady=int(widht_line.get()),
                              font='Arial 5')
            tochka.place(x=int(tochka_x), y=tochka_y)
            # сохранение новой позиции
            infaa[0] = tochka_x
            infaa[1] = tochka_y
        elif tochka_y > 0 and combo.get() == 'down' and widht_line.get().isdigit():
            # если точка находиться в пределах листа и оно опущено то переместить кисть и нарисовать
            tk.Label(win, text=' ', bg=combo_color.get(), padx=int(widht_line.get()), pady=int(widht_line.get()),
                     font='Arial 5').place(x=int(tochka_x), y=int(tochka_y))
            tochka.place(x=int(tochka_x), y=tochka_y)
            tochka.destroy()

            tochka = tk.Label(win, text='0', bg='black', fg='white', padx=int(widht_line.get()),
                              pady=int(widht_line.get()),
                              font='Arial 5')
            tochka.place(x=int(tochka_x), y=tochka_y)

            # сохранение новой позиции
            infaa[0] = tochka_x
            infaa[1] = tochka_y
    except:
        errorlabel.config(text='ERROR: проверьте выбранное выше', bg='red', fg='white')


def down():
    global tochka
    '''перемещение пера вниз'''
    tochka_x = infaa[0]
    tochka_y = int(infaa[1]) + 10
    try:
        errorlabel.config(text='', bg='grey', fg='white')
        if tochka_y < 490 and combo.get() == 'up' and widht_line.get().isdigit():
            # если точка находиться в пределах листа и оно поднято то переместить кисть
            tochka.destroy()
            tochka = tk.Label(win, text='0', bg='black', fg='white', padx=int(widht_line.get()),
                              pady=int(widht_line.get()),
                              font='Arial 5')
            tochka.place(x=int(tochka_x), y=tochka_y)
            # сохранение новой позиции
            infaa[0] = tochka_x
            infaa[1] = tochka_y
        elif tochka_y < 490 and combo.get() == 'down' and widht_line.get().isdigit():
            # если точка находиться в пределах листа и оно опущено то переместить кисть и нарисовать
            tk.Label(win, text=' ', bg=combo_color.get(), padx=int(widht_line.get()), pady=int(widht_line.get()),
                     font='Arial 5').place(x=int(tochka_x), y=int(tochka_y))
            tochka.place(x=int(tochka_x), y=tochka_y)
            tochka.destroy()

            tochka = tk.Label(win, text='0', bg='black', fg='white', padx=int(widht_line.get()),
                              pady=int(widht_line.get()),
                              font='Arial 5')
            tochka.place(x=int(tochka_x), y=tochka_y)

            # сохранение новой позиции
            infaa[0] = tochka_x
            infaa[1] = tochka_y
    except:
        errorlabel.config(text='ERROR: проверьте выбранное выше', bg='red', fg='white')


def right():
    global tochka
    '''перемещение пера вправо'''
    tochka_x = int(infaa[0]) + 10
    tochka_y = int(infaa[1])
    try:
        errorlabel.config(text='', bg='grey', fg='white')
        if tochka_x < 850 and combo.get() == 'up' and widht_line.get().isdigit():
            # если точка находиться в пределах листа и оно поднято то переместить кисть
            tochka.destroy()
            tochka = tk.Label(win, text='0', bg='black', fg='white', padx=int(widht_line.get()),
                              pady=int(widht_line.get()),
                              font='Arial 5')
            tochka.place(x=int(tochka_x), y=tochka_y)
            # сохранение новой позиции
            infaa[0] = tochka_x
            infaa[1] = tochka_y
        elif tochka_x < 850 and combo.get() == 'down' and widht_line.get().isdigit():
            # если точка находиться в пределах листа и оно опущено то переместить кисть и нарисовать
            tk.Label(win, text=' ', bg=combo_color.get(), padx=int(widht_line.get()), pady=int(widht_line.get()),
                     font='Arial 5').place(x=int(tochka_x), y=int(tochka_y))
            tochka.place(x=int(tochka_x), y=tochka_y)
            tochka.destroy()

            tochka = tk.Label(win, text='0', bg='black', fg='white', padx=int(widht_line.get()),
                              pady=int(widht_line.get()),
                              font='Arial 5')
            tochka.place(x=int(tochka_x), y=tochka_y)
            # сохранение новой позиции
            infaa[0] = tochka_x
            infaa[1] = tochka_y
    except:
        errorlabel.config(text='ERROR: проверьте выбранное выше', bg='red', fg='white')


def left():
    global tochka
    '''перемещение пера влево'''
    tochka_x = int(infaa[0]) - 10
    tochka_y = int(infaa[1])
    try:
        errorlabel.config(text='', bg='grey', fg='white')
        if tochka_x > 200 and combo.get() == 'up' and widht_line.get().isdigit():
            # если точка находиться в пределах листа и оно поднято то переместить кисть
            tochka.destroy()
            tochka = tk.Label(win, text='0', bg='black', fg='white', padx=int(widht_line.get()),
                              pady=int(widht_line.get()),
                              font='Arial 5')
            tochka.place(x=int(tochka_x), y=tochka_y)
            # сохранение новой позиции
            infaa[0] = tochka_x
            infaa[1] = tochka_y
        elif tochka_x > 200 and combo.get() == 'down' and widht_line.get().isdigit():
            # если точка находиться в пределах листа и оно опущено то переместить кисть и нарисовать
            tk.Label(win, text=' ', bg=combo_color.get(), padx=int(widht_line.get()), pady=int(widht_line.get()),
                     font='Arial 5').place(x=int(tochka_x), y=int(tochka_y))
            tochka.place(x=int(tochka_x), y=tochka_y)
            tochka.destroy()

            tochka = tk.Label(win, text='0', bg='black', fg='white', padx=int(widht_line.get()),
                              pady=int(widht_line.get()),
                              font='Arial 5')
            tochka.place(x=int(tochka_x), y=tochka_y)
            # сохранение новой позиции
            infaa[0] = tochka_x
            infaa[1] = tochka_y
    except:
        errorlabel.config(text='ERROR: проверьте выбранное выше', bg='red', fg='white')


# создание окна
win = tk.Tk()
win.geometry('850x500+400+100')
win.title("paint")
win.config(background='white')
win.resizable(False, False)

# серый фон позади параметров
tk.Label(win, text='', padx=100, pady=600, bg='grey').place(x=0, y=0)
tk.Label(win, text='paint', bg='grey', fg='pink1', font='Arial 13', padx=1).place(x=30, y=5)
tk.Label(win, text='TO', bg='grey', fg='green', font='Arial 13', padx=1).place(x=70, y=5)
tk.Label(win, text='python', bg='grey', fg='blue3', font='Arial 13', padx=1).place(x=95, y=5)
tk.Label(win, text='brush options', bg='grey', fg='white', font='Arial 15').place(x=30, y=30)

# кисть
tochka = tk.Label(win, text='0', bg='black', fg='white', padx=3, pady=3, font='Arial 5')
tochka.place(x=205, y=1)
info = tochka.place_info()

# кнопки для перемещения кисти
btnup = tk.Button(win, text=' ^ ', bd=1, font='Arial 20', command=lambda: up())
btnup.place(x=75, y=350)
btnleft = tk.Button(win, text=' < ', bd=1, font='Arial 20', command=lambda: left())
btnleft.place(x=20, y=405)
btnright = tk.Button(win, text=' > ', bd=1, font='Arial 20', command=lambda: right())
btnright.place(x=126, y=405)
btndown = tk.Button(win, text='\/', bd=1, font='Arial 20', padx=7, command=lambda: down())
btndown.place(x=75, y=405)

# параметры для кисти
updown = ('up', 'down')
colors = ('red', 'green', 'yellow', 'black', 'blue', 'orange', 'brown', 'pink', 'grey', 'purple', 'white')

# удаление всего
delete_btn = tk.Button(win, text='delete', font='Arial 10', bd=1, pady=13, padx=7,
                       command=lambda: delete_all())
delete_btn.place(x=120, y=90)

# кнопка заливки фона
pouring_btn = tk.Button(win, text=' pouring ', bd=1, font='Arial 10', pady=13, command=pouring)
pouring_btn.place(x=20, y=90)

combo_color = ttk.Combobox(win, values=colors, font='Arial 10')
combo_color.current(0)  # начальное значение
combo_color.place(x=20, y=240)

combo = ttk.Combobox(win, values=updown, font='Arial 10')
combo.current(0)  # начальное значение
combo.place(x=20, y=280)

# будет изменяться в случае ошибки
errorlabel = tk.Label(win, font='Arial 8', bg='grey', pady=5)
errorlabel.place(x=6, y=310)

# толщина кисти
line_int = tk.Label(win, text='brush thickness', font='Arial 15', bg='grey', pady=5)
line_int.place(x=30, y=140)
widht_line = tk.Entry(win, font='Arial 20', width=5, justify='center')
widht_line.place(x=60, y=180)

# info creator
tk.Label(win, text='made by Sapega, tg: Kripersi', font='Arial 10', bg='grey').place(x=5, y=480)

win.mainloop()