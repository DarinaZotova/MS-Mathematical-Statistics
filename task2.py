import numpy as np
import matplotlib.pyplot as plt

def entering_samples_A_B():
    # ФУНКЦІЯ внесення вибірок
    while True:
        try:
            A = list(map(float, input("Введіть вибірку A (через кому): ").split(',')))
            B = list(map(float, input("Введіть вибірку Б (через кому): ").split(',')))
            if not A or not B:
                raise ValueError("Вибірки НЕ повинні бути порожніми.")
            return A, B
        except ValueError as e:
            print(f"ERROR: {e}. Введіть вибірки ще раз.")

def empirical(sample):
    # Емпірична функція розподілення
    sorted_sample = np.sort(sample)
    n = len(sample)
    y = np.arange(1, n + 1) / n
    return sorted_sample, y

def print_empirical_distribution(sorted_sample, y):
    # Виведення емпіричної функції розподілення
    n = len(sorted_sample)
    print("Результат:")
    for i in range(n):
        print(f"x = {sorted_sample[i]:.2f}: n_x = {i+1}, F*(x) = {i+1}/{n} = {y[i]:.2f}")
    print("\nF*(x) = {")
    for i in range(n):
        if i == 0:
            print(f"  0, якщо x < {sorted_sample[0]:.2f},")
        elif i == n - 1:
            print(f"  1.00, якщо x ≥ {sorted_sample[i]:.2f}.")
        else:
            print(f"  {y[i]:.2f}, якщо {sorted_sample[i]:.2f} ≤ x < {sorted_sample[i+1]:.2f},")
    print("}")

def graphs_variation_series_polygon_histogram(A, B):
    # ФУНКЦІЯ побудови графіків варіаційного ряду / полігон / гістограма 
    plt.figure(figsize=(18, 8))

    # Полігон частот для вибірки A
    plt.subplot(2, 2, 1)
    freq_A, edges_A = np.histogram(A, bins='auto')
    midpoints_A = (edges_A[:-1] + edges_A[1:]) / 2
    plt.plot(midpoints_A, freq_A, marker='o', linestyle='-', color='#8E414E', label='Полігон A')
    plt.title("Полігон частот для вибірки A")
    plt.xlabel("Значення")
    plt.ylabel("Частота")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()

    # Полігон частот для вибірки Б
    plt.subplot(2, 2, 2)
    freq_B, edges_B = np.histogram(B, bins='auto')
    midpoints_B = (edges_B[:-1] + edges_B[1:]) / 2
    plt.plot(midpoints_B, freq_B, marker='o', linestyle='-', color='#2B3144', label='Полігон Б')
    plt.title("Полігон частот для вибірки Б")
    plt.xlabel("Значення")
    plt.ylabel("Частота")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()

    # Гістограма для вибірки A
    plt.subplot(2, 2, 3)
    plt.hist(A, bins=10, alpha=0.7, color='#8E414E', label='Гістограма A')
    plt.title("Гістограма вибірки A")
    plt.xlabel("Значення")
    plt.ylabel("Частота")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()

    # Гістограма для вибірки Б
    plt.subplot(2, 2, 4)
    plt.hist(B, bins=10, alpha=0.7, color='#2B3144', label='Гістограма Б')
    plt.title("Гістограма вибірки Б")
    plt.xlabel("Значення")
    plt.ylabel("Частота")
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.legend()

    # Відображення графіків
    plt.tight_layout()
    plt.show()

def graph_empirical_distribution_function(A, B):
    # ФУНКЦІЯ Побудови графіка емпіричної функції розподілення для вибірок
    sorted_A, y_A = empirical(A)
    sorted_B, y_B = empirical(B)

    # Виведення результату для вибірки A
    print("Емпірична функція розподілу для вибірки A:")
    print_empirical_distribution(sorted_A, y_A)

    # Виведення результату для вибірки Б
    print("\nЕмпірична функція розподілу для вибірки Б:")
    print_empirical_distribution(sorted_B, y_B)

    # Побудова графіків емпіричних функцій розподілення
    plt.figure(figsize=(10, 6))
    plt.plot(sorted_A, y_A, marker='o', linestyle='-', color='#8E414E', label='Емпірична функція A')
    plt.plot(sorted_B, y_B, marker='x', linestyle='-', color='#2B3144', label='Емпірична функція Б')
    plt.title("Емпірична функція розподілення для вибірок A і Б")
    plt.xlabel("Значення")
    plt.ylabel("Ймовірність")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Внесення вибірок
    A, B = entering_samples_A_B()

    # Побудова графіків для вибірок (A;Б)
    graphs_variation_series_polygon_histogram(A, B)

    # Побудова графіка емпіричної функції розподілення для вибірок (A;Б)
    graph_empirical_distribution_function(A, B)

if __name__ == "__main__":
    main()

'''1
import numpy as np
import matplotlib.pyplot as plt

def entering_samples_A_B():
    # ФУНКЦІЯ внесення вибірок
    while True:
        try:
            A = list(map(float, input("Введіть вибірку A (через кому): ").split(',')))
            B = list(map(float, input("Введіть вибірку Б (через кому): ").split(',')))
            if not A or not B:
                raise ValueError("Вибірки НЕ повинні бути порожніми.")
            return A, B
        except ValueError as e:
            print(f"ERROR: {e}. Введіть вибірки ще раз.")

def empirical(sample):
    # Емпірична функція розподілення
    sorted_sample = np.sort(sample)
    n = len(sample)
    y = np.arange(1, n + 1) / n
    return sorted_sample, y

def print_empirical_distribution(sorted_sample, y):
    # Виведення емпіричної функції розподілення
    n = len(sorted_sample)
    print("Результат:")
    for i in range(n):
        print(f"x = {sorted_sample[i]:.2f}: n_x = {i+1}, F*(x) = {i+1}/{n} = {y[i]:.2f}")
    print("\nF*(x) = {")
    for i in range(n):
        if i == 0:
            print(f"  0, якщо x < {sorted_sample[0]:.2f},")
        elif i == n - 1:
            print(f"  1.00, якщо x ≥ {sorted_sample[i]:.2f}.")
        else:
            print(f"  {y[i]:.2f}, якщо {sorted_sample[i]:.2f} ≤ x < {sorted_sample[i+1]:.2f},")
    print("}")

def graphs_variation_series_polygon_histogram(A, B):
    # ФУНКЦІЯ побудови графіків варіаційного ряду / полігон і гістограма 
    # ---------------------------------------
    # Побудова графіка для вибірки A
    plt.figure(figsize=(14, 6))

    # Варіаційний ряд для вибірки A (Полігон)
    plt.subplot(1, 2, 1)
    plt.plot(sorted(A), np.arange(1, len(A) + 1) / len(A), marker='o', linestyle='-', color='#F2C2C6', label='Полігон A')
    plt.title("Полігон варіаційного ряду для вибірки A")
    plt.xlabel("Значення")
    plt.ylabel("Емпірична ймовірність")
    plt.grid(True)

    # Гістограма для вибірки A
    plt.subplot(1, 2, 2)
    plt.hist(A, bins=10, density=True, alpha=0.6, color='#F2C2C6', label='Гістограма A')
    plt.title("Гістограма для вибірки A")
    plt.xlabel("Значення")
    plt.ylabel("Частота")
    plt.grid(True)

    # Відображення графіків
    plt.tight_layout()
    plt.show()
# ---------------------------------------
    # Побудова графіка для вибірки Б
    plt.figure(figsize=(14, 6))

    # Варіаційний ряд для вибірки Б (Полігон)
    plt.subplot(1, 2, 1)
    plt.plot(sorted(B), np.arange(1, len(B) + 1) / len(B), marker='o', linestyle='-', color='#A67676', label='Полігон Б')
    plt.title("Полігон варіаційного ряду для вибірки Б")
    plt.xlabel("Значення")
    plt.ylabel("Емпірична ймовірність")
    plt.grid(True)

    # Гістограма для вибірки Б
    plt.subplot(1, 2, 2)
    plt.hist(B, bins=10, density=True, alpha=0.6, color='#A67676', label='Гістограма Б')
    plt.title("Гістограма для вибірки Б")
    plt.xlabel("Значення")
    plt.ylabel("Частота")
    plt.grid(True)

    # Відображення графіків
    plt.tight_layout()
    plt.show()

def graph_empirical_distribution_function(A, B):
    # ФУНКЦІЯ Побудови графіка емпіричної функції розподілення для вибірок
    # Обчислення емпіричної функції розподілення
    sorted_A, y_A = empirical(A)
    sorted_B, y_B = empirical(B)

    # Виведення результату для вибірки A
    print("Емпірична функція розподілу для вибірки A:")
    print_empirical_distribution(sorted_A, y_A)

    # Виведення результату для вибірки Б
    print("\nЕмпірична функція розподілу для вибірки Б:")
    print_empirical_distribution(sorted_B, y_B)

    # Побудова графіків емпіричних функцій розподілення
    plt.figure(figsize=(10, 6))
    plt.plot(sorted_A, y_A, marker='o', linestyle='-', color='#F2C2C6', label='Емпірична функція A')
    plt.plot(sorted_B, y_B, marker='x', linestyle='-', color='#A67676', label='Емпірична функція Б')
    plt.title("Емпірична функція розподілення для вибірок (A;Б)")
    plt.xlabel("Значення")
    plt.ylabel("Ймовірність")
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    # Внесення вибірок
    A, B = entering_samples_A_B()

    # Побудова графіків для вибірок (A;Б)
    graphs_variation_series_polygon_histogram(A, B)

    # Побудова графіка емпіричної функції розподілення для вибірок (A;Б)
    graph_empirical_distribution_function(A, B)

if __name__ == "__main__":
    main()
'''