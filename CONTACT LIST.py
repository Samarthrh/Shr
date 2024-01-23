import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation
import tkinter as tk
from tkinter import simpledialog

contacts = {}
time_steps = []
contact_count = []

def add_contact(name, number):
    contacts[name] = number

def delete_contact(name):
    if name in contacts:
        del contacts[name]
    else:
        print("Contact not found.")

def find_contact(name):
    if name in contacts:
        print(f"{name}: {contacts[name]}")
    else:
        print("Contact not found.")

def list_contacts():
    for name, number in contacts.items():
        print(f"{name}: {number}")

def update_animation(frame):
    time_steps.append(frame)
    contact_count.append(len(contacts))
    ax.clear()
    ax.plot(time_steps, contact_count)
    ax.set_title("Contact Count Over Time")
    ax.set_xlabel("Time")
    ax.set_ylabel("Contact Count")

def on_add_contact():
    name = simpledialog.askstring("Input", "Enter the name of the contact:")
    number = simpledialog.askstring("Input", "Enter the phone number of the contact:")
    add_contact(name, number)
    print(f"Added {name} with phone number {number}.")

def on_delete_contact():
    name = simpledialog.askstring("Input", "Enter the name of the contact:")
    delete_contact(name)

def on_find_contact():
    name = simpledialog.askstring("Input", "Enter the name of the contact:")
    find_contact(name)

def on_list_contacts():
    list_contacts()

def on_exit():
    root.destroy()

fig, ax = plt.subplots()
fig.set_facecolor('white')  # Set background color for the figure
ax.set_facecolor('white')   # Set background color for the plot area
ani = FuncAnimation(fig, update_animation, frames=np.arange(0, 10), repeat=False)

root = tk.Tk()
root.title("Contact Management")

# Increase the font size and dimensions of the buttons
button_font = ('Arial', 16)
button_width = 20
button_height = 2

# Specify different background colors for each button
add_button = tk.Button(root, text="Add Contact", command=on_add_contact, font=button_font, width=button_width, height=button_height, bg='green')
add_button.pack()

delete_button = tk.Button(root, text="Delete Contact", command=on_delete_contact, font=button_font, width=button_width, height=button_height, bg='red')
delete_button.pack()

find_button = tk.Button(root, text="Find Contact", command=on_find_contact, font=button_font, width=button_width, height=button_height, bg='blue')
find_button.pack()

list_button = tk.Button(root, text="List Contacts", command=on_list_contacts, font=button_font, width=button_width, height=button_height, bg='yellow')
list_button.pack()

exit_button = tk.Button(root, text="Exit", command=on_exit, font=button_font, width=button_width, height=button_height, bg='gray')
exit_button.pack()

root.mainloop()
