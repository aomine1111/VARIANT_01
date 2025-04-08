def fibonacci(n):
    """
    Функция вычисления n-го числа Фибоначчи.
    """
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == '__main__':
    num_terms = 10
    print(f"Последовательность Фибоначчи до {num_terms}-го числа:")
    for i in range(num_terms):
        print(f"Число Фибоначчи {i}: {fibonacci(i)}")
