import numpy as np
from scipy.stats import f
from prettytable import PrettyTable
from colorama import Fore, init

init(autoreset=True)

def entering_samples_X_Y(user_message):
    try:
        sample = list(map(float, input(user_message).split()))
        return sample if sample else entering_samples_X_Y("Вибірка не повинна бути порожня! Введіть вибірку ще раз: ")
    except ValueError:
        print("ERROR: Вибірка повинна містити лише числа, розділені пробілами!")
        return entering_samples_X_Y(user_message)

# Основна функція для перевірки гіпотези про рівність дисперсій двох нормально розподілених генеральних сукупностей.
def main():
    #-------пункт 1: Введення вибірок
    samples = {var: entering_samples_X_Y(f"Введіть вибірку {var} (через пробіл): ") for var in ["X", "Y"]}
    X, Y = samples["X"], samples["Y"]

    n1, n2 = len(X), len(Y)

    #-------пункт 2: Обчислення незміщених вибіркових дисперсій Sx^2 та Sy^2
    s_X_2 = np.var(X, ddof=1)
    s_Y_2 = np.var(Y, ddof=1)

    #-------пункт 3: Визначення більшої (sB^2) та меншої (sM^2) дисперсій
    s_B_2, s_M_2 = (s_X_2, s_Y_2) if s_X_2 > s_Y_2 else (s_Y_2, s_X_2)

    #-------пункт 4: Визначення ступенів вільності k1 та k2
    k1, k2 = (n1 - 1, n2 - 1) if s_B_2 == s_X_2 else (n2 - 1, n1 - 1)

    #-------пункт 5: Розрахунок обчисленого значення статистики Fдосл
    F_researched = s_B_2 / s_M_2

    #-------пункт 6: Обчислення критичного значення Fкр для рівня значущості α = 0.05
    a = 0.05
    F_critical = f.ppf(1 - a / 2, k1, k2)

    # Створення таблиці результатів
    table = PrettyTable()
    table.field_names = ["Параметр", "Значення"]
    table.add_row(["Вибірка X", f"{X}"])
    table.add_row(["Вибірка Y", f"{Y}"])
    table.add_row(["Обсяг вибірки n1", f"{n1}"])
    table.add_row(["Обсяг вибірки n2", f"{n2}"])
    table.add_row(["Незміщена дисперсія Sx^2", f"{s_X_2:.2f}"])
    table.add_row(["Незміщена дисперсія Sy^2", f"{s_Y_2:.2f}"])
    table.add_row(["Ступені вільності k1", f"{k1}"])
    table.add_row(["Ступені вільності k2", f"{k2}"])
    table.add_row(["Обчислене значення Fдосл", f"{F_researched:.2f}"])
    table.add_row([f"Критичне значення Fкр (α = {a})", f"{F_critical:.2f}"])

    #-------пункт 7: Перевірка гіпотези
    # Нульова гіпотеза H0: D(X) = D(Y), альтернативна H1: D(X) ≠ D(Y)
    result = "Відхиляємо нульову гіпотезу: дисперсії нерівні D(X) ≠ D(Y)." if F_researched > F_critical else "Немає підстав відхиляти нульову гіпотезу: дисперсії рівні D(X) = D(Y)."
    result_color = Fore.RED + result if F_researched > F_critical else Fore.GREEN + result
    table.add_row(["Висновок", result_color])

    # Виведення результатів
    print("\nРезультати перевірки гіпотези:")
    print(table)

if __name__ == "__main__":
    main()
