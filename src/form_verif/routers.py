from fastapi import APIRouter, HTTPException, status
from tinydb import where
from .schemas import PY_MODELS
from .handlers import check_fields_in, quary_num_equal_fields_num
from database.handlers import find_by_dict


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


    valid_data_dict = {}
    valid_data_list = []
    for form in forms_list:
        quary = form.split("=")

        valid_data = check_fields_in(
            quary[0],quary[1]
        )
        if valid_data is None:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Поле {quary[0]} является полем формы"
            )

        data_key = list(valid_data.keys())[0]
        data_value = valid_data[data_key]

        if quary_num > fields_num:
            valid_data_list.append(valid_data)
        else:
            valid_data_dict[data_key] = data_value

    
    if quary_num == fields_num or quary_num < fields_num:
        form = find_by_dict(valid_data_dict)
        if len(form) != 0:
            return form[0]["form_name"]
    
        if len(form) == 0:
            for quary_field in valid_data_dict.keys():
                valid_data_dict[quary_field] = str(type(valid_data_dict[quary_field]))
            return valid_data_dict

    # # Если кол-во валидных запросов больше полей в форме, то проверяем что бы кол-во одинаковых вхождений в бд было равно кол-ву полей
    if quary_num > fields_num:
        form_names_list = []
        not_found_dict = {}
        for data in valid_data_list:

            form = find_by_dict(data)

            if len(form) != 0:
                form_names_list.append(form[0]["form_name"])

        form_name = quary_num_equal_fields_num(
            form_names_list, fields_num
        )

        if form_name is False:
            for data in valid_data_list:
                for field_name in data.keys():
                    not_found_dict[field_name] = str(type(data[field_name]))
            return not_found_dict
        return form_name


"user_email=ebuzuev@gmail.com&user_phone=+79823356450&reg_date=2023-11-11&hello_text=Some random stuff 1&form_name=form1&user_phone=+78123567489"