from fastapi import APIRouter, Form, HTTPException, status
from database.db import db
from tinydb import where
from .schemas import PY_MODELS, UserEmail
from .handlers import check_fields_in, check_list_equal
from typing import List
from collections import Counter


from_verif_router = APIRouter(
    prefix="/form",
    tags=["Роутер форм"]
)

@from_verif_router.post("/get_form")
def get_form(
    quary_string: str 
):
    # f_name1=value1&f_name2=value2
    forms_list = quary_string.split("&")
    quary_num = len(forms_list)
    fields_num = len(PY_MODELS)
    valid_data_list = []
    print(
        f"Количество запросов: {quary_num},\n"
        f"Количество полей в форме: {fields_num},\n"
    )

    for form in forms_list:

        quary = form.split("=")
        valid_data = check_fields_in(
            quary[0],quary[1]
        )
        print(valid_data)
        valid_data_list.append(valid_data)
    # Если колличество запросов небольше чем полей в форме, то проверяем, что бы каждый запрос был валидным и выдавал ту же самую форму
    answer_list = []
    if quary_num < fields_num:
        for data in valid_data_list:
            data_key = list(data.keys())[0]
            data_value = data[data_key]
            answer = db.search(where(data_key) == data_value)
            if len(answer) is not 0:
                answer_list.append(answer[0]["form_name"])
            if len(answer) is 0:
                return ("Нет записи в бд по вашим запросам")
        if check_list_equal(answer_list) is True:
            return answer_list[0]
        print(*answer_list)
    # Если колличество запросов больше чем полей в форме, то проверяем что бы кол во верных запросов было равно кол ву полей в форме
    if quary_num > fields_num:
        for data in valid_data_list:
            answer = db.search(where(data.keys()[0]) == data[data.keys()[0]])

            if answer is not []:
                answer_list.append(answer[0]["form_name"])
        
        form_names = Counter(answer_list)
        for form_name in dict(form_names).keys():
            if dict(form_names)[form_name] == fields_num:
                return form_name

    # Если колво запросов равноценно, то каждый запрос должен выдавать верный запрос
    if quary_num == fields_num:
        for data in valid_data_list:
            answer = db.search(where(data.keys()[0]) == data[data.keys()[0]])
            if answer is []:
                return ("If quary_num == fields_num / not true")
            
        return data[data.keys()[0]]

"user_email=ebuzuev@gmail.com&phone_number=+79823356450"