from typing import Literal

import httpx

from models import Vacancies


class ApiManager:
    def __init__(self) -> None:
        self._base_url = "https://api.hh.ru"
        self._headers = {
            "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:147.0) Gecko/20100101 Firefox/147.0"
        }
        self._client = httpx.Client(base_url=self._base_url, headers=self._headers)

    def get_vacancies(
        self,
        query: str | None = None,
        page: int | None = 0,
        per_page: int | None = 10,
        search_field: Literal["name", "company_name", "id", "all"] = "all",
    ):
        parameters = "/vacancies?"

        if query:
            parameters += f"text={query}&"
        if page is not None and per_page is not None:
            parameters += f"per_page={per_page}&page={page}&"
        if search_field != "all":
            parameters += f"search_field={search_field}&"

        try:
            response = self._client.get(parameters)
            if not response.status_code == 200:
                ...
            return Vacancies.model_validate_json(response.content)
        except Exception as e:
            raise e

    @staticmethod
    def _format_salary(salary) -> str:
        if not salary:
            return "not specified"

        from_part = salary.from_ if salary.from_ is not None else "?"
        to_part = salary.to if salary.to is not None else "?"
        currency = salary.currency or ""
        tax = "gross" if salary.gross else "net"
        return f"{from_part} - {to_part} {currency} ({tax})".strip()

    @staticmethod
    def _truncate(text: str | None, limit: int = 140) -> str:
        if not text:
            return "-"
        text = " ".join(text.split())
        if len(text) <= limit:
            return text
        return text[: limit - 3] + "..."

    def format_vacancies(self, vacancies: Vacancies, limit: int | None = None) -> str:
        items = vacancies.items[:limit] if limit is not None else vacancies.items

        lines = [
            f"Found: {vacancies.found} | Page: {vacancies.page + 1}/{vacancies.pages} | Per page: {vacancies.per_page}",
            "-" * 100,
        ]

        for index, vacancy in enumerate(items, start=1):
            company = vacancy.employer.name if vacancy.employer else "unknown"
            area = vacancy.area.name if vacancy.area else "unknown"
            schedule = vacancy.schedule.name if vacancy.schedule else "not specified"

            requirement = self._truncate(
                vacancy.snippet.requirement if vacancy.snippet else None
            )
            responsibility = self._truncate(
                vacancy.snippet.responsibility if vacancy.snippet else None
            )

            lines.extend(
                [
                    f"{index}. {vacancy.name}",
                    f"   Company: {company}",
                    f"   Area: {area}",
                    f"   Salary: {self._format_salary(vacancy.salary)}",
                    f"   Experience: {vacancy.experience.name if vacancy.experience else 'not specified'}",
                    f"   Employment: {vacancy.employment.name if vacancy.employment else 'not specified'}",
                    f"   Schedule: {schedule}",
                    f"   Published: {vacancy.published_at.strftime('%Y-%m-%d %H:%M')}",
                    f"   URL: {vacancy.alternate_url}",
                    f"   Requirement: {requirement}",
                    f"   Responsibility: {responsibility}",
                    "-" * 100,
                ]
            )

        return "\n".join(lines)

    def print_vacancies(self, vacancies: Vacancies, limit: int | None = None) -> None:
        print(self.format_vacancies(vacancies, limit=limit))

    def save_to_json(
        self, vacancies: Vacancies, filename: str = "vacancies.json"
    ) -> None:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(vacancies.model_dump_json(indent=2, by_alias=True))
