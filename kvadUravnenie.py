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
        D = B**2 - (4*A*C)
        diskr.config(text=D)
        if D > 0:
            x1 = ((-1)*B + math.sqrt(D))/(2*A)
            x2 = ((-1)*B - math.sqrt(D))/(2*A)
            xodin.config(text=x1)
            xdva.config(text=x2)
        elif D == 0:
            x1 = ((-1)*B)/(2*A)
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
root.minsize(400,325)
root.resizable(False,False)
U = Label(root,text='Ax²+Bx+C=0',font='Arial 20')
labelA = Label(root,text='A =',font='Arial 16')
labelB = Label(root,text='B =',font='Arial 16')
labelC = Label(root,text='C =',font='Arial 16')
digA = Text(root,width=5,height=1,font='Arial 16')
digB = Text(root,width=5,height=1,font='Arial 16')
digC = Text(root,width=5,height=1,font='Arial 16')
solver = Button(root,width=6,height=5,text='Решить',command=solve,font='Arial 16')
D_ravno = Label(root,text='D =',font='Arial 16')
diskr = Label(root,text='',font='Arial 16')
x1_ravno = Label(root,text='x1 =',font='Arial 16')
xodin = Label(root,text='',font='Arial 16')
x2_ravno = Label(root,text='x2 =',font='Arial 16')
xdva = Label(root,text='',font='Arial 16')
labelError = Label(root,text='',font='Arial 16')

U.grid(row=0,column=1)
labelA.grid(row=1,column=0)
labelB.grid(row=2,column=0)
labelC.grid(row=3,column=0)
digA.grid(row=1,column=1)
digB.grid(row=2,column=1)
digC.grid(row=3,column=1)
solver.grid(row=2,column=2)
D_ravno.grid(row=4,column=0)
diskr.grid(row=4,column=1)
x1_ravno.grid(row=5,column=0)
xodin.grid(row=5,column=1)
x2_ravno.grid(row=6,column=0)
xdva.grid(row=6,column=1)
labelError.grid(row=2,column=3)

root.mainloop()
