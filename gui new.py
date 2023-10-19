from tkinter import *
from tkinter import ttk
from tkinter import messagebox

GUI = Tk()
GUI.title('Programme for data')
GUI.geometry('1000x800')

L1 = Label(GUI,text='Programme for data',font=('Angsana New',50),fg='blue')
L1.place(x=100,y=30)
L2 = Label(GUI,text='Data',font=('Angsana New',30),fg='blue')
L2.place(x=100,y=150)
#B1 = ttk.Button(GUI,text='มีเงินเท่าไร')
#B1.pack(ipadx=50,ipady=50)

def Button2():
    text = 'Transaction in Today'
    messagebox.showinfo('Today',text)

FB2 = Frame(GUI)
FB2.place(x=200,y=200)
B2 = ttk.Button(FB2,text='History',command=Button2)
B2.pack(ipadx=20,ipady=20)
########################################################

def Button3():
    text = 'Buy confirm'
    messagebox.showinfo('Buy',text)

FB3 = Frame(GUI)
FB3.place(x=100,y=400)
B3 = ttk.Button(FB3,text='Buy',command=Button3)
B3.pack(ipadx=10,ipady=10)
#######################################################

def Button4():
    text = 'Sell confirm'
    messagebox.showinfo('Sell',text)

FB4 = Frame(GUI)
FB4.place(x=400,y=400)
B4 = ttk.Button(FB4,text='Sell',command=Button4)
B4.pack(ipadx=10,ipady=10)
######################################################

def Button5():
    text = 'Confirm'
    messagebox.showinfo('OK',text)

FB5 = Frame(GUI)
FB5.place(x=220,y=400)
B5 = ttk.Button(FB5,text='OK',command=Button5)
B5.pack(ipadx=5,ipady=5)
#########################################################

def Button6():
    text = "Confirm"
    messagebox.showinfo('Cancel',text)
    
FB6 = Frame(GUI)
FB6.place(x=300,y=400)
B6 = ttk.Button(FB6,text='Cancel',command=Button6)
B6.pack(ipadx=5,ipady=5)




GUI.mainloop()




