from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
import pyperclip
import json

FONT = ('Arial', 12)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    password_lett = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice (numbers) for _ in range(randint(2, 4))]
    password_list = password_lett + password_symbols + password_numbers
    shuffle(password_list)
    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {
        website : {
        'email' : email,
        'password' : password,
        }
    }
    if len(website) == 0 or len(password) == 0:
        messagebox.showinfo(title='Ooops', message="Please make sure you haven't left any fields empty")
    else:
        try:
            with open('data.json', 'r') as file:
            #Reading old data
                data = json.load(file)
        except FileNotFoundError:
            with open("data.json", 'w') as file:
                json.dump(new_data, file, indent=4)
        else:
            #Updating old data with new data
            data.update(new_data)
            with open ("data.json", 'w') as file:
            #Saving updated data
                json.dump(data, file,indent=4)
        finally:
            website_entry.delete(0, END)
            password_entry.delete(0, END)

# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    website = website_entry.get()
    try:
        with open('data.json') as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title='Error', message='No Data File Found')
    else:
        if website in data:
            email = data[website]['email']
            password = data[website]['password']
            messagebox.showinfo(title=website, message=f'Email: {email}\n Password: {password}')
        else:
            messagebox.showinfo(title='Error', message=f'No details for {website} exist')

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.config(width=400, height=600, padx=50, pady=50)
window.title('Password Manager')

canvas = Canvas(width=200, height=200)
lock_img = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=lock_img)
canvas.grid(column=1, row=0)

#website label
website_label = Label(text='Website:', font=FONT)
website_label.grid(column=0, row=1)

#website entry
website_entry = Entry(width=22)
website_entry.grid(column=1, row=1)
website_entry.focus()
website_entry.insert(index=0, string='')


#email label
email_label = Label(text='Email/Username:', font=FONT)
email_label.grid(column=0, row=2)

#email_entry
email_entry = Entry(width=35)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, 'lukwiecz@gmail.com')

#password label
password_label = Label(text='Password:', font=FONT)
password_label.grid(column=0, row=3)

#password entry
password_entry = Entry(width=22)
password_entry.grid(column=1, row=3)

#generate password button
generate_password_button = Button(text='Generate Password', font=FONT, command=generate_password)
generate_password_button.grid(column=2, row=3)

#add button
add_button = Button(text='Add', font=FONT, width=45, command=save)
add_button.grid(column=1, row=4, columnspan=2)

#search button
search_button = Button(text='Search', font=FONT, width=16, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
