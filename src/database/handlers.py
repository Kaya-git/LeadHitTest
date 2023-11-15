from typing import Dict, Optional, List
from tinydb import TinyDB, where, Query
from database.db import db


def find_by_dict(
        valid_data_dict
):
    return db.search(Query().fragment(valid_data_dict))


