#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Пример CLI приложения, реализованного с помощью Typer.

В этом файле представлены следующие команды:
1. hello – выводит приветственное сообщение.
2. add – складывает два числа и выводит результат.
3. repeat – повторяет заданный текст указанное число раз.
4. config – группа подкоманд для управления конфигурацией.
"""

import typer

# Создаем основной экземпляр CLI-приложения Typer.
app = typer.Typer(help="Пример CLI приложения, реализованного с Typer.")

# -----------------------------------------------------------
# Команда hello
# Описание: Выводит простое приветственное сообщение.
# -----------------------------------------------------------
@app.command()
def hello():
    """Выводит приветственное сообщение."""
    typer.echo("Привет, мир!")

# -----------------------------------------------------------
# Команда add
# Описание: Складывает два числа, введённых пользователем.
# -----------------------------------------------------------
@app.command()
def add(a: float, b: float):
    """
    Складывает два числа и выводит результат.

    Аргументы:
      a (float): Первое число.
      b (float): Второе число.
    """
    result = a + b
    typer.echo(f"Результат сложения: {result}")

# -----------------------------------------------------------
# Команда repeat
# Описание: Повторяет заданный текст указанное число раз.
# -----------------------------------------------------------
@app.command()
def repeat(text: str, count: int = 1):
    """
    Повторяет заданный текст указанное количество раз.

    Аргументы:
      text (str): Текст для повторения.
      count (int, опционально): Количество повторений (по умолчанию 1).
    """
    for _ in range(count):
        typer.echo(text)

# -----------------------------------------------------------
# Группа команд config для управления конфигурацией
# -----------------------------------------------------------
# Создаем отдельный экземпляр Typer для группы команд "config".
config_app = typer.Typer(help="Команды для управления конфигурацией приложения.")

@config_app.command("show")
def config_show():
    """Показывает текущую конфигурацию приложения (демонстрация)."""
    config_data = {"theme": "light", "version": "1.0.0"}
    typer.echo(f"Текущая конфигурация: {config_data}")

@config_app.command("set")
def config_set(key: str, value: str):
    """
    Устанавливает значение для ключа конфигурации.

    Аргументы:
      key (str): Ключ конфигурации.
      value (str): Новое значение для ключа.
    """
    typer.echo(f"Настройка изменена: {key} = {value}")

# Добавляем группу config в основное приложение.
app.add_typer(config_app, name="config")

if __name__ == "__main__":
    app()
