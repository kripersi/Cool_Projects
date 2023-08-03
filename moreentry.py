import tkinter as tk
import random


def up():
    entry1 = entry.get()
    entry.delete(0, 'end')
    entry.insert(0, entry1.upper())


def lowe():
    entry1 = entry.get()
    entry.delete(0, 'end')
    entry.insert(0, entry1.lower())


def tit():
    entry1 = entry.get()
    entry.delete(0, 'end')
    entry.insert(0, entry1.title())


def capit():
    entry1 = entry.get()
    entry.delete(0, 'end')
    entry.insert(0, entry1.capitalize())


def reve():
    entry1 = entry.get()
    entry.delete(0, 'end')
    entry.insert(0, entry1[::-1])


def binn():
    entry1 = entry.get()
    entry.delete(0, 'end')
    binarn = []
    for i in entry1:
        binarn.append(ord(i))
    entry.insert(0, binarn)


def ran_low_up():
    entry1 = entry.get()
    entry.delete(0, 'end')
    spis_entry = []
    for i in range(len(entry1)):
        k=random.randint(1,2)
        if k==1:
            spis_entry.append(entry1[int(i)].upper())
        else:
            spis_entry.append(entry1[int(i)].lower())
    entry.insert(0, ''.join(spis_entry))


win = tk.Tk()  # создание окна
win.geometry('400x300+700+100')
win.title('работа в тексте')
win.config(background='#82c1ed')
# win.resizable(False, False)

tk.Label(text='рAзн.е тeksта', bg='#82c1ed', font=('Arial',13, 'bold')).place(x=150, y=10)

entry = tk.Entry(win, font=(50))
entry.place(x=120, y=100)

btnup = tk.Button(win, text='UPPER',bd=0, bg='#4294cf',activebackground='#02487a', fg='black', font=('Arial', 13, 'bold'),
                  command=lambda: up())
btnup.place(x=10, y=150)

btnlow = tk.Button(win, text='lower',bd=0, bg='#4294cf',activebackground='#02487a', fg='black', font=('Arial', 13, 'bold'),
                  command=lambda: lowe())
btnlow.place(x=90, y=150)

btntit = tk.Button(win, text='Title',bd=0, bg='#4294cf',activebackground='#02487a',fg='black', font=('Arial', 13, 'bold'),
                  command=lambda: tit())
btntit.place(x=155, y=150)

btnran = tk.Button(win, text='low&UP',bd=0, bg='#4294cf',activebackground='#02487a', fg='black', font=('Arial', 13, 'bold'),
                   command=lambda: ran_low_up())
btnran.place(x=215, y=150)

btncap = tk.Button(win, text='Capitalize',bd=0, bg='#4294cf',activebackground='#02487a', fg='black', font=('Arial', 13, 'bold'),
                   command=lambda: capit())
btncap.place(x=300, y=150)

# 2 строка

btnbin = tk.Button(win, text='binarn',bd=0, bg='#4294cf',activebackground='#02487a', fg='black', font=('Arial', 13, 'bold'),
                   command=lambda: binn())
btnbin.place(x=127, y=220)

btnreve = tk.Button(win, text='reverse',bd=0, bg='#4294cf',activebackground='#02487a', fg='black', font=('Arial', 13, 'bold'),
                   command=lambda: reve())
btnreve.place(x=220, y=220)




win.mainloop()