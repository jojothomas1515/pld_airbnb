#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel

myd = {'id': '55e6b42b-5f7d-4b01-9811-f2fc3c76eacc', 'created_at': '2023-03-13T10:56:21.824373',
       'updated_at': '2023-03-13T10:56:21.824426', 'name': 'My First Model', 'my_number': 89, '__class__': 'BaseModel'}

all_objs = storage.all()
print("-- Reloaded objects --")
for obj_id in all_objs.keys():
    obj = all_objs[obj_id]
    print(obj)

print("-- Create a new object --")
my_model = BaseModel()
my_model.name = "My_First_Model"
my_model.my_number = 89
my_model.save()
print(my_model)
