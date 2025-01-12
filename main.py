'''
======= CREATED BY PAUL MENDOZA =======
======= PYTHON 3.12.7 =======
'''


from tkinter import *
from tkinter import messagebox
import traceback


root = Tk()
root.geometry('800x600')
root.title('Percentage Calculator')
root.iconbitmap('images/logo.ico')
root.resizable(False, False)

def e(value):
    try:
        float_value = float(value.replace(",", "."))
        return not (float_value != float_value or float_value == float('inf') or float_value == -float('inf'))
    except ValueError:
        return False

def calculate1():
    a = input1_1.get()
    r = input2_1.get()
    u = False
    
    if e(a):
        entry1_1.config(bg="#fff")
    else:
        entry1_1.config(bg="#fee")
        u = True

    if e(r):
        entry2_1.config(bg="#fff")
    else:
        entry2_1.config(bg="#fee")
        u = True

    if u:
        return
    c = 0
    c = float(a.replace(",", ".")) / 100 * float(r.replace(",", "."))

    result1.set(c)
    
def calculate2():
    a = input1_2.get()
    r = input2_2.get()
    u = False
    
    if e(a):
        entry1_2.config(bg="#fff")
    else:
        entry1_2.config(bg="#fee")
        u = True

    if e(r):
        entry2_2.config(bg="#fff")
    else:
        entry2_2.config(bg="#fee")
        u = True

    if u:
        return
    c = 0
    c = float(a.replace(",", ".")) / float(r.replace(",", ".")) * 100

    result2.set(c)
    
def calculate3():
    a = input1_3.get()
    r = input2_3.get()
    u = False
    
    if e(a):
        entry1_3.config(bg="#fff")
    else:
        entry1_3.config(bg="#fee")
        u = True

    if e(r):
        entry2_3.config(bg="#fff")
    else:
        entry2_3.config(bg="#fee")
        u = True

    if u:
        return
    c = 0
    c = (float(r.replace(",", ".")) - float(a.replace(",", "."))) / float(a.replace(",", ".")) * 100

    result3.set(c)
    

def clear_entries():
    entry1_1.delete(0, END)
    entry2_1.delete(0, END)
    entry3_1.delete(0, END)
    entry1_2.delete(0, END)
    entry2_2.delete(0, END)
    entry1_3.delete(0, END)
    entry2_3.delete(0, END)
    entry3_3.delete(0, END)

try:
    background = PhotoImage(file='images/logo.png')
    background_label = Label(root, image=background)
    background_label.pack()
except Exception as e:
    messagebox.showerror('Error', f'{e}\n{traceback.format_exc()}')
    root.destroy()

try:
    background2 = PhotoImage(file='images/frame.png')
    background_label2 = Label(root, image=background2)
    background_label2.pack()
except Exception as e:
    messagebox.showerror('Error', f'{e}\n{traceback.format_exc()}')
    root.destroy()



label1 = Label(root, text='Percentage Calculator is a tool to calculate percentages.',
               font=('Georgia', 10), bg='#D9D9D9', fg='black')
label1.place(x=20, y=210)

# First Row
input1_1 = StringVar()
input2_1 = StringVar()
result1 = StringVar()
entry1_1 = Entry(root, width=12, bd=2, font=('Banscrift', 10),textvariable=input1_1)
entry1_1.place(x=120, y=260)
entry2_1 = Entry(root, width=12, bd=2, font=('Banscrift', 10),textvariable=input2_1)
entry2_1.place(x=290, y=260)
btn1 = Button(root, width=10, text='CALCULATE', bg='#336699', font=('Banscrift', 10, 'bold'),
              fg='white', activebackground='green', cursor='hand2',command=calculate1)
btn1.place(x=530, y=255)
entry3_1 = Entry(root, width=12, bd=2, font=('Banscrift', 10),textvariable=result1, state='readonly')
entry3_1.place(x=630, y=260)
btn_clear = Button(root, width=10, text='Clear', bg='#336699', font=('Banscrift', 10, 'bold'),
                   fg='white', activebackground='green', cursor='hand2', command=clear_entries)
btn_clear.place(x=630, y=300)

# Second Row
input1_2 = StringVar()
input2_2 = StringVar()
result2 = StringVar()
entry1_2 = Entry(root, width=12, bd=2, font=('Banscrift', 10),textvariable=input1_2)
entry1_2.place(x=60, y=387)
entry2_2 = Entry(root, width=12, bd=2, font=('Banscrift', 10),textvariable=input2_2)
entry2_2.place(x=320, y=387)
btn2 = Button(root, width=10, text='CALCULATE', bg='#336699', font=('Banscrift', 10, 'bold'),
              fg='white', activebackground='green', cursor='hand2',command=calculate2)
btn2.place(x=530, y=382)
entry3_2 = Entry(root, width=12, bd=2, font=('Banscrift', 10),textvariable=result2, state='readonly')
entry3_2.place(x=630, y=387)

# Third Row
input1_3 = StringVar()
input2_3 = StringVar()
result3 = StringVar()
entry1_3 = Entry(root, width=12, bd=2, font=('Banscrift', 10),textvariable=input1_3)
entry1_3.place(x=110, y=525)
entry2_3 = Entry(root, width=12, bd=2, font=('Banscrift', 10),textvariable=input2_3)
entry2_3.place(x=280, y=525)
btn3 = Button(root, width=10, text='CALCULATE', bg='#336699', font=('Banscrift', 10, 'bold'),
              fg='white', activebackground='green', cursor='hand2',command=calculate3)
btn3.place(x=530, y=520)
entry3_3 = Entry(root, width=12, bd=2, font=('Banscrift', 10),textvariable=result3, state='readonly')
entry3_3.place(x=630, y=525)
labelqm= Label(root, text='?',
               font=('Banscrift', 10,'bold'), bg='#D9D9D9', fg='black')
labelqm.place(x=400, y=525)



root.mainloop()