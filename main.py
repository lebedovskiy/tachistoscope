import tkinter as tk
import random


def check_var(event):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    global showen_digits
    showen_digits = random.shuffle(digits)
    lbl.after(50, lbl.grid(row=1, column=1))
    ent.delete(0,20)
    for i in range(5):
        if var.get() == i:
            for r in range(5):
                if var1.get() == r:
                    showen_digits = digits[:-(r+1)]
                    lbl.configure(text=showen_digits)
                    lbl.after(int((text_time[i]*1000)), lbl.grid_remove)
    return showen_digits


def answer(event):
    c = int(''.join((str(i) for i in showen_digits)))
    if int(your_answer.get()) == c:
        lbl.grid(row=1, column=1)
        your_answer.set('Верно!')
    else:
        lbl.grid(row=1, column=1)
        your_answer.set('Неверно!')

root = tk.Tk()
root.title('Tachistoscope')
frm_settings = tk.Frame(root)
frm_settings.grid(row=1, column=1)
frm_view = tk.Frame(root)
frm_view.grid(row=1, column=2)
""" Make Radiobuttons and Labels for digit's quality and time"""
var = tk.IntVar()
var1 = tk.IntVar()
text_time = [1, 0.5, 0.25, 0.1, 0.05]
text_dig = [9, 8, 7, 6, 5]
text = ['Выберите время', 'Выберите кол-во цифр']
rbn = []
rbn1 = []
frms = []
lbls = []
i = 0
for i in range(2):
    frms.append(tk.Frame(frm_settings))
    lbls.append(tk.Label(frms[i], text=text[i]))
    frms[i].grid(row=i, column=1)
    lbls[i].grid(row=i, column=0, columnspan=5, sticky='s')
    i += 1
i = 0
for i in range(5):
    rbn.append(tk.Radiobutton(frms[0], text=text_time[i], variable=var, value=i))
    rbn[i].grid(row=2, column=i)
    rbn1.append(tk.Radiobutton(frms[1], text=text_dig[i], variable=var1, value=i))
    rbn1[i].grid(row=2, column=i)
    i += 1
"""Make Label and Entry for tachistoscope"""
lbl2 = tk.Label(frm_view, width=35, height=3 )
"""this Label use for making window true width and height)"""
lbl2.grid(row=1,column=1, rowspan=3)
lbl = tk.Label(frm_view, font='arial 20')
lbl1 = tk.Label(frm_view, text='Введите увиденное число', )
lbl1.grid(row=4, column=1,)
your_answer = tk.StringVar()
ent = tk.Entry(frm_view, textvariable=your_answer)
ent.grid(row=5, column=1)
ent.bind('<Key-Return>', answer)
ent.bind('<space>', check_var)
btn = tk.Button(frm_settings, text='Начать!')
btn.grid(row=4,  column=1, sticky='s')
btn.bind('<Button-1>', check_var)
btn_answer = tk.Button(frm_view, text='Ответ!')
btn_answer.grid(row=6, column=1, sticky='s')
btn_answer.bind('<Button-1>', answer)
root.mainloop()
