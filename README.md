# vacancy_tracker

A small command-line tool that searches job vacancies through the public HH.ru API and prints them in a readable format. It is a small learning project.

## Demo
<!-- TODO: add a screenshot or GIF -->

## Features
- Searches `https://api.hh.ru/vacancies` by a text query
- Parses and validates the API response with Pydantic models
- Prints each vacancy: title, company, area, salary, experience, employment type, schedule, publish date, URL, requirement and responsibility snippets
- Optional `-sf` flag to choose the search field (`name`, `company_name`)
- Optional `-f` flag to also save the result to `vacancies.json`

Limitations: only the first page (10 results) is requested, and the `-f` flag always writes to `vacancies.json` (the value you pass is not used as a file name). There is minimal error handling and no tests.

## Tech stack
- Python 3.13+
- httpx
- Pydantic v2
- uv (project and dependency management)

## How to run
```bash
git clone <repo-url>
cd vacancy_tracker
uv sync
uv run python run.py "python"
uv run python run.py "python" -sf name
uv run python run.py "python" -f vacancies.json
```
No API key or environment variables are needed.

Example output (shortened):
```text
Found: <total> | Page: 1/<pages> | Per page: 10
----------------------------------------------------------------------------------------------------
1. <vacancy title>
   Company: <company>
   Area: <city>
   Salary: not specified
   Experience: ...
   Employment: ...
   Schedule: ...
   Published: <date time>
   URL: https://hh.ru/vacancy/<id>
   Requirement: ...
   Responsibility: ...
----------------------------------------------------------------------------------------------------
```

## What I learned
<!-- TODO: write 2-4 sentences in your own words -->
