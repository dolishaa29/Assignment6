from tkinter import *
window=Tk()
window.geometry('500x500')

#Entry Box
e=Entry(window,width=56,borderwidth=5)
e.place(x=0,y=0)

#Buttons
def click(num):
    result=e.get()
    e.delete(0,END)
    e.insert(0,str(result)+str(num))

b=Button(window,text='1',width=12,command=lambda:click(1))
b1=Button(window,text='2',width=12,command=lambda:click(2))
b2=Button(window,text='3',width=12,command=lambda:click(3))
b3=Button(window,text='4',width=12,command=lambda:click(4))
b4=Button(window,text='5',width=12,command=lambda:click(5))
b5=Button(window,text='6',width=12,command=lambda:click(6))
b6=Button(window,text='7',width=12,command=lambda:click(7))
b7=Button(window,text='8',width=12,command=lambda:click(8))
b8=Button(window,text='9',width=12,command=lambda:click(9))
b9=Button(window,text='0',width=12,command=lambda:click(0))

#operators:
def add():
    n1=e.get()
    global math
    math='addition'
    global i
    i=int(n1)
    e.delete(0,END)

b10=Button(window,text='+',width=12,command=add)

def sub():
    n1=e.get()
    global math
    math='subtraction'
    global i
    i=int(n1)
    e.delete(0,END)

b11=Button(window,text='-',width=12,command=sub)

def mul():
    n1=e.get()
    global math
    math = 'multiplication'
    global i
    i=int(n1)
    e.delete(0,END)


b12=Button(window,text='x',width=12,command=mul)

def div():
    n1=e.get()
    global math
    math = 'division'
    global i
    i=int(n1)
    e.delete(0,END)



b13=Button(window,text='/',width=12,command=div)


def equal():
    n2=e.get()
    e.delete(0,END)
    if math=='addition':
        e.insert(0,i+int(n2))
    elif math=='subtraction':
        e.insert(0,i-int(n2))
    elif math=='multiplication':
        e.insert(0,i*int(n2))
    elif math=='division':
        e.insert(0,i/int(n2))

b14=Button(window,text='=',width=12,command=equal)

def clear():
    e.delete(0,END)
b15=Button(window,text='clear',width=12,command=clear)

b.place(x=10,y=60)
b1.place(x=80,y=60)
b2.place(x=170,y=60)
b3.place(x=10,y=120)
b4.place(x=80,y=120)
b5.place(x=170,y=120)
b6.place(x=10,y=180)
b7.place(x=80,y=180)
b8.place(x=170,y=180)
b9.place(x=10,y=240)
b10.place(x=80,y=240)
b11.place(x=170,y=240)
b12.place(x=10,y=300)
b13.place(x=80,y=300)
b14.place(x=170,y=300)
b15.place(x=80,y=360)


mainloop()