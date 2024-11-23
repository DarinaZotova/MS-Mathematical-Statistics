import numpy as np
from scipy import stats
from tabulate import tabulate

def entering_samples_A_B():
   # Внесення вибірки
   try:
       samples = list(map(float, input("Введіть вибірку (через кому): ").split(',')))
   except ValueError: # Перевірка даних та вірність, або рекурсія для спроби введення ще раз
       print("ERROR: Переконайтесь, що ввели лише числа (через кому)!!!.")
       return entering_samples_A_B()
   return samples


def confidence_interval_mean(sample, confidence=0.95):
   # Інтервальна оцінка для математичного сподівання
   n = len(sample)
   mean = np.mean(sample)
   std_dev = np.std(sample, ddof=1)  # Виправлене середнє квадратичне відхилення
   t_value = stats.t.ppf((1 + confidence) / 2, df=n - 1)
   margin_of_error = t_value * (std_dev / np.sqrt(n))
   return mean - margin_of_error, mean + margin_of_error


def confidence_interval_std(sample, confidence=0.95):
   # Інтервальна оцінка для середньоквадратичного відхилення
   n = len(sample)
   variance = np.var(sample, ddof=1)
   chi2_lower = stats.chi2.ppf((1 - confidence) / 2, df=n - 1)
   chi2_upper = stats.chi2.ppf((1 + confidence) / 2, df=n - 1)
   std_lower = np.sqrt((n - 1) * variance / chi2_upper)
   std_upper = np.sqrt((n - 1) * variance / chi2_lower)
   return std_lower, std_upper


def normality_tests(sample):
  
   # Тест Шапіро-Вілка для нормальності розподілу
   shapiro_stat, shapiro_p_value = stats.shapiro(sample)
  
   # Тест Колмогорова-Смирнова для нормальності розподілу
   ks_stat, ks_p_value = stats.kstest(sample, 'norm', args=(np.mean(sample), np.std(sample, ddof=1)))

   shapiro_result = "Нормальний розподіл" if shapiro_p_value > 0.05 else "Не нормальний розподіл"
   ks_result = "Нормальний розподіл" if ks_p_value > 0.05 else "Не нормальний розподіл"
  
   return {
       "Shapiro-Wilk Test": (shapiro_stat, shapiro_p_value, shapiro_result),
       "Kolmogorov-Smirnov Test": (ks_stat, ks_p_value, ks_result)
   }

def main():
   sample = entering_samples_A_B()


   mean_ci_lower, mean_ci_upper = confidence_interval_mean(sample)
   std_ci_lower, std_ci_upper = confidence_interval_std(sample)
   normality_results = normality_tests(sample)


   results = [
       ["Математичне сподівання", mean_ci_lower, mean_ci_upper],
       ["Середньоквадратичне відхилення", std_ci_lower, std_ci_upper]
   ]
   results.append(["Тест Шапіро-Вілка", normality_results["Shapiro-Wilk Test"][2], f"p-value: {normality_results['Shapiro-Wilk Test'][1]}"])
   results.append(["Тест Колмогорова-Смирнова", normality_results["Kolmogorov-Smirnov Test"][2], f"p-value: {normality_results['Kolmogorov-Smirnov Test'][1]}"])
  
   headers = ["Параметр", "Результат", "p-value"]
   print(tabulate(results, headers=headers, tablefmt="fancy_grid"))


if __name__ == "__main__":
   main()
