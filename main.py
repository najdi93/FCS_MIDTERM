# we use stack overflow and more video youtube 
#split the value by ,
ile_path = "data.txt"

with open(file_path, "r") as file:
    lines = file.readlines()

data = []

for line in lines:
    values = line.strip().split(",")
    data.append(values)

print(data)

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
  
# Create and place widgets for the main menu
    Label(main_menu, text=f"Welcome, {username}!").pack()

    # Add more widgets for the main menu options

    # Start the main menu loop
    main_menu.mainloop()

# Create the main window
root = Tk()
root.title("Login Form")

# Create and place widgets for the login window
Label(root, text="Username:").pack()
username_entry = Entry(root)
username_entry.pack()

Label(root, text="Password:").pack()
password_entry = Entry(root, show="*")
password_entry.pack()

login_button = Button(root, text="Login", command=login)
login_button.pack()

result_label = Label(root, text="")
result_label.pack()
# Start the main loop for the login window
root.mainloop()
show_main_menu("User 2")
  else :
     
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

    # Add more widgets for the main menu options

    # Start the main menu loop
    main_menu.mainloop()

# Create the main window
root = Tk()
root.title("Login Form")

# Create and place widgets for the login window
Label(root, text="Username:").pack()
username_entry = Entry(root)
username_entry.pack()

Label(root, text="Password:").pack()
password_entry = Entry(root, show="*")
password_entry.pack()

login_button = Button(root, text="Login", command=login)
login_button.pack()

result_label = Label(root, text="")
result_label.pack()

# Start the main loop for the login window
root.mainloop()