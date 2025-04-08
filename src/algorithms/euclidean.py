def euclidean_algorithm(a, b):
    """
    Функция нахождения наибольшего общего делителя (НОД) с помощью алгоритма Евклида.
    """
    while b:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    num1, num2 = 56, 98
    print(f"НОД ({num1}, {num2}) = {euclidean_algorithm(num1, num2)}")
