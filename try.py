from sympy import symbols, Eq, solve
import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import numpy as np

def solve_quadratic(a, b, c):
    x = symbols('x')
    equation = Eq(a * x**2 + b * x + c, 0)
    solutions = solve(equation, x)
    return solutions

def plot_quadratic(a, b, c):
    x = np.linspace(-10, 10, 400)
    # вычислением значения y для графика
    y = a * x**2 + b * x + c

    # очищаем график
    ax.clear()
    # Рисуем график
    ax.plot(x, y, label=f'{a}x² + {b}x + {c}')
    ax.axhline(0, color='black', linewidth=0.5)
    ax.axvline(0, color='black', linewidth=0.5)
    ax.set_title("График функции")
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.legend()
    # обновляем график
    canvas.draw()

def calculate():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        if (b**2 - 4*a*c) >= 0:
            solutions = solve_quadratic(a, b, c)
            # Обновление полей вывода решений
            solution1_var.set(solutions[0])
            solution2_var.set(solutions[1] if len(solutions) > 1 else '')
            no_real_solution_var.set('')
            plot_quadratic(a, b, c) # чертим график
        else:
            solution1_var.set('')
            solution2_var.set('')
            no_real_solution_var.set('Нет действительных корней')
    except ValueError:
        solution1_var.set('')
        solution2_var.set('')
        no_real_solution_var.set('Коэффициенты должны быть числами')

# Создание основного окна
root = tk.Tk()
root.title("Калькулятор квадратных уравнений")

# Увеличение размера окна
root.geometry("1000x410")

# Метки и поля ввода для коэффициентов
tk.Label(root, text="Коэффициент a:").grid(row=0, column=0, padx=10, pady=10)
entry_a = tk.Entry(root, width=40)
entry_a.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Коэффициент b:").grid(row=1, column=0, padx=10, pady=10)
entry_b = tk.Entry(root, width=40)
entry_b.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Коэффициент c:").grid(row=2, column=0, padx=10, pady=10)
entry_c = tk.Entry(root, width=40)
entry_c.grid(row=2, column=1, padx=10, pady=10)

# Кнопка для расчета
calculate_button = tk.Button(root, text="Рассчитать", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=20)

# Метки и поля вывода для решений
tk.Label(root, text="Решение 1:").grid(row=4, column=0, padx=10, pady=10)
solution1_var = tk.StringVar()
solution1_entry = tk.Entry(root, textvariable=solution1_var, state='readonly', width=40)
solution1_entry.grid(row=4, column=1, padx=10, pady=10)

tk.Label(root, text="Решение 2:").grid(row=5, column=0, padx=10, pady=10)
solution2_var = tk.StringVar()
solution2_entry = tk.Entry(root, textvariable=solution2_var, state='readonly', width=40)
solution2_entry.grid(row=5, column=1, padx=10, pady=10)

# Поле для вывода сообщения о недействительных корнях
tk.Label(root, text="Сообщение:").grid(row=6, column=0, padx=10, pady=10)
no_real_solution_var = tk.StringVar()
no_real_solution_entry = tk.Entry(root, textvariable=no_real_solution_var, state='readonly', width=40)
no_real_solution_entry.grid(row=6, column=1, padx=10, pady=10)

# Создание области для графика
fig = Figure(figsize=(5, 4), dpi=100)
ax = fig.add_subplot(111)
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.get_tk_widget().grid(row=0, column=2, rowspan=7, padx=10, pady=10)
root.iconbitmap(default="icon.ico")
root.mainloop()