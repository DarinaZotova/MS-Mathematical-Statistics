import numpy as np
from tabulate import tabulate

def entering_samples_A_B():
    # Внесення вибірок
    try:
        A = list(map(float, input("Введіть вибірку A (через кому): ").split(',')))
        B = list(map(float, input("Введіть вибірку Б (через кому): ").split(',')))
    except ValueError: # Перевірка даних та вірність, або рекурсія для спроби введення ще раз 
        print("ERROR: Переконайтесь, що ввели лише числа (через кому)!!!.")
        return entering_samples_A_B() 
    return A, B

def moment_method(sample):
    # Метод моментів
    sample_mean = np.mean(sample) 
    corrected_variance = np.var(sample, ddof=1)  # Виправлена вибіркова дисперсія (np.var – для розрахунку деспесії)
    return sample_mean, corrected_variance

def method_max_similarity(sample):
    # Метод найбільшої подібності
    sample_mean = np.mean(sample) 
    uncorrected_variance = np.var(sample, ddof=0) 
    return sample_mean, uncorrected_variance

def main():
    # Внесення вибірок
    A, B = entering_samples_A_B()

    moments_mean_A, moments_variance_A = moment_method(A)
    mom_mean_B, mom_var_B = moment_method(B)
    mle_mean_A, mle_var_A = method_max_similarity(A)
    mle_mean_B, mle_var_B = method_max_similarity(B)

    results = {
        "Метод моментів вибірки(A)": [moments_mean_A, moments_variance_A],
        "Метод моментів вибірки(B)": [mom_mean_B, mom_var_B],
        "Метод найбільщої подібності вибірки(A)": [mle_mean_A, mle_var_A],
        "Метод найбільшої подібності вибірки(B)": [mle_mean_B, mle_var_B]
    }

    headers = ["Метод", "Оцінка середнього", "Оцінка дисперсії"]
    table_data = [[key, *value] for key, value in results.items()]
    print(tabulate(table_data, headers=headers, tablefmt="fancy_grid"))

if __name__ == "__main__":
    main()
