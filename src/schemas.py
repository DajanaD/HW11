from pydantic import BaseModel
from typing import Optional
from datetime import date

# Модель для контакту
class ContactBase(BaseModel):
    first_name: str
    last_name: str
    email: str
    phone_number: str
    birthday: date
    additional_data: Optional[str] = None

# Використовуємо введення користувача для створення нового контакту
class ContactCreate(ContactBase):
    pass

# Модель для виведення інформації про контакт користувачу
class Contact(ContactBase):
    id: int

    class Config:
        orm_mode = True
