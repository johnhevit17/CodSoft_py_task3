from tkinter import *
import string
import secrets
import random
import pyperclip


def generator():
    upper = list(string.ascii_uppercase)
    lower = list(string.ascii_lowercase)
    digits = list(string.digits)
    punctuation = list(string.punctuation)

    password_len = int(length_Box.get())
    part1 = round(password_len * 30/100) #letters 60%
    part2 = round(password_len * 20/100) #digits+punc 40%

    password = ""
    for i in range(part1):
        password += secrets.choice(upper)
        password += secrets.choice(digits)

    for i in range(part2):
        password += secrets.choice(punctuation)
        password += secrets.choice(lower)
    passwordField.delete(0, END)
    passwordField.insert(0, password)


def copy():
    random_password = passwordField.get()
    pyperclip.copy(random_password)


root = Tk()
root.geometry("220x220")

password_label = Label(root, text='Password Generator',
                       font=('Times', 18, 'bold'))
password_label.grid(pady=10)

length_label = Label(root, text="Password Length",
                     font=('cairo', 13, 'bold'))
length_label.grid()

length_Box = Spinbox(root, from_=4,
                     to=32,
                     font=('arial', 13, 'bold'), width=5, wrap=True)
length_Box.grid()

generateButton = Button(root,
                        text='Generate',
                        font=('arial', 10, 'bold'), command=generator)
generateButton.grid(pady=5)

passwordField = Entry(root, width=20, bd=2, font=('arial', 13, 'bold'))
passwordField.grid()

copyButton = Button(root, text='Copy to Clipboard',
                    font=('arial', 10, 'bold'), command=copy)
copyButton.grid(pady=5)

root.mainloop()
