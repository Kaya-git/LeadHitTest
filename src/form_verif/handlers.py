from .schemas import PY_MODELS
from fastapi import HTTPException, status
from collections import Counter


def check_fields_in(
        field_name,
        field_value
):  
    if field_name in PY_MODELS.keys():
        quary = {
            field_name: field_value
        }
        valid_data = PY_MODELS[field_name](**quary)
        if valid_data is not None:
            return valid_data.dict()
        return None


def quary_num_equal_fields_num(
        form_names_list,
        fields_num
):
    form_names = Counter(form_names_list)
    form_equal = []
    form_names_dict = dict(form_names)
    for form_name in form_names_dict.keys():
        if form_names_dict[form_name] != fields_num:
            form_equal.append(False)
        else:
            form_equal.append(True)
    if True not in form_equal:
        return False
    return form_name
