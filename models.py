from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class HHBaseModel(BaseModel):
    class Config:
        extra = "ignore"


class Area(HHBaseModel):
    id: str
    name: str
    url: str


class VacancyType(HHBaseModel):
    id: str
    name: str


class LogoUrls(HHBaseModel):
    url_90: Optional[str] = Field(default=None, alias="90")
    url_240: Optional[str] = Field(default=None, alias="240")
    original: Optional[str] = None


class Employer(HHBaseModel):
    id: str
    name: str
    url: str
    alternate_url: str
    logo_urls: Optional[LogoUrls] = None
    vacancies_url: str
    country_id: Optional[int] = None
    accredited_it_employer: Optional[bool] = None
    trusted: Optional[bool] = None


class Snippet(HHBaseModel):
    requirement: Optional[str] = None
    responsibility: Optional[str] = None


class Schedule(HHBaseModel):
    id: str
    name: str


class WorkFormat(HHBaseModel):
    id: str
    name: str


class WorkingHours(HHBaseModel):
    id: str
    name: str


class WorkScheduleByDays(HHBaseModel):
    id: str
    name: str


class ProfessionalRole(HHBaseModel):
    id: str
    name: str


class Experience(HHBaseModel):
    id: str
    name: str


class Employment(HHBaseModel):
    id: str
    name: str


class EmploymentForm(HHBaseModel):
    id: str
    name: str


class Department(HHBaseModel):
    id: Optional[str] = None
    name: Optional[str] = None


class Address(HHBaseModel):
    city: Optional[str] = None
    street: Optional[str] = None
    building: Optional[str] = None
    lat: Optional[float] = None
    lng: Optional[float] = None
    description: Optional[str] = None
    raw: Optional[str] = None


class Salary(HHBaseModel):
    from_: Optional[int] = Field(default=None, alias="from")
    to: Optional[int] = None
    currency: Optional[str] = None
    gross: Optional[bool] = None


class ContactPhone(HHBaseModel):
    city: Optional[str] = None
    country: Optional[str] = None
    number: Optional[str] = None
    comment: Optional[str] = None


class Contacts(HHBaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phones: List[ContactPhone] = Field(default_factory=list)


class InsiderInterview(HHBaseModel):
    id: Optional[str] = None
    url: Optional[str] = None


class Item(HHBaseModel):
    id: str
    premium: bool
    name: str
    department: Optional[Department] = None
    has_test: bool
    response_letter_required: bool
    area: Area
    salary: Optional[Salary] = None
    salary_range: Optional[Dict[str, Any]] = None
    type: VacancyType
    address: Optional[Address] = None
    response_url: Optional[str] = None
    sort_point_distance: Optional[float] = None
    published_at: datetime
    created_at: datetime
    archived: bool
    apply_alternate_url: str
    show_contacts: bool
    insider_interview: Optional[InsiderInterview] = None
    url: str
    alternate_url: str
    relations: List[Any] = Field(default_factory=list)
    employer: Employer
    snippet: Snippet
    contacts: Optional[Contacts] = None
    schedule: Optional[Schedule] = None
    working_days: List[Any] = Field(default_factory=list)
    working_time_intervals: List[Any] = Field(default_factory=list)
    working_time_modes: List[Any] = Field(default_factory=list)
    accept_temporary: Optional[bool] = None
    fly_in_fly_out_duration: List[Any] = Field(default_factory=list)
    work_format: List[WorkFormat] = Field(default_factory=list)
    working_hours: List[WorkingHours] = Field(default_factory=list)
    work_schedule_by_days: List[WorkScheduleByDays] = Field(default_factory=list)
    accept_labor_contract: Optional[bool] = None
    civil_law_contracts: List[Any] = Field(default_factory=list)
    night_shifts: Optional[bool] = None
    professional_roles: List[ProfessionalRole] = Field(default_factory=list)
    accept_incomplete_resumes: Optional[bool] = None
    experience: Optional[Experience] = None
    employment: Optional[Employment] = None
    employment_form: Optional[EmploymentForm] = None
    internship: Optional[bool] = None
    adv_response_url: Optional[str] = None
    is_adv_vacancy: Optional[bool] = None
    adv_context: Optional[Dict[str, Any]] = None


class Vacancies(HHBaseModel):
    items: List[Item]
    found: int
    pages: int
    page: int
    per_page: int
    clusters: Optional[List[Any]] = None
    arguments: Optional[List[Any]] = None
    fixes: Optional[List[Any]] = None
    suggests: Optional[Any] = None
    alternate_url: str
