from tkinter import *
from random import randint
w=Tk()
w.title('Password Generator')
w.geometry("500x300")
lf=LabelFrame(w,text="How Many Characters?")
lf.pack(pady=20)
my_entry=Entry(lf,font=("Helvetica",24),background="lightyellow")
my_entry.pack(pady=20,padx=20)
pw=Entry(w,text='',font=("Helevetica",24),background="pink")
pw.pack(pady=20)
def generate_password():
    pw.delete(0,END)
    try:
          pw_length=int(my_entry.get())
          my_password=''
          for x in range(pw_length):
              my_password+=chr(randint(33,126))
              pw.insert(0,my_password)
    except Exception as e:
         my_password="Enter valid number"
         pw.insert(0,my_password)
my_frame=Frame(w)
my_frame.pack(pady=20)
my_button=Button(my_frame,text="Generate strong password",background="blue",command=generate_password)
my_button.grid(row=0,column=0,padx=10)
w.mainloop()
