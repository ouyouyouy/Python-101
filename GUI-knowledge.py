from tkinter import *
from tkinter import ttk # theme of tk
from tkinter import messagebox

GUI = Tk() #นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล')#นี่คือชื่อโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดโปรแกรม

L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=100,y=300)

B1 = ttk.Button(GUI,text='เงินมีอยู่กี่บาท')
B1.pack(ipadx=20,ipady=20)

#######################
def Button2():
    text = 'ตอนนี้มีเงินในบัญชี 300 บาท'
    messagebox.showinfo('เงินในบัญชี',text)#showinfo,showwarning,showerror
                    

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=200,y=200)
B2 = ttk.Button(FB1,text='เงินมีอยู่กี่บาท',command=Button2)
B2.pack(ipadx=20,ipady=20)

#######################

def Button3():
    text = 'Python101,Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 ก.ค.',text)#showinfo,showwarning,showerror
                    

FB2 = Frame(GUI) #คล้ายกระดาน
FB2.place(x=100,y=100)
B3 = ttk.Button(FB2,text='สัปดาห์นี้เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)

#######################3
GUI.mainloop()
