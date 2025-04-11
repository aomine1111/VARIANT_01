# Pandas

[Pandas](https://pandas.pydata.org/) — это библиотека для анализа и обработки данных в Python. Она предоставляет структуры данных и функции высокого уровня для работы с таблицами (DataFrame) и временными рядами, а также удобные средства для импорта, фильтрации, группировки и агрегирования данных.

---

## Установка

Установить Pandas можно с помощью [pip](https://pip.pypa.io/) через команду:

```bash
pip install pandas
```

Либо же для Anaconda через команду:
```bash
conda install anaconda::pandas
```

---

## Примеры использования

В файле [pandas_example.py](../../src/libraries/pandas_example.py) находятся практические примеры работы с Pandas. Рассмотрим их по порядку:

---

### 1. Создание DataFrame и базовые операции

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 70000, 65000]
}
df = pd.DataFrame(data, columns=['Name', 'Age', 'Salary'])
print("Исходный DataFrame:")
print(df)
#       Name  Age  Salary
# 0    Alice   25   50000
# 1      Bob   30   60000
# 2  Charlie   35   70000
# 3    Diana   28   65000
```

**Что делает:**
- Создаёт DataFrame из словаря.
- Выводит получившийся DataFrame

**Методы:**
- `pd.DataFrame()` - создание табличной структуры.

---

### 2. Фильтрация данных

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
    'Age': [25, 30, 35, 28],
    'Salary': [50000, 60000, 70000, 65000]
}
df = pd.DataFrame(data)
filtered_df = df[df['Age'] > 28].sort_values(by='Salary', ascending=False)
print("Отфильтрованный и отсортированный DataFrame (Age > 28):")
print(filtered_df)
#       Name  Age  Salary
# 2  Charlie   35   70000
# 1      Bob   30   60000
```

**Что делает:**
- Создаёт DataFrame с зарплатой.
- Фильтрует людей, у которых возраст больше 28.

**Методы:**
- `df['Age'] > 28` - булева фильтрация.
- `sort_values(by='Salary', ascending=False)` - сортировка по зарплате.

---

### 3. Группировка и агрегирование

```python
import pandas as pd

data = {
    'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan', 'Fiona'],
    'Department': ['Sales', 'IT', 'Sales', 'HR', 'IT', 'HR'],
    'Salary': [50000, 70000, 52000, 60000, 72000, 61000]
}
df = pd.DataFrame(data)
grouped_df = df.groupby('Department').agg({'Salary': 'mean'}).reset_index()
print("Среднее значение Salary по отделам:")
print(grouped_df)
#   Department   Salary
# 0         HR  60500.0
# 1         IT  71000.0
# 2      Sales  51000.0
```

**Что делает:**
- Группирует данные по отделам и считает среднюю зарплату по отделам.

**Методы:**
- `groupby('Department')` - группировка по столбцу.
- `agg({'Salary': 'mean'})` - применение агрегирующей функции.

---

## Как запустить примеры

Выполните команду в репозитории:

```bash
py src/libraries/pandas_example.py
```

Это последовательно вызовет каждую из трех функций и выведет результаты в консоль.

---

## Исходный код
Исходный код доступен в файле [/src/libraries/pandas_example.py](../../src/libraries/pandas_example.py)


