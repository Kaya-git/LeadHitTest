from pydantic import BaseModel, EmailStr, validator
import datetime as dt
import re
from pydantic import TypeAdapter
from pydantic.dataclasses import dataclass

class FormName(BaseModel):
    form_name: str

class UserEmail(BaseModel):
    user_email: EmailStr

class PhoneNumber(BaseModel):
    user_phone: str

    @validator("user_phone")
    def check_user_phone(cls, v):
        regExs = (r"^((8|\+7)[\- ]?)?(\(?\d{3}\)?[\- ]?)?[\d\- ]{7,10}$")
        if not re.search(regExs[0], v):
            return ValueError("not match")
        return v

class Date(BaseModel):
    reg_date: dt.date

    @validator("reg_date", pre=True)
    def parse_reg_date(cls, v):
        date = dt.datetime.strptime(
            v,
            "%Y-%m-%d"
        ).date()
        return date

class Text(BaseModel):
    hello_text: str

PY_MODELS = {
    "form_name": FormName,
    "reg_date": Date,
    "hello_text": Text,
    "user_email": UserEmail,
    "user_phone": PhoneNumber
}