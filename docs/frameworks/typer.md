# Typer

В данном документе описаны примеры кода для демонстрации возможностей библиотеки **Typer** для создания CLI-приложений. Typer позволяет создавать удобные в использовании консольные приложения с автогенерацией справки и поддержкой аннотаций типов.

**Исходный файл с примерами:**  
[typer_example.py](../../src/frameworks/typer_example.py)

**Запуск:**  
Для получения справки запустите приложение командой:  

```bash
py typer_example.py --help
```

---

## Структура примеров

### 1. Команда hello
Выводит приветственное сообщение в консоль.  

```python
@app.command()
def hello():
    typer.echo("Привет, мир!")
```

---

### 2. Команда add

Складывает два числа и выводит результат.

```python
@app.command()
def add(a: float, b: float):
    typer.echo(f"Результат сложения: {a + b}")
```

---

### 3. Команда repeat

Повторяет заданный текст указанное число раз.

```python
@app.command()
def repeat(text: str, count: int = 1):
    for _ in range(count):
        typer.echo(text)
```

---

### 4. Группа команд config

Группа команд для управления конфигурацией приложения. Содержит две подкоманды:
- `config show`: Выводит текущую конфигурацию.
- `config set`: Изменяет значение настройки.

```python
config_app = typer.Typer()

@config_app.command("show")
def config_show():
    typer.echo("Текущая конфигурация: {...}")

@config_app.command("set")
def config_set(key: str, value: str):
    typer.echo(f"Настройка изменена: {key} = {value}")

app.add_typer(config_app, name="config")
```

---

## Демонстрация работы

Убедитесь, что библиотека Typer установлена:

```bash
pip install typer
```

Запустите приложение командой:

```bash
py typer_example.py --help
```

и получите список всех доступных команд. Пример вызова команд:
- `py typer_example.py hello`
- `py typer_example.py add 2 3`
- `py typer_example.py repeat "Текст" --count 4`
- `py typer_example.py config show`
