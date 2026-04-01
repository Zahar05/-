# 1. Самостоятельно напишите следующие функции для практики
# алгоритмов: *Поиск N-го числа Фибоначчи, **Поиск N-го простого
# числа* и *Поиск факториала*.
# Запустите данные функции последовательно в одном процессе, а
# потом - каждую в отдельном процессе. С помощью библиотеки time
# замерьте и сравните время выполнения последовательного и
# параллельного выполнения программы.

import multiprocessing
import time
import math


def fibonacci(n):
    """Вычисление N-го числа Фибоначчи"""
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def get_prime(n):
    """Поиск N-го простого числа"""
    count = 0
    num = 2
    while True:
        is_prime = True
        # Оптимизация: проверяем только до корня из num
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            if count == n:
                return num
        num += 1


def task_fibonacci():
    """Вычисление Фибоначчи с замером времени"""
    start_time = time.time()
    n = 300000
    result = fibonacci(n)
    duration = time.time() - start_time

    # Не преобразуем число в строку, чтобы избежать ошибки
    # Просто выводим время выполнения
    print(f"Фибоначчи({n}) — вычислено за {duration:.4f} сек.")
    return result


def task_prime():
    """Поиск простого числа с замером времени"""
    start_time = time.time()
    n = 15000
    result = get_prime(n)
    duration = time.time() - start_time
    print(f"{n}-е простое число = {result} — выполнено за {duration:.4f} сек.")
    return result


def task_factorial():
    """Вычисление факториала с замером времени"""
    start_time = time.time()
    n = 100000
    result = math.factorial(n)
    duration = time.time() - start_time

    # Не преобразуем число в строку, чтобы избежать ошибки
    print(f"{n}! — вычислено за {duration:.4f} сек.")
    return result


def sequential_run():
    """Последовательное выполнение всех задач"""
    start = time.time()
    print("=" * 50)
    print("Последовательное выполнение:")

    task_fibonacci()
    task_prime()
    task_factorial()

    total_time = time.time() - start
    print(f"\nОбщее время последовательного выполнения: {total_time:.4f} сек")
    print("=" * 50 + "\n")


def parallel_run():
    """Параллельное выполнение всех задач"""
    start = time.time()
    print("=" * 50)
    print("Параллельное выполнение:")

    # Создаем процессы
    p1 = multiprocessing.Process(target=task_fibonacci)
    p2 = multiprocessing.Process(target=task_prime)
    p3 = multiprocessing.Process(target=task_factorial)

    # Запускаем процессы
    p1.start()
    p2.start()
    p3.start()

    # Ждем завершения
    p1.join()
    p2.join()
    p3.join()

    total_time = time.time() - start
    print(f"\nОбщее время параллельного выполнения: {total_time:.4f} сек")
    print("=" * 50 + "\n")


if __name__ == '__main__':
    sequential_run()
    parallel_run()
