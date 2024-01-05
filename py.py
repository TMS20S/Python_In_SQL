from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from db import Databese
db = Databese("employees.db")
root = Tk()
root.title('Exel_Sheets')
root.geometry('1210x515+45+100')
root.resizable(False,False)
root.configure(bg='#2c3e50')
name=StringVar()
Position=StringVar()
gender=StringVar()
age=StringVar()
email=StringVar()
phone=StringVar()
#======== button finctions======
def hide1():
    root.geometry("360x515")
    pass
def show1():
    root.geometry('1210x515')
    pass
def getData(event):
    selected_row=tv.focus()
    data=tv.item(selected_row)
    global row
    row=data["values"]
    name.insert(0,row[1])
    Position.set(row[2])
    gender.set(row[3])
    age.insert(0,row[4])
    email.insert(0,row[5])
    phone.insert(0,row[6])
    address.delete('1.0',END)
    address.insert(END,row[7])
def display():
    tv.delete(*tv.get_children())
    for row in db.fetch():
        tv.insert('',END,values=row)
def Clear():
    name.delete(0, END)
    Position.set("")
    gender.set("")
    age.delete(0, END)
    email.delete(0, END)
    phone.delete(0, END)
    address.delete('1.0',END)  
def Delet():
    db.delete(row[0])
    Clear()
    display()
def update():
    if name.get()=="" or age.get()=="" or Position.get()=="" or gender.get()=="" or email.get()=="" or phone.get()=="" or address.get(1.0,END)=="":
          messagebox.showerror("Error","Name is required")
          return
    db.update(row[0],
              name.get(),
              Position.get(),
              gender.get(),
              age.get(),
              email.get(),
              phone.get(),
              address.get(1.0,END)
              )
    messagebox.showinfo("success","The employ data is update")
    Clear()
    display()
    
def add():
      if name.get()=="" or age.get()=="" or Position.get()=="" or gender.get()=="" or email.get()=="" or phone.get()=="" or address.get(1.0,END)=="":
          messagebox.showerror("Error","Name is required")
          return
      db.insert(
          name.get(),
          Position.get(),
          gender.get(),
          age.get(),
          email.get(),
          phone.get(),
          address.get(1.0,END)
      )
      messagebox.showinfo("success","Added new employ ")
      Clear()
      display()
        


#========== ENTIRES ========
EntriesFrame=Frame(root,bg='#b7c7d7')#text="ENTRIES",relief=RIDGE,font=("Arial Bold", 16)
EntriesFrame.place(x=1,y=1,width=360,height=510)
title = Label(EntriesFrame,text='Employ',font=('Playfair Display', 16,'bold'),bg='#2c3e50',fg='#b7c7d7')
title.pack(fill=X)
name = Entry(EntriesFrame, font=('Arial', 14),textvariable=name)
position = Entry(EntriesFrame, font=('Arial', 14),textvariable=Position)
gender=ttk.Combobox(EntriesFrame, font=('Arial', 14),width=18,state='readonly',textvariable=gender)
age = Entry(EntriesFrame, font=('Arial', 14),textvariable=age)
email =Entry(EntriesFrame, font=('Arial', 14),textvariable=email)
phone=Entry(EntriesFrame, font=('Arial', 14),textvariable=phone)
address=Text(EntriesFrame, font=('Arial', 14))
gender['values']=("Male","Female")
name.place(x=100,y=36)
position.place(x=100,y=66)
gender.place(x=100,y=96)
age.place(x=100,y=126)
email.place(x=100,y=156)
phone.place(x=100,y=186)
address.place(x=10,y=250,width=340,height=50)

#========= label ========
name_label = Label(EntriesFrame,text='Name',font=('Arial', 14),bg='#b7c7d7',fg='#090d10')
position_label = Label(EntriesFrame,text='Position',font=('Arial', 14),bg='#b7c7d7',fg='#090d10')
gender_label=Label(EntriesFrame,text='Gender',font=('Arial', 14),bg='#b7c7d7',fg='#090d10')
age_label = Label(EntriesFrame,text='Age',font=('Arial', 14),bg='#b7c7d7',fg='#090d10')
email_label=Label(EntriesFrame,text='Email',font=('Arial', 14),bg='#b7c7d7',fg='#090d10')
phone_label=Label(EntriesFrame,text='Phone',font=('Arial', 14),bg='#b7c7d7',fg='#090d10')
address_label=Label(EntriesFrame,text='Address',font=('Arial', 14),bg='#b7c7d7',fg='#090d10')
name_label.place(x=0,y=36)
position_label.place(x=0,y=66)
gender_label.place(x=0,y=96)
age_label.place(x=0,y=126)
email_label.place(x=0,y=156)
phone_label.place(x=0,y=186)
address_label.place(x=150,y=216)
#====== Button (Add Details,Delet Details,Update Details,Clear Details)========

ButtonFrame=Frame(EntriesFrame,bg='#b7c7d7')
ButtonFrame.place(x=40,y=400,width=280,height=100)
add =Button(ButtonFrame,text='Add Details',font=('Arial', 14),bg='#c7b7d7',fg='#090d10',command=add)
del_details = Button(ButtonFrame, text='Delete Details', bg='#d7b7c7', fg='white', font=('Arial', 14),command=Delet)
update = Button(ButtonFrame,text='Update Details',font=('Arial', 14),bg='#b7d7c7',fg='#090d10',command=update)#bg=rgb(199,215,183)
clear = Button(ButtonFrame,text='Clear Details',font=('Arial', 14),bg='#c7d7b7',fg='#090d10',command=Clear)
show_button=Button(EntriesFrame,text='Show',font=('Arial', 10),bg='#415b75',fg='#d0dbe5',command=show1)
hide_button=Button(EntriesFrame,text='Hide',font=('Arial', 10),bg='#10161d',fg='#7896b4',command=hide1)
add.place(x=0,y=0,width=140,height=50)
update.place(x=140,y=0,width=140,height=50)
del_details.place(x=0,y=50,width=140,height=50)
clear.place(x=140,y=50,width=140,height=50)
hide_button.place(x=250,y=10,width=40,height=20)
show_button.place(x=300,y=10,width=40,height=20)
#======== Teble Frame ==========

TebleFrame=Frame(root,bg='#dde5ec')
TebleFrame.place(x=365,y=1,width=940,height=510)
style=ttk.Style()
style.configure("myStyle.Treeview",font=("Arial Bold", 16),rowheight=50)
style.configure("myStyle.Treeview.Heading",font=("Arial Bold", 16))
tv=ttk.Treeview(TebleFrame,columns=(1,2,3,4,5,6,7,8),style="MyStyle.Treeview")
tv.heading("1",text='ID')
tv.heading("2",text='Name')
tv.heading("3",text='Position')
tv.heading("4",text='Gender')
tv.heading("5",text='Age')
tv.heading("6",text='Email')
tv.heading("7",text='Phone')
tv.heading("8",text='Address')
tv.column("1",width=40)
tv.column("2",width=140)
tv.column("3",width=50)
tv.column("4",width=120)
tv.column("5",width=150)
tv.column("6",width=90)
tv.column("7",width=150)
tv.column("8",width=110)
tv['show']='headings'
tv.bind("<ButtonRelease-1>",getData)
tv.place(x=1,y=1,height=610)
display()
root.mainloop()

