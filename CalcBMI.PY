import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
import csv

def calculateBMI(weight, height):
    heightMeters = height / 100
    BMI = weight / (heightMeters ** 2)

    if BMI < 18.5:
        return "Underweight"
    elif BMI >= 18.5 and BMI < 25:
        return "Normal"
    elif BMI >= 25 and BMI < 30:
        return "Overweight"
    else:
        return "Obese"

def click_calculate_bmi():
    try:
        name = enter_name.get()
        age = int(enter_age.get())
        height = int(enter_height.get())
        weight = int(enter_weight.get())

        if age <= 0 or height <= 0 or weight <= 0:
            raise ValueError("Age, height, and weight are suppose to be positive numbers.")

        category_bmi = calculateBMI(weight, height)

        with open('bmi_data.csv', 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([name, age, height, weight, category_bmi])

        messagebox.showinfo("BMI Category", "Your BMI category is: " + category_bmi)

        enter_name.delete(0, tk.END)
        enter_age.delete(0, tk.END)
        enter_height.delete(0, tk.END)
        enter_weight.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def click_show_graph():
    various_categories = {'Underweight': 0, 'Normal': 0, 'Overweight': 0, 'Obese': 0}
    with open('bmi_data.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            category_bmi = row[4]
            if category_bmi in various_categories:
                various_categories[category_bmi] += 1

    labels = list(various_categories.keys())
    sizes = list(various_categories.values())
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90)
    ax.axis('equal')
    plt.show()

root = tk.Tk()
root.title("BMI Calculator")

# Example: tk.Label(root, text="Label Text").grid(row=0, column=0)
tk.Label(root, text="Name:").grid(row=0, column=0)
tk.Label(root, text="Age:").grid(row=1, column=0)
tk.Label(root, text="Height:").grid(row=2, column=0)
tk.Label(root, text="Weight:").grid(row=3, column=0)

enter_name = tk.Entry(root)
enter_age = tk.Entry(root)
enter_height = tk.Entry(root)
enter_weight = tk.Entry(root)

enter_name.grid(row=0, column=1)
enter_age.grid(row=1, column=1)
enter_height.grid(row=2, column=1)
enter_weight.grid(row=3, column=1)

btn_calculate = tk.Button(root, text="Calculate BMI", command=click_calculate_bmi)
btn_calculate.grid(row=4, column=0, columnspan=2, pady=10)

btn_show_graph = tk.Button(root, text="Show Graph", command=click_show_graph)
btn_show_graph.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
