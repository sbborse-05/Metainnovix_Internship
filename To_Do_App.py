import tkinter as tk
from tkinter import ttk, messagebox
import os

# File to store tasks
TASKS_FILE = "tasks.txt"

# Function to load tasks from file
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, "r") as file:
            for task in file.readlines():
                task_list.insert(tk.END, task.strip())

# Function to add task
def add_task():
    task = task_entry.get()
    if task:
        task_list.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Function to remove selected task
def remove_task():
    try:
        selected_task = task_list.curselection()[0]
        task_list.delete(selected_task)
    except IndexError:
        messagebox.showwarning("Warning", "No task selected!")

# Function to save tasks to file
def save_tasks():
    with open(TASKS_FILE, "w") as file:
        for task in task_list.get(0, tk.END):
            file.write(task + "\n")
    messagebox.showinfo("Saved", "Tasks saved successfully!")

# Hover effect for buttons
def on_enter(e):
    e.widget.config(bg="#27AE60", fg="white")

def on_leave(e):
    e.widget.config(bg="#2ECC71", fg="black")

# GUI Setup
root = tk.Tk()
root.title("To-Do List ✔")
root.geometry("420x580")
root.configure(bg="#1C1C1C")  # Dark Background

# Custom Styling
HEADER_FONT = ("Arial", 20, "bold")
BUTTON_FONT = ("Arial", 12, "bold")
ENTRY_FONT = ("Arial", 14)
LIST_FONT = ("Arial", 12)

# Header Label
header_label = tk.Label(root, text="📝 To-Do List", font=HEADER_FONT, bg="#1C1C1C", fg="white")
header_label.pack(pady=10)

# Task Entry
task_entry = tk.Entry(root, width=40, font=ENTRY_FONT, bg="#34495E", fg="white", insertbackground="white", bd=2, relief="flat")
task_entry.pack(pady=5)

# Buttons Frame
btn_frame = tk.Frame(root, bg="#1C1C1C")
btn_frame.pack(pady=5)

# Add Button
add_button = tk.Button(btn_frame, text="➕ Add Task", font=BUTTON_FONT, bg="#2ECC71", fg="black", width=12, bd=0, relief="flat", cursor="hand2", command=add_task)
add_button.grid(row=0, column=0, padx=5)
add_button.bind("<Enter>", on_enter)
add_button.bind("<Leave>", on_leave)

# Remove Button
remove_button = tk.Button(btn_frame, text="❌ Remove Task", font=BUTTON_FONT, bg="#E74C3C", fg="black", width=12, bd=0, relief="flat", cursor="hand2", command=remove_task)
remove_button.grid(row=0, column=1, padx=5)

# Save Button
save_button = tk.Button(root, text="💾 Save Tasks", font=BUTTON_FONT, bg="#F1C40F", fg="black", width=25, bd=0, relief="flat", cursor="hand2", command=save_tasks)
save_button.pack(pady=5)

# Task List with Scrollbar
frame = tk.Frame(root, bg="#1C1C1C")
frame.pack(pady=10)

task_list = tk.Listbox(frame, width=45, height=15, font=LIST_FONT, bg="#34495E", fg="white", selectbackground="#2980B9", bd=0, relief="flat")
task_list.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = ttk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
task_list.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=task_list.yview)

# Load existing tasks
load_tasks()

# Run the app
root.mainloop()
