# -"- coding:utf-8 -"-
from tkinter import*
import math

def solve():
    A = digA.get('1.0', END)
    B = digB.get('1.0', END)
    C = digC.get('1.0', END)
    try:
        A = int(A)
        B = int(B)
        C = int(C)
        D = b**2 - (4*a*c)
        diskr.config(text=D)
        if D > 0:
            x1 = ((-1)*b + math.sqrt(D))/(2*a)
            x2 = ((-1)*b - math.sqrt(D))/(2*a)
            xodin.config(text=x1)
            xdva.config(text=x2)
        elif D == 0:
            x1 = ((-1)*b)/(2*a)
            xodin.config(text=x1)
            xdva.config(text='-')
        elif D < 0:
            xodin.config(text='x∈∅')
            xdva.config(text='-')
    except Exception:
        labelError.config(text='Error')
        def nuke():
            labelError.config(text='')
        root.after(3000, nuke)

root = Tk()
U = Label(root,text='Ax²+Bx+C=0')
labelA = Label(root,text='A =')
labelB = Label(root,text='B =')
labelC = Label(root,text='C =')
digA = Text(root,width=5,height=1)
digB = Text(root,width=5,height=1)
digC = Text(root,width=5,height=1)
solver = Button(root,width=5,height=5,text='Решить',command=solve)
D_ravno = Label(root,text='D =')
diskr = Label(root,text='')
x1_ravno = Label(root,text='x1 =')
xodin = Label(root,text='')
x2_ravno = Label(root,text='x2 =')
xdva = Label(root,text='')
labelError = Label(root,text='')

U.grid(row=0,column=0)
labelA.grid(row=1,column=0)
labelB.grid(row=2,column=0)
labelC.grid(row=3,column=0)
digA.grid(row=1,column=1)
digB.grid(row=2,column=1)
digC.grid(row=3,column=1)
solver.grid(row=2,column=2)
D_ravno.grid(row=4,column=0)
diskr.grid(row=4,column=1)

root.mainloop()
