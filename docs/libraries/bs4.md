# BeautifulSoup

[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) — это популярная библиотека для парсинга HTML и XML в Python. Она используется для извлечения данных из веб-страниц, поиска элементов по тегам и атрибутам, а также навигации по DOM-структуре документа.

---

## Установка

Установить библиотеку можно через pip:

```bash
pip install beautifulsoup4
```

Либо с помощью Anaconda:

```bash
conda install beautifulsoup4
```

---

## Примеры использования

Файл [bs4_example.py](../../src/libraries/bs4_example.py) содержит несколько практических сценариев применения библиотеки.

---

### 1. Разбор HTML-документа и извлечение текста

```python
from bs4 import BeautifulSoup

html_doc = """
<html>
    <head>
        <title>Пример страницы</title>
    </head>
    <body>
        <p class="content">Это пример контента на странице.</p>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

title = soup.title.string
paragraph = soup.find('p', class_='content').get_text()

print("Заголовок страницы:", title) # Пример страницы
print("Содержимое параграфа:", paragraph) # Это пример контента на странице.
```

**Что делает:**
- Парсит HTML-строку.
- Извлекает заголовок страницы (`<title>`) и текст параграфа (`<p>` с классом `content`).

**Методы:**
- `BeautifulSoup(html_doc, 'html.parser')` — создание объекта парсера.
- `soup.title.string` — получение текста заголовка.
- `soup.find('p', class_='content').get_text()` — поиск и извлечение текста из конкретного тега.

---

### 2. Извлечение всех ссылок с HTML-страницы

```python
from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <a href="https://example.com/page1">Страница 1</a>
        <a href="https://example.com/page2">Страница 2</a>
        <a href="https://example.com/page3">Страница 3</a>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

links = [a['href'] for a in soup.find_all('a', href=True)]

print("Найденные ссылки:")
for link in links:
    print(link)
    
# https://example.com/page1
# https://example.com/page2
# https://example.com/page3
```

**Что делает:**
- Находит все теги `<a>` с атрибутом `href`.
- Извлекает и выводит URL.

**Методы:**
- `soup.find_all('a', href=True)` — поиск всех ссылок.
- `a['href']` — извлечение значения атрибута `href`.

---

### 3. Поиск всех определённых тегов

```python
from bs4 import BeautifulSoup

html_doc = """
<html>
    <body>
        <div>Первый блок</div>
        <div>Второй блок</div>
        <p>Некоторый текст</p>
        <div>Третий блок</div>
    </body>
</html>
"""

soup = BeautifulSoup(html_doc, 'html.parser')

divs = soup.find_all('div')

print("Найденные теги <div>:")
for d in divs:
    print(d.get_text())

# Первый блок
# Второй блок
# Третий блок

```

**Что делает:**
- Извлекает все теги `<div>` из HTML-документа.
- Выводит содержимое каждого блока.

**Методы:**
- `soup.find_all('div')` — поиск всех `<div>` тегов.
- `get_text()` — извлечение внутреннего текста.

---

## Как запустить примеры

```bash
py src/libraries/bs4_example.py
```

---

## Исходный код
Доступен в файле [/src/libraries/bs4_example.py](../../src/libraries/bs4_example.py)
