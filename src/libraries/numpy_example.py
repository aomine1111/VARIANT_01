import numpy as np

def example_array_manipulation():
    """
    Пример комплексной работы с массивами NumPy:
    - Создание массива с помощью np.arange
    - Изменение формы массива с np.reshape
    - Элементные операции и арифметика с broadcasting
    - Вычисление средних значений по строкам и столбцам с np.mean
    """
    # Создание одномерного массива из 12 последовательных чисел
    arr = np.arange(12)
    print("Исходный 1D массив:", arr)

    # Изменение формы в матрицу 3x4
    arr2 = arr.reshape(3, 4)
    print("\nМассив 3x4:\n", arr2)

    # Вычисление среднего значения по строкам и столбцам
    row_mean = np.mean(arr2, axis=1)
    col_mean = np.mean(arr2, axis=0)
    print("\nСреднее по строкам:", row_mean)
    print("Среднее по столбцам:", col_mean)

    # Применение арифметических операций с broadcasting
    arr2_doubled = arr2 * 2
    print("\nМассив, умноженный на 2:\n", arr2_doubled)
    print("-" * 40)


def example_linear_algebra():
    """
    Пример использования методов линейной алгебры в NumPy:
    - Создание квадратной матрицы
    - Вычисление детерминанта с np.linalg.det
    - Вычисление обратной матрицы с np.linalg.inv
    - Нахождение собственных значений и собственных векторов с np.linalg.eig
    """
    # Создаем квадратную матрицу
    A = np.array([[4, 2], [3, 1]])
    print("Матрица A:\n", A)

    # Вычисляем детерминант матрицы A
    det_A = np.linalg.det(A)
    print("\nДетерминант A:", det_A)

    # Вычисляем обратную матрицу (если она существует)
    try:
        inv_A = np.linalg.inv(A)
        print("\nОбратная матрица A:\n", inv_A)
    except np.linalg.LinAlgError:
        print("\nМатрица A необратима")

    # Нахождение собственных значений и собственных векторов
    eigenvalues, eigenvectors = np.linalg.eig(A)
    print("\nСобственные значения A:", eigenvalues)
    print("Собственные векторы A:\n", eigenvectors)
    print("-" * 40)


def example_random_statistics():
    """
    Пример генерации случайных данных и вычисления статистических параметров:
    - Генерация массива случайных чисел с np.random.randn
    - Вычисление среднего, медианы и стандартного отклонения с np.mean, np.median, np.std
    """
    # Генерация массива из 1000 случайных чисел (нормальное распределение)
    data = np.random.randn(1000)

    # Вычисление статистических параметров
    mean_value = np.mean(data)
    median_value = np.median(data)
    std_dev = np.std(data)

    print("Статистика для случайных данных:")
    print("Среднее:", mean_value)
    print("Медиана:", median_value)
    print("Стандартное отклонение:", std_dev)
    print("-" * 40)


if __name__ == '__main__':
    print("=== Примеры работы с NumPy ===\n")
    example_array_manipulation()
    example_linear_algebra()
    example_random_statistics()
