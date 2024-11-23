import pandas as pd
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

def calculate_range(sample):
    # Розрахунок розмаху вибірки
    print("\nОбчислення розмаху вибірки:")
    min_val, max_val = min(sample), max(sample)
    range_value = max_val - min_val
    print(f"Мінімальне значення: {min_val}, Максимальне значення: {max_val}")
    print(f"Розмах: {range_value}")
    return range_value

def calculate_frequencies(sample):
    # Накопичувані частоти / Відносні частоти / Накопичувальні відносні частоти з поясненням
    print("\nОбчислення частот для кожного унікального значення вибірки:")
    sorted_sample = sorted(sample)
    frequencies = []
    total_count = len(sorted_sample)
    cum_freq = 0

    unique_sample_values = sorted(set(sorted_sample))

    for value in unique_sample_values:
        count = sorted_sample.count(value)
        cum_freq += count
        relative_freq = count / total_count
        accumulated_relative_freq = cum_freq / total_count
        
        # Виведення проміжних обчислень 
        print(f"\nЗначення вибірки: {value}")
        print(f"  -- Кількість повторень (частота): {count}")
        print(f"  -- Накопичена частота: {cum_freq}")
        print(f"  -- Відносна частота: {relative_freq:.4f} (обчислено як {count} / {total_count})")
        print(f"  -- Накопичена відносна частота: {accumulated_relative_freq:.4f} (обчислено як {cum_freq} / {total_count})")
        
        frequencies.append([value, count, cum_freq, relative_freq, accumulated_relative_freq])

    return frequencies

def main():
    # Запуск 
    pd.set_option('display.max_rows', None)  
    pd.set_option('display.max_columns', None)  
    pd.set_option('display.width', None) 
    pd.set_option('display.max_colwidth', None) 

    # Внесення вибірок
    A, B = entering_samples_A_B()

    # Складання вибірок в одну
    all_sample = A + B
    print(f"\nСкладена вибірка: {all_sample}")

    range_total = calculate_range(all_sample)
    print(f"\nРозмах вибірки R: {range_total}")

    # Обчислення частот для вибірки
    freq_table = calculate_frequencies(all_sample)

    # Виведення результатів
    df = pd.DataFrame(freq_table, columns=['Значення', 'Частота', 'Накопичена частота', 'Відносна частота', 'Накопичена відносна частота'])
    
    formatted_table = tabulate(df, headers='keys', tablefmt='grid', showindex=False)
    print("\nТаблиця частот для вибірки:")
    print(formatted_table)

if __name__ == "__main__":
    main()
