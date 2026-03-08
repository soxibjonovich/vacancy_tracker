# Vacansy Tracker

Minimal CLI project to fetch vacancies from HH.ru API and print them in a readable format.

## Stack
- Python 3.13+
- `httpx`
- `pydantic` v2

## Install
```bash
uv sync
```

## Run
```bash
uv run python run.py "python"
```

With search field:
```bash
uv run python run.py "python" -sf name
```

## What It Does
- Calls `https://api.hh.ru/vacancies`
- Validates response with Pydantic models (`models.py`)
- Prints compact vacancy cards via `ApiManager.print_vacancies(...)`

## Example Output
```text
Found: 783 | Page: 1/783 | Per page: 10
----------------------------------------------------------------------------------------------------
1. Python-разработчик
   Company: Subscrible
   Area: Тбилиси
   Salary: not specified
   Experience: От 1 года до 3 лет
   Employment: Полная занятость
   Schedule: Удаленная работа
   Published: 2026-02-27 22:29
   URL: https://hh.ru/vacancy/130845553
   Requirement: ...
   Responsibility: ...
----------------------------------------------------------------------------------------------------
```

### Source
https://solvit.space/projects/vacancies_statistics

