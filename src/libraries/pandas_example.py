import pandas as pd

def example_dataframe_creation():
    """
    Пример создания DataFrame:
    - Создание DataFrame из словаря
    - Указание порядка столбцов
    """
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [25, 30, 35, 28],
        'Salary': [50000, 60000, 70000, 65000]
    }
    df = pd.DataFrame(data, columns=['Name', 'Age', 'Salary'])
    print("Исходный DataFrame:")
    print(df)
    print("-" * 40)

def example_data_filtering():
    """
    Пример фильтрации DataFrame:
    - Фильтрация по условию (Age > 28)
    - Сортировка по столбцу Salary
    """
    data = {
        'Name': ['Alice', 'Bob', 'Charlie', 'Diana'],
        'Age': [25, 30, 35, 28],
        'Salary': [50000, 60000, 70000, 65000]
    }
    df = pd.DataFrame(data)
    filtered_df = df[df['Age'] > 28].sort_values(by='Salary', ascending=False)
    print("Отфильтрованный и отсортированный DataFrame (Age > 28):")
    print(filtered_df)
    print("-" * 40)

def example_grouping_and_aggregation():
    """
    Пример группировки и агрегации:
    - Создание DataFrame с данными по отделам
    - Группировка по отделу и вычисление среднего значения по Salary
    """
    data = {
        'Employee': ['Alice', 'Bob', 'Charlie', 'Diana', 'Evan', 'Fiona'],
        'Department': ['Sales', 'IT', 'Sales', 'HR', 'IT', 'HR'],
        'Salary': [50000, 70000, 52000, 60000, 72000, 61000]
    }
    df = pd.DataFrame(data)
    grouped_df = df.groupby('Department').agg({'Salary': 'mean'}).reset_index()
    print("Среднее значение Salary по отделам:")
    print(grouped_df)
    print("-" * 40)

if __name__ == '__main__':
    print("=== Примеры работы с Pandas ===\n")
    example_dataframe_creation()
    example_data_filtering()
    example_grouping_and_aggregation()
