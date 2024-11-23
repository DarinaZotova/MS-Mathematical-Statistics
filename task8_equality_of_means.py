import numpy as np
from scipy.stats import t as t_dist
from tabulate import tabulate
from colorama import Fore, Style

#-------Обчислення T (формула з методички)
def calculate_T(X, Y):
    n1, n2 = len(X), len(Y)  # Розміри вибірок
    m_X, m_Y = np.mean(X), np.mean(Y)  # Середні значення вибірок
    var_X, var_Y = np.var(X, ddof=1), np.var(Y, ddof=1)  # Незміщені дисперсії

    #-------Формули для чисельника та знаменника
    formula_numerator = m_X - m_Y
    pooled_dispersion = ((n1 - 1) * var_X + (n2 - 1) * var_Y) / (n1 + n2 - 2)
    formula_denominator = np.sqrt(pooled_dispersion * (1 / n1 + 1 / n2))

    t_stat = formula_numerator / formula_denominator if formula_denominator != 0 else 0

    return t_stat, pooled_dispersion, var_X, var_Y

def main():
    print("Перевірка гіпотези про рівність середніх значень двох вибірок.")

    try:
        X = list(map(float, input("Введіть вибірку X (через пробіл): ").split()))
        Y = list(map(float, input("Введіть вибірку Y (через пробіл): ").split()))
    except ValueError:
        print("Error: будь ласка, введіть вибірку через пробіл!")
        return

    #-------Обчислення T
    t_stat, pooled_dispersion, var_X, var_Y = calculate_T(X, Y)

    n1, n2 = len(X), len(Y)
    num_of_degrees_of_freedom = n1 + n2 - 2  #-------Число степенів свободи k = n1 + n2 − 2

    #-------Критичне значення t-критерію
    a = 0.05 
    t_critical = t_dist.ppf(1 - a / 2, num_of_degrees_of_freedom)

    #-------Формулювання гіпотез
    null_hypothesis = "H0: Середні значення вибірок рівні (μ1 = μ2)."
    alternative_hypothesis = "H1: Середні значення вибірок відрізняються (μ1 ≠ μ2)."

    print("\nФормулювання гіпотез:")
    print(f"- {null_hypothesis}")
    print(f"- {alternative_hypothesis}")

    #-------Перевірка дисперсій (рівні або ні)
    f_statistic = var_X / var_Y if var_X > var_Y else var_Y / var_X
    f_critical = t_dist.ppf(1 - a / 2, num_of_degrees_of_freedom)

    if f_statistic < f_critical:
        dispersion_message = f"{Fore.GREEN}Дисперсії рівні.{Style.RESET_ALL}"
        alternative_dispersion_message = "Дисперсії нерівні."
    else:
        dispersion_message = "Дисперсії рівні."
        alternative_dispersion_message = f"{Fore.RED}Дисперсії нерівні.{Style.RESET_ALL}"

    print(f"\n{dispersion_message}")
    print(f"{alternative_dispersion_message}")

    #-------Підготовка даних для таблиці
    table_data = [
        ["Розмір вибірки X", n1],
        ["Розмір вибірки Y", n2],
        ["Середнє X", f"{np.mean(X):.2f}"],
        ["Середнє Y", f"{np.mean(Y):.2f}"],
        ["Дисперсія X", f"{var_X:.2f}"],
        ["Дисперсія Y", f"{var_Y:.2f}"],
        ["Об'єднана дисперсія", f"{pooled_dispersion:.2f}"],
        ["Число ступенів свободи", num_of_degrees_of_freedom],
        ["T", f"{t_stat:.4f}"],
        [f"Критичне значення t ({a})", f"{t_critical:.3f}"]
    ]

    print("\nРезультати у вигляді таблиці:")
    print(tabulate(table_data, headers=["Параметр", "Значення"], tablefmt="grid"))

    #-------Кольоровий висновок для середніх
    if abs(t_stat) > t_critical:
        result = f"{Fore.RED}Нульову гіпотезу H0 відхилено: середні значення вибірок відрізняються.{Style.RESET_ALL}"
    else:
        result = f"{Fore.GREEN}Немає підстав відхиляти нульову гіпотезу H0: середні значення вибірок рівні.{Style.RESET_ALL}"

    print(f"\n{result}")

if __name__ == "__main__":
    main()
