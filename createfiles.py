import tkinter as tk
from tkinter import messagebox
import json
import os

def create_json_files(filenames, create_vehicles):
    filenames = [filename.strip() for filename in filenames.split(',')]
    
    for filename in filenames:
        if not filename.endswith('.json'):
            filename += '.json'

        try:
            with open('_DEFAULT.json', 'r') as file:
                data = json.load(file)
        except (json.JSONDecodeError, FileNotFoundError):
            messagebox.showerror("Error", "Invalid or missing _DEFAULT.json")
            return

        with open(filename, 'w') as file:
            json.dump(data, file, indent=4)

    if create_vehicles:
        file_names = [f for f in os.listdir('.') if os.path.isfile(f)]
        file_names = [f for f in file_names if f not in ['test.py', '_VEHICLES.json']]
        file_names = [os.path.splitext(f)[0] for f in file_names if f.endswith('.json')]
        with open('_VEHICLES.json', 'w') as f:
            json.dump(file_names, f, indent=4)

def submit():
    filenames = filename_entry.get()
    create_vehicles = var.get()
    if not filenames:
        messagebox.showerror("Error", "Filename cannot be empty")
        return
    create_json_files(filenames, create_vehicles)
    messagebox.showinfo("Success", "Files created successfully. Built by harv._ on Discord.")

root = tk.Tk()

root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)

tk.Label(root, text="Filenames (comma separated)").grid(row=0, sticky='ew')
filename_entry = tk.Entry(root)
filename_entry.grid(row=0, column=1, sticky='ew')

var = tk.IntVar()
tk.Checkbutton(root, text="Create vehicles.json", variable=var).grid(row=1, columnspan=2, sticky='ew')

tk.Button(root, text="Submit", command=submit).grid(row=2, columnspan=2, sticky='ew')

root.mainloop()