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
    else:
        attempts += 1
        remaining_attempts = MAX_ATTEMPTS - attempts
        if remaining_attempts > 0:
            result_label.config(text=f"Login failed. {remaining_attempts} attempts remaining.")
        else:
            result_label.config(text="Login failed. No more attempts allowed.")
            username_entry.config(state=DISABLED)
            password_entry.config(state=DISABLED)
            login_button.config(state=DISABLED)
def show_main_menu(username):
    root.destroy()  # Close the login window

    main_menu = Tk()
    main_menu.title(f"Welcome, {username}")

    # Create and place widgets for the main menu
    Label(main_menu, text=f"Welcome, {username}!").pack()
