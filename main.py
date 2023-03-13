#!/usr/bin/python3
from models.base_model import BaseModel


myd = {'id': '55e6b42b-5f7d-4b01-9811-f2fc3c76eacc', 'created_at': '2023-03-13T10:56:21.824373', 'updated_at': '2023-03-13T10:56:21.824426', 'name': 'My First Model', 'my_number': 89, '__class__': 'BaseModel'}

bm = BaseModel(**myd)
print(bm)