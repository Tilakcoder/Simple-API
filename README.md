# Simple-API
This is simple project based on django REST API. This project uses API to save and get the data of a family members. The data is divided into two main tables Parent and Children.There is also a third table names Member which has only one field named flat. Member table is created to connect diffrent Parent objects to one Member of a family. These tables are created using django models.

# How to start project
Just after running the default django server by using the command ``python manage.py runserver`` 
go to the browser and open the this link for accessing all the data:
``http://127.0.0.1:8000/member/``

For accessing and saving Parents data go to this link:
``http://127.0.0.1:8000/parent/``

For accessing and saving Children data go to this link:
``http://127.0.0.1:8000/child/``
