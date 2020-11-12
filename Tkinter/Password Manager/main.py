from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle 
import json

def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    password_entry.insert(0, password)

def save():
    website = website_entry.get().lower()
    email = email_entry.get().lower()
    password = password_entry.get()

    new_data = {
        website: {
            "email": email,
            "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="There are empty fields.!")
    
    else:   
        is_correct = messagebox.askokcancel(title=website, message=f"Verify your details \nEmail: {email} \npassword: {password}\n")

        if is_correct:
            try:
                with open("data.json", "r") as file:
                    data = json.load(file)
            
            except:
                with open("data.json", "w") as file:
                    json.dump(new_data, file, indent=4)
                
            else:
                data.update(new_data)

                with open("data.json", "w") as file:
                    json.dump(data, file, indent=4)

            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


def find_password():
    website = website_entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data doesn't exist")
    else:
        if website in data:
            email = data[website]["email"]
            password = data[website]["password"]
            messagebox.showinfo(title=website, message=f"Email: {email}\nPassword: {password}")
        else:
            messagebox.showerror(title="Error", message="Data doesn't exist")

def is_valid_password():
    password = entry.get()
    try:
        with open("data.json") as file:
            data = json.load(file)

    except FileNotFoundError:
        messagebox.showerror(title="Error", message="Data doesn't exist")

    else:
        if data["master_password"] == password:
            open_app()
        else:
            reply = messagebox.askretrycancel("Invalid master password", message="Try again")
            if not reply:
                window.destroy()
    

# UI
window = Tk()

window.config(padx=50, pady=50)

def open_app():
    entry.destroy()
    btn.destroy()
    global website_entry, password_entry, email_entry, canvas, logo_img
    window.title("Password Manager")
    # create a canvas and put the image on top of it
    canvas = Canvas(height=200, width=200)
    logo_img = PhotoImage(file="logo.png")
    canvas.create_image(100, 100, image=logo_img)
    canvas.grid(row=0, column=1)

        # Labels
    website_label = Label(text="Website:")
    website_label.grid(row=1, column=0)
    email_label = Label(text="Name/Email:")
    email_label.grid(row=2, column=0)
    password_label = Label(text="Password:")
    password_label.grid(row=3, column=0)

        #Input fields / Entries
    website_entry = Entry(width=35)
    website_entry.grid(row=1, column=1, columnspan=2)
    website_entry.focus()       # puts cursor here
    email_entry = Entry(width=35)
    email_entry.grid(row=2, column=1, columnspan=2)
    email_entry.insert(0, "hello2@gmail.com")
    password_entry = Entry(width=35)
    password_entry.grid(row=3, column=1, columnspan=2)

        # Buttons
    search_button = Button(text="Search", width=13, command=find_password)
    search_button.grid(row=1, column=2)
    generate_password_button = Button(text="Generate Password", width=13, command=generate_password)
    generate_password_button.grid(row=3, column=2)
    add_button = Button(text="Add", width=30, command=save)
    add_button.grid(row=4, column=1, columnspan=2)

def auth_window():
    window.title("Enter master password")
    global entry, btn
    entry = Entry(width=35)
    entry.grid(row=0, column=0)
    btn = Button(window, text="Confirm Password", command=is_valid_password)
    btn.grid(row=0, column=1)

auth_window()

window.mainloop()



