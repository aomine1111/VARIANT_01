# Сборник примеров кода на Python

Этот репозиторий содержит коллекцию примеров реализации известных **алгоритмов** и **структур данных**, а также примеры использования различных **библиотек** и **фреймворков** на языке **Python**.\
Он создан в образовательных целях, чтобы продемонстрировать принципы работы и показать примеры использования кода.\
Каждый пример имеет свою реализацию в папке `src` и подробную документацию в папке `docs`.

## Структура репозитория

Репозиторий разделён на несколько категорий, каждая из которых содержит примеры.

### 1. Алгоритмы
- [Bubble Sort](docs/algorithms/bubble_sort.md) - простой алгоритм сортировки, который многократно проходит по списку, меняя местами соседние элементы.
- [Insertion Sort](docs/algorithms/insertion_sort.md) - алгоритм сортировки вставками, который постепенно строит отсортированный массив, вставляя каждый новый элемент в нужное место.
- [Selection Sort](docs/algorithms/selection_sort.md) - алгоритм сортировки выбором, который находит минимальный элемент в неотсортированной части массива и перемещает его в начало.
- [Merge Sort](docs/algorithms/merge_sort.md) - рекурсивный алгоритм сортировки, использующий стратегию «разделяй и властвуй», путем слияния отсортированных подмассивов.
- [Linear Search](docs/algorithms/linear_search.md) - простой алгоритм линейного поиска, последовательно перебирающий элементы массива для поиска заданного значения.
- [Binary Search](docs/algorithms/binary_search.md) - эффективный алгоритм поиска в отсортированном массиве, который делит область поиска пополам.
- [Euclidean Algorithm](docs/algorithms/euclidean.md) - алгоритм для нахождения наибольшего общего делителя двух чисел.
- [Fibonacci Sequence](docs/algorithms/fibonacci.md) - реализация алгоритма вычисления последовательности Фибоначчи с использованием рекурсии.
- [Breadth-First Search (BFS)](docs/algorithms/bfs.md) - алгоритм обхода графа в ширину, который исследует все смежные вершины перед переходом к следующему уровню.

*Замечание:* Ссылки в описании ведут на файлы с подробной документацией, где указан принцип работы и ссылка на исходный код.

## Как использовать этот код

Существует два способа для запуска и тестирования предоставленного кода:

1. **Полное клонирование репозитория:**  
   Клонируйте репозиторий на свой компьютер с помощью команды:
   ```bash
   git clone https://github.com/aomine1111/VARIANT_01.git
   ```
   После этого вы можете запускать каждый пример, находясь в директории `src`, и изменять код по своему усмотрению.
2. **Копирование необходимого кода:**<br>
    Если вам нужен только определённый алгоритм, скопируйте интересующий вас код из соответствующего файла в папке src и запустите его в вашем интерпретаторе Python.