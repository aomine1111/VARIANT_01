from bs4 import BeautifulSoup

def example_parse_html():
    """
    Пример разбора HTML-строки:
    - Парсинг HTML документа с помощью BeautifulSoup
    - Извлечение заголовка и текста из параграфа
    """
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
    print("Заголовок страницы:", title)
    print("Содержимое параграфа:", paragraph)
    print("-" * 40)

def example_extract_links():
    """
    Пример извлечения ссылок:
    - Парсинг HTML с несколькими ссылками
    - Извлечение всех URL из тегов <a>
    """
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
    print("-" * 40)

def example_find_all_tags():
    """
    Пример использования метода find_all:
    - Поиск всех тегов <div> и вывод их содержимого
    """
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
    print("-" * 40)

if __name__ == '__main__':
    print("=== Примеры работы с BeautifulSoup ===\n")
    example_parse_html()
    example_extract_links()
    example_find_all_tags()
