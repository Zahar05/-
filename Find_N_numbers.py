import multiprocessing
import time
import math

# Глобальные функции - оставляем без изменений

def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def get_prime(n):
    count = 0
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            count += 1
            if count == n:
                return num
        num += 1

def factorial_20():
    return math.factorial(20)

# Обертки для задач с измерением времени
def task_fibonacci():
    start_time = time.time()
    print("Вычисление Фибоначчи(35)...")
    result = fibonacci(35)
    duration = time.time() - start_time
    print(f"Фибоначчи(35) = {result} — выполнено за {duration:.4f} сек.")

def task_prime():
    start_time = time.time()
    print("Получение 35-го простого числа...")
    result = get_prime(35)
    duration = time.time() - start_time
    print(f"35-е простое число = {result} — выполнено за {duration:.4f} сек.")

def task_factorial():
    start_time = time.time()
    print("Вычисление 20!...")
    result = factorial_20()
    duration = time.time() - start_time
    print(f"20! = {result} — выполнено за {duration:.4f} сек.")

# Тяжелые задачи с измерением времени
def heavy_fibonacci():
    start_time = time.time()
    print("Heavy: Вычисление Фибоначчи(50)...")
    result = fibonacci(50)
    duration = time.time() - start_time
    print(f"Фибоначчи(50) = {result} — выполнено за {duration:.4f} сек.")

def heavy_prime():
    start_time = time.time()
    print("Heavy: Получение 100-го простого числа...")
    result = get_prime(100)
    duration = time.time() - start_time
    print(f"100-е простое число = {result} — выполнено за {duration:.4f} сек.")

def heavy_factorial():
    start_time = time.time()
    print("Heavy: Вычисление 25!...")
    result = math.factorial(25)
    duration = time.time() - start_time
    print(f"25! = {result} — выполнено за {duration:.4f} сек.")

# Тестовые функции
def sequential_run():
    start = time.time()
    print("Последовательное выполнение:")

    # Легкие задачи
    print("Вычисление 20!...")
    print(f"20! = {factorial_20()}")
    print("Вычисление Фибоначчи(35)...")
    print(f"Фибоначчи(35) = {fibonacci(35)}")
    print("Получение 35-го простого числа...")
    print(f"35-е простое число = {get_prime(35)}")

    # Тяжелые задачи
    print("\nТяжелые задачи:")
    print("Heavy: Вычисление Фибоначчи(50)...")
    print(f"Фибоначчи(50) = {fibonacci(50)}")
    print("Heavy: Получение 100-го простого числа...")
    print(f"100-е простое число = {get_prime(100)}")
    print("Heavy: Вычисление 25!...")
    print(f"25! = {math.factorial(25)}")
    print(f"Весь последовательный запуск занял {time.time() - start:.4f} сек\n")


def parallel_run():
    start = time.time()
    print("Параллельное выполнение:")

    # Создаем процессы для задач
    p1 = multiprocessing.Process(target=task_fibonacci)
    p2 = multiprocessing.Process(target=task_prime)
    p3 = multiprocessing.Process(target=task_factorial)

    p4 = multiprocessing.Process(target=heavy_fibonacci)
    p5 = multiprocessing.Process(target=heavy_prime)
    p6 = multiprocessing.Process(target=heavy_factorial)

    # Запускаем процессы
    p1.start()
    p2.start()
    p3.start()
    p4.start()
    p5.start()
    p6.start()

    # Ждем завершения всех процессов
    p1.join()
    p2.join()
    p3.join()
    p4.join()
    p5.join()
    p6.join()

    print(f"Весь параллельный запуск занял {time.time() - start:.4f} сек\n")

if __name__ == '__main__':
    multiprocessing.freeze_support()
    sequential_run()
    parallel_run()