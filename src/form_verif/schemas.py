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
    phone_number: str

    @validator("phone_number")
    def check_phone_number(cls, v):
        regExs = (r"^79\s*\d{2}\s*\d{3}\s*\d{2}\s*\d{2}$")
        if not re.search(regExs[0], v):
            return ValueError("not match")
        return v

class Date(BaseModel):
    registry_date: dt.date

    # @validator("date")
    # def check_date_format(cls, v):
    #     if v != dt.date.strftime("%d%d.%m%m.%Y%Y"):
    #         return ValueError("not match")
    #     return v

class Text(BaseModel):
    text: str

PY_MODELS = {
    "form_name": FormName,
    "date": Date,
    "text": Text,
    "user_email": UserEmail,
    "phone_number": PhoneNumber
}