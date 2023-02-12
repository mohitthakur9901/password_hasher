from tkinter import *
from tkinter import messagebox
from random import randint,choice,shuffle
import pyperclip
import json
window=Tk()
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def password_generater():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
               'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H',
               'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_list = []
    letter=[password_list.append(choice(letters)) for _ in range(randint(4, 8))]
    symbol=[password_list.append(choice(symbols))for _ in range(randint(2, 4))]
    num=[password_list.append(choice(numbers)) for _ in range(randint(2, 4))]
    shuffle(password_list)
    password="".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_file():
    a=website_entry.get()
    b=email_entry.get()
    c=password_entry.get()
    new_data={
        a:{
            "email":b,
            "password":c,
        }
    }

    if len(a) == 0 or len(b) == 0:
        messagebox.showinfo(title="OOPS", message="don't leave any line empty")

    try:
        with open("data.json","r") as data_file:
                data=json.load(data_file,)

    except FileNotFoundError:
        with open("data.json","w") as data_file:
            json.dump(new_data,data_file,indent=4)
    else:
        data.update(new_data)
        with open("data.json", "w") as data_file:
            json.dump(data,data_file,indent=4)
    finally:
        website_entry.delete(0, END)
        email_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    web=website_entry.get()
    try:
        with open("data.json") as data_file:
            data=json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="OOPS",message="FILE NOT FOUND")
    else:
        if web in data:
            EMAIL = data[web]["email"]
            PASSWORD = data[web]["password"]
            messagebox.showinfo(title=web, message=f"EMAIL: {EMAIL}\n "
                                                   f"PASSWORD: {PASSWORD}")
        else:
            messagebox.showinfo(title="NOT SAVED",message=f"YOU DIDN'T SAVE {web} INFORMATION")
# ---------------------------- UI SETUP ------------------------------- #

window.title("PASSWORD MANAGER")
window.config(padx=50,pady=50)
canvas=Canvas(width=200,height=200,)
lock=PhotoImage(file="logo.png")
canvas.create_image(100,100,image=lock)
canvas.grid(column=1,row=0)
#Labels

website=Label(text="WEBSITE:")
website.grid(row=1,column=0)
emai=Label(text="ENMAIL/USERNAME:")
emai.grid(row=2,column=0)
password=Label(text="PASSWORD:")
password.grid(row=3,column=0)
#entry
website_entry=Entry(width=30)
website_entry.grid(row=1,column=1)
website_entry.focus()

email_entry=Entry(width=35)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,string="mohitthakur9901@gmail.com")
password_entry=Entry(width=21,)
password_entry.grid(row=3,column=1)
#user buttons
search_button=Button(text="SEARCH",width=20,command=find_password)
search_button.grid(row=1,column=2)
genrate_button=Button(text="GENERATE BUTTON",command=password_generater)
genrate_button.grid(row=3,column=2)
add_button=Button(text="ADD PASSWORD",width=36,command=save_file)
add_button.grid(row=4,column=1,columnspan=2)

window.mainloop()