# Ask the user for the filename
filename = input("Please enter the name of the text file to import: ")

# Open the text file in read mode
with open(filename, 'r') as file:
    content = file.read()


from tkinter import *

MAX_ATTEMPTS = 5

attempts = 0

def login():
    global attempts
    username = username_entry.get()
    password = password_entry.get()
  # Check the username and password
    if username == "user1" and password == "pass1":
        show_main_menu("User 1")
    elif username == "user2" and password == "pass2":
        show_main_menu("User 2")
