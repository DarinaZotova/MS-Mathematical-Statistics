import numpy as np
import scipy.stats as stats
import matplotlib.pyplot as plt

#------Обчислення вибіркових характеристик: середнє та стандартне відхилення
def calculate_sample_stat(data, bins):
    midpoints = np.mean(bins, axis=1)
    data = np.array(data)
    total_frequency = data.sum()  # Загальна кількість спостережень
    
    # Обчислюємо середнє значення та дисперсію за допомогою векторизованих операцій
    sample_mean = np.sum(data * midpoints) / total_frequency
    sample_var = np.sum(data * (midpoints - sample_mean) ** 2) / (total_frequency - 1)
    
    # Стандартне відхилення
    sample_std_deviation = np.sqrt(sample_var)
    
    return sample_mean, sample_std_deviation

#------Обчислення теоретичних частот для кожного інтервалу, припускаючи нормальний розподіл
def theoretical(bins, sample_mean, sample_std_deviation, total_frequency):
    # Для кожного інтервалу (нижня та верхня межі)
    return [
        total_frequency * (stats.norm.cdf(upper, loc=sample_mean, scale=sample_std_deviation) - 
                           stats.norm.cdf(lower, loc=sample_mean, scale=sample_std_deviation))
        for lower, upper in bins
    ]

 #-------Обчислення статистики критерію Пірсона
def pearson_chi_squared_test(observed_freq, expected_freq):
    return sum((o - e) ** 2 / e for o, e in zip(observed_freq, expected_freq) if e > 0)
    
#-------Перевірка гістограми + гіпотиза
def check_histogram(frequencies, intervals):
    midpoints = [(interval[0] + interval[1]) / 2 for interval in intervals]
    if frequencies[0] > frequencies[-1]:
        return "H1: Розподіл не є нормальним."
    else:
        return "H0: Розподіл є нормальним."

#-------Перевірки мінімальної кількості спостережень в інтервалах
def check_minimum_frequencies(frequencies):
    return all(f >= 4 for f in frequencies)
    
#---------------------------------------------------------------------------
def main():
    intervals = [(440, 452), (452, 464), (464, 476), (476, 488), (488, 500),
                 (500, 512), (512, 524), (524, 536), (536, 548), (548, 560)]
    frequencies = [24, 18, 16, 14, 12, 10, 8, 6, 4, 4]  #-------Частоти
    alpha = 0.05  #------пунтк 1: Рівень значущості 

    #-------пункт 2: Розрахунок статистичних характеристик
    sample_mean, sample_std = calculate_sample_stat(frequencies, intervals)

    #-------пункт 4: Обчислення теоретичних частот
    n_total = sum(frequencies)
    expected_frequencies = theoretical(intervals, sample_mean, sample_std, n_total)

    #------пункт 5: Обчислення критерію Пірсона
    chi_square = pearson_chi_squared_test(frequencies, expected_frequencies)

    #-------пункт 6: Ступені свободи
    degrees_of_freedom = len(intervals) - 3  # Степінь свободи

    #------пункт 7: Критичне значення для заданого рівня значущості
    critical_value = round(stats.chi2.ppf(1 - alpha, degrees_of_freedom), 1) #critical_value = stats.chi2.ppf(1 - alpha, degrees_of_freedom)

    #------пункт 8: Висновок: порівняння X^2сп з X^2кр
    print("Результати:")
    print(f"Вибіркове середнє: {sample_mean:.2f}")
    print(f"Вибіркове стандартне відхилення: {sample_std:.2f}")
    print(f"Спостережене значення χ²сп \u03c7\u00b2: {chi_square:.2f}")
    print(f"Критичне значення χ²кр \u03c7\u00b2: {critical_value:.1f}") #print(f"Критичне значення X^2кр \u03c7\u00b2: {critical_value:.2f}")
    if chi_square < critical_value:
        print("Немає підстав відхилити нульову гіпотезу (H\u2080): розподіл нормальний χ²сп < χ²кр.")
    else:
        print("Нульову гіпотезу (H\u2080) треба відхилити: розподіл не є нормальним χ²сп > χ²кр.")

    #-------Перевірка гістограми для гіпотези
    histogram_hypothesis = check_histogram(frequencies, intervals)
    print(histogram_hypothesis)

    #-----пункт 2_2: Гістограмма
    midpoints = [(interval[0] + interval[1]) / 2 for interval in intervals]
    plt.bar(midpoints, frequencies, width=8, alpha=0.6, color='#2B3144', label="Спостережені частоти")
    plt.plot(midpoints, expected_frequencies, 'o-', color='#8E414E', label="Теоретичні частоти")
    plt.title("Гістограма частот та теоретичний розподіл")
    plt.xlabel("Кількість опадів (мм)")
    plt.ylabel("Частота")
    plt.xticks(midpoints) 
    plt.legend()
    plt.show()

if __name__ == "__main__":
    main()
