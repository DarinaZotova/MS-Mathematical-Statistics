import numpy as np
import pandas as pd
from scipy import stats
from prettytable import PrettyTable # Інший формат таблички

def entering_samples_A_B():
    # Внесення вибірок
    try:
        A = list(map(float, input("Введіть вибірку A (через кому): ").split(',')))
        B = list(map(float, input("Введіть вибірку Б (через кому): ").split(',')))
    except ValueError: # Перевірка даних та вірність, або рекурсія для спроби введення ще раз 
        print("ERROR: Переконайтесь, що ввели лише числа (через кому)!!!.")
        return entering_samples_A_B() 
    return A, B

def round_value(value, decimals=2):
    # Округлення значень 
    return round(value, decimals)

def calculate_statistics(sample):
    # Обчислення числових характеристик вибірки
    average = np.mean(sample)
    median = np.median(sample)
    
    # Перевірка моди
    mode_r = stats.mode(sample, keepdims=True)
    if len(mode_r.count) > 0 and mode_r.count[0] > 1:
        mode = mode_r.mode[0]
    else:
        mode = "Мода не визначена: всі елементи з'являються лише один раз"
    
    variance = np.var(sample, ddof=0)
    corrected_variance = np.var(sample, ddof=1)
    std_dev = np.sqrt(variance)
    corrected_std_dev = np.std(sample, ddof=1)
    coefficient_of_variation = std_dev / average * 100 if average != 0 else float('inf')
    
    # Центральні моменти 3-го та 4-го порядку
    central_moment_third = stats.moment(sample, moment=3)
    central_moment_fourth = stats.moment(sample, moment=4)
    
    # Асиметрія та ексцес
    asymmetry = stats.skew(sample)
    kurtosis = stats.kurtosis(sample)
    
    # Результати 
    stats_dict = {
        "Вибіркова Середня:": round_value(average),
        "Медіана:": round_value(median),
        "Мода:": mode,
        "Вибіркова Дисперсія:": round_value(variance),
        "Вибіркове Середнє Квадратичне Відхилення:": round_value(std_dev),
        "Коефіцієнт Варіації:": round_value(coefficient_of_variation),
        "Центральний Момент 3 Порядку:": round_value(central_moment_third),
        "Центральний Момент 4 Порядку:": round_value(central_moment_fourth),
        "Асиметрія:": round_value(asymmetry),
        "Ексцес:": round_value(kurtosis),
        "Виправлена Дисперсія:": round_value(corrected_variance),
        "Виправлене Середнє Квадратичне Відхилення: ": round_value(corrected_std_dev)
    }
    
    return stats_dict

# Щоб показуввало всі стовбці в таблиці повністю
pd.set_option('display.max_columns', None)

def print_statistics_table(stats_dict, sample_name):
    # Створення таблиці 
    output_table = PrettyTable()
    output_table.field_names = ["Математична Статистика", sample_name]
    
    for key, value in stats_dict.items():
        output_table.add_row([key, value])

    print(output_table)

def main():
    # Внесення вибірок
    A, B = entering_samples_A_B()

    # Обчислення статистик для вибірок A та B
    stats_A = calculate_statistics(A)
    stats_B = calculate_statistics(B)

    # Виведення результатів у вигляді таблиці з використанням PrettyTable
    print("\nХарактеристики Вибірки A:")
    print_statistics_table(stats_A, "A")
    
    print("\nХарактеристики Вибірки Б:")
    print_statistics_table(stats_B, "Б")

if __name__ == "__main__":
    main()
