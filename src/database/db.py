from tinydb import TinyDB, Query


db=TinyDB('db.json')

def insert():
    db.insert(
        {
            "form_name": "form1",
            "user_email": "ebuzuev@gmail.com",
            "user_phone": "+79823356450",
            "reg_date": "2023-11-10",
            "hello_text": "Some random stuff 1"
        }
    )
    db.insert(
        {
            "form_name": "form2",
            "user_email": "antonov@gmail.com",
            "user_phone": "+78473256748",
            "reg_date": "2023-11-11",
            "hello_text": "Some random stuff 2"
            }
    )
    db.insert(
        {
            "form_name": "form3",
            "user_email": "pavlov@gmail.com",
            "user_phone": "+78123567489",
            "reg_date": "2023-11-12",
            "hello_text": "Some random stuff 3"
        }
    )
    db.insert(
        {
            "form_name": "form4",
            "user_email": "sergeev@gmail.com",
            "user_phone": "+78123567489",
            "reg_date": "2023-11-13",
            "hello_text": "Some random stuff 3"
        }
    )

insert()
