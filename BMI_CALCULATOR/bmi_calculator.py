import tkinter as tk
from tkinter import messagebox
import csv
import os
import matplotlib.pyplot as plt
import numpy as np

def calculate_bmi(weight, height):
    try:
        weight = float(weight)
        height = float(height) / 100
        bmi = weight / (height ** 2)
        return round(bmi, 2)
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter valid numerical values for weight and height.")
        return None
    
def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obesity"

def save_data(username, weight, height, bmi, category):
    file_exists = os.path.isfile('bmi_data.csv')
    with open('bmi_data.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Username", "Weight (kg)", "Height (cm)", "BMI", "Category"])
        writer.writerow([username, weight, height, bmi, category])

def show_history():
    if not os.path.isfile('bmi_data.csv'):
        messagebox.showinfo("No Data", "No historical data found.")
        return
    
    data = {}
    with open('bmi_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Username'] not in data:
                data[row['Username']] = []
            data[row['Username']].append((row['Weight (kg)'], row['Height (cm)'], row['BMI'], row['Category']))
    
    history_window = tk.Toplevel(root)
    history_window.title("BMI History")
    history_window.configure(bg="#f0f8ff")
    
    for username, records in data.items():
        tk.Label(history_window, text=f"User: {username}", font=('Lucida', 12, 'bold'), bg="#f0f8ff").pack()
        for record in records:
            tk.Label(history_window, text=f"Weight: {record[0]} kg, Height: {record[1]} cm, BMI: {record[2]}, Category: {record[3]}", bg="#f0f8ff", font=('Lucida', 10)).pack()

def plot_data():
    if not os.path.isfile('bmi_data.csv'):
        messagebox.showinfo("No Data", "No historical data found.")
        return
    
    data = {}
    with open('bmi_data.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Username'] not in data:
                data[row['Username']] = []
            data[row['Username']].append(float(row['BMI']))
    
    colors = plt.cm.viridis(np.linspace(0, 1, len(data)))
    for (username, bmi_values), color in zip(data.items(), colors):
        plt.plot(bmi_values, label=username, color=color)
    
    plt.xlabel('Record')
    plt.ylabel('BMI')
    plt.title('BMI Trends')
    plt.legend()
    plt.grid(True)
    plt.show()

def calculate():
    username = entry_username.get()
    weight = entry_weight.get()
    height = entry_height.get()
    
    if not username or not weight or not height:
        messagebox.showerror("Input Error", "Please fill in all fields.")
        return
    
    bmi = calculate_bmi(weight, height)
    if bmi is not None:
        category = classify_bmi(bmi)
        result_label.config(text=f"BMI: {bmi}, Category: {category}")
        save_data(username, weight, height, bmi, category)

root = tk.Tk()
root.title("BMI Calculator")
root.configure(bg="#e6f7ff")
title_label = tk.Label(root, text="BMI Calculator", font=("Lucida", 20, "bold"), bg="#e6f7ff", fg="#005b96")
title_label.grid(row=0, column=0, columnspan=2, pady=20)
tk.Label(root, text="Username:", bg="#e6f7ff", fg="#005b96", font=("Lucida", 12)).grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_username = tk.Entry(root, font=("Lucida", 12))
entry_username.grid(row=1, column=1, padx=10, pady=5)
tk.Label(root, text="Weight (kg):", bg="#e6f7ff", fg="#005b96", font=("Lucida", 12)).grid(row=2, column=0, padx=10, pady=5, sticky="e")
entry_weight = tk.Entry(root, font=("Lucida", 12))
entry_weight.grid(row=2, column=1, padx=10, pady=5)
tk.Label(root, text="Height (cm):", bg="#e6f7ff", fg="#005b96", font=("Lucida", 12)).grid(row=3, column=0, padx=10, pady=5, sticky="e")
entry_height = tk.Entry(root, font=("Lucida", 12))
entry_height.grid(row=3, column=1, padx=10, pady=5)
calculate_button = tk.Button(root, text="Calculate BMI", command=calculate, bg="#3399ff", fg="white", font=("Lucida", 12, "bold"))
calculate_button.grid(row=4, column=0, columnspan=2, pady=20)
result_label = tk.Label(root, text="", bg="#e6f7ff", font=("Lucida", 14, "bold"))# Result label
result_label.grid(row=5, column=0, columnspan=2, pady=20)
history_button = tk.Button(root, text="Show History", command=show_history, bg="#3399ff", fg="white", font=("Lucida", 12, "bold"))
history_button.grid(row=6, column=0, columnspan=2, pady=10)
plot_button = tk.Button(root, text="Plot Data", command=plot_data, bg="#3399ff", fg="white", font=("Lucida", 12, "bold"))
plot_button.grid(row=7, column=0, columnspan=2, pady=10)

root.mainloop()
