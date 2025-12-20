import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

# Цільова функція
def objective_function(x):
    return 3 * x[0]**2 + 4 * x[1]**2

# Обмеження у вигляді штрафної функції
def penalty_function(x, r):
    constraint = x[1] - x[0]**2 - 2
    penalty = r * max(0, constraint)**2
    return objective_function(x) + penalty

# Метод штрафних функцій
def penalty_method(epsilon=0.01, r_initial=1, beta=10, max_iterations=100):
    # Стартова точка
    x0 = [-2.0, 0.75]
    r = r_initial
    iteration = 0
    history = []

    while iteration < max_iterations:
        # Мінімізуємо з урахуванням штрафної функції
        result = minimize(lambda x: penalty_function(x, r), x0, method='BFGS')
        x0 = result.x
        history.append((iteration, x0[0], x0[1], objective_function(x0)))

        # Перевірка умови зупинки
        constraint = x0[1] - x0[0]**2 - 2
        if abs(constraint) < epsilon:
            break

        # Збільшуємо штраф
        r *= beta
        iteration += 1

    return x0, iteration, history

# Виконання алгоритму
solution, iterations, history = penalty_method()

# Виведення результатів
print(f"Кількість ітерацій: {iterations}")
print(f"Наближене значення мінімуму: P* = ({solution[0]:.4f}, {solution[1]:.4f})")
print(f"Значення цільової функції у точці P*: {objective_function(solution):.4f}")

# Візуалізація
x_vals = [h[1] for h in history]
y_vals = [h[2] for h in history]

plt.figure()
plt.plot(x_vals, y_vals, marker='o', label="Ітерації")
plt.xlabel("x")
plt.ylabel("y")
plt.title("Процес мінімізації")
plt.legend()
plt.grid()
plt.show()
