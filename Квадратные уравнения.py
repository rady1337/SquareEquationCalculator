# -*- coding: utf-8 -*-

from tkinter import *
import math


def main():
	result.delete(1.0, END)
	try:
		a = a_entry.get()
		if a == '':
			a = 1
		else:
			a = float(a)
		b = float((b_entry.get()))
		c = float(c_entry.get())
		d = b ** 2 - (4 * a * c)
		if '.0' in str(d):
			index = str(d).index('.')
			d = int(d)
		if d < 0:
			result.insert(END, 'Ответ:\nD < 0\nКорней нет')
		elif d > 0:
			x1 = (-b + math.sqrt(d)) / (2 * a)
			if '.0' in str(x1):
				x1 = int(x1)
			x2 = (-b - math.sqrt(d)) / (2 * a)
			if '.0' in str(x2):
				x2 = int(x2)
			result.insert(END, f'Ответ:\nD = {d}\nX₁ = {round(x1, 2)}\nX₂ = {round(x2, 2)}')
		elif d == 0:
			x = (-b) / (2 * a)
			if '.0' in str(x):
				x = int(x)
			result.insert(END, f'Ответ:\nD = {d}\nX₁ = X₂ = {round(x, 2)}')
	except:
		result.insert(END, 'ОШИБКА!\nПопробуйте ещё раз')


# Create windows
win = Tk()

# Set window color
win['bg'] = '#292929'

# Set window name
win.title('Калькулятор Квадратных Уравнений')

# Set windows resolution
win.geometry('235x250')

# Disable resizable
win.resizable(width=True, height=False)

al = Label(win, text='ax² + bx + c = 0', font='Times 20',  bg='#292929',
               fg="white")
a_label = Label(win, text='a =: ', font='Times 15',  bg='#292929',
               fg="white")
a_entry = Entry(win, width=5, font='Times 15',  bg='#292929',
               fg="white")
b_label = Label(win, text='b =: ', font='Times 15',  bg='#292929',
               fg="white")
b_entry = Entry(win, width=5, font='Times 15',  bg='#292929',
               fg="white")
c_label = Label(win, text='c =: ', font='Times 15',  bg='#292929',
               fg="white")
c_entry = Entry(win, width=5, font='Times 15',  bg='#292929',
               fg="white")

btn = Button(win,  text='Посчитать', font='Times 15',  bg='#292929',
               fg="white", command=main)
result = Text(win, width=23, height=4, wrap=WORD, font='Times 15',  bg='#292929',
               fg="white" )

al.grid(column=0, row=0)
a_label.grid(column=0, row=1)
a_entry.grid(column=1, row=1)

b_label.grid(column=0, row=2)
b_entry.grid(column=1, row=2)

c_label.grid(column=0, row=3)
c_entry.grid(column=1, row=3)
btn.grid(column=0, row=4)
result.place(x=1, y=160)





win.mainloop()