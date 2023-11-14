from .schemas import PY_MODELS
from fastapi import HTTPException, status


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
    
def check_list_equal(
        answer_list
):
   answer =  all(
        answer_list[i] < answer_list[i+1] for i in range(len(answer_list)-1)
    )
   return answer
