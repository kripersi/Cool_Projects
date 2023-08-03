import tkinter as tk

user = {'artem': '12344',
        'dima': '8829',
        'nikita': 'qwe',
        'ivan': 'ivanpro'}


def potv():
    name = vvod.get()
    passw = password.get()
    if name and passw:
        if name in user and passw == user[name]:
            ms.config(text=f'Здраствуйте {name}', bg='orange')
        elif name not in user:
            ms.config(text='регистрация прошла успешно!', bg='green')
            user[name]=passw
            potvnamee = tk.Button(win, text='войти', bg='#FFDEAD', activebackground='green',
                                 command=potv).grid(row=3, column=1, columnspan=3, stick='e')
        else:
            ms.config(text='пользователь с таким именем уже есть', bg='blue')
    else:
        ms.config(text='вы не заполнили одно из полей!', bg='red')

win = tk.Tk()  # создание окна
win.geometry('500x130+700+100')
win.title('registration')
win.config(background='#FFDEAD')

reg = tk.Label(win, text=' Регистрация', bg='#FFDEAD', fg='#483D8B', font=('Serif', 20, 'bold')).grid(row=0, column=1,columnspan=4, stick='w')
name = tk.Label(win, text='Name', bg='#FFDEAD', fg='#483D8B', font=('Serif', 12, 'bold')).grid(row=1, column=0, stick='w')
passw = tk.Label(win, text='Password', bg='#FFDEAD', fg='#483D8B', font=('Serif', 12, 'bold')).grid(row=2, column=0, stick='w')
potvname = tk.Button(win, text='потведрить', bg='#FFDEAD', activebackground='blue', command=potv).grid(row=3, column=1)

vvod = tk.Entry(win) # если добавить show='*' то будет как пароль
vvod.grid(row=1, column=1, stick='e')

password = tk.Entry(win, show='*')
password.grid(row=2, column=1, stick='e')

ms = tk.Label(win,text='пройдите регистрацию', bg='red')
ms.grid(row=1, column=5, rowspan=2, stick='ns')



win.mainloop()

