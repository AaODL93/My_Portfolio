import tkinter as tk
from tkinter import messagebox
import random
import pyperclip

WHITE_COLOR = "#ecfcff"
FONT_NAME = "Courier"

# ---------------------------------------- PASSWORD GENERATOR ------------------------------------------- #


def generate_password():
    """Function used to generate a random password with a combination of 8-10 letters, 2-4 symbols and 2-4 numbers with
    a random order."""
    password = password_entry.get()
    if len(password) > 0:
        password_entry.delete(0, tk.END)

    else:
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N',
                   'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_letters = [random.choice(letters) for letter in range(nr_letters)]

        password_symbols = [random.choice(symbols) for symbol in range(nr_symbols)]

        password_numbers = [random.choice(numbers) for number in range(nr_numbers)]

        password_list = password_letters + password_symbols + password_numbers

        random.shuffle(password_list)

        password = "".join(password_list)

        password_entry.insert(index=0, string=password)

        pyperclip.copy(password)

# ---------------------------------------- SAVE PASSWORD ------------------------------------------- #


def save():
    website = website_entry.get()
    email = email_username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        not_ok = messagebox.showwarning(title="WARNING", message="Don't leave any field empty.")

    else:
        is_ok = messagebox.askokcancel(title=f"Website: {website}",
                                       message=f"These are the details entered: "
                                               f"\nEmail: {email}\n"
                                               f"Password: {password}\n"
                                               f"Is it ok to save?")

        if is_ok:
            with open("data.txt", mode="a") as password_list:
                password_list.write(f"{website} | {email} | {password}")
                website_entry.delete(0, tk.END)
                password_entry.delete(0, tk.END)

# ---------------------------------------- UI SETUP ------------------------------------------- #


window = tk.Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = tk.Canvas(width=204, height=204, highlightthickness=0, bg=WHITE_COLOR)
logo_image = tk.PhotoImage(file="logo.png")
canvas.create_image(102, 102, image=logo_image)
canvas.grid(column=1, row=0)

# LABELS
website_label = tk.Label()
website_label.config(text="Website:", bg=WHITE_COLOR, font=(FONT_NAME, 12))
website_label.grid(column=0, row=1)

email_username_label = tk.Label()
email_username_label.config(text="Email/Username:", bg=WHITE_COLOR, font=(FONT_NAME, 12))
email_username_label.grid(column=0, row=2)

password_label = tk.Label()
password_label.config(text="Password:", bg=WHITE_COLOR, font=(FONT_NAME, 12))
password_label.grid(column=0, row=3)

# ENTRIES
website_entry = tk.Entry(width=51)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_username_entry = tk.Entry(width=51)
email_username_entry.grid(column=1, row=2, columnspan=2)
# TODO Enter your email address as a parameter on the next line, so you don't have to capture it every single time.
email_username_entry.insert(index=0, string="YOUR EMAIL ADDRESS")

password_entry = tk.Entry(width=32)
password_entry.grid(column=1, row=3)

# BUTTONS
generate_password_button = tk.Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=3)

add_button = tk.Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
