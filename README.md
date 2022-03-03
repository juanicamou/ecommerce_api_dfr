# Ecommerce API REST using Django Rest Framework

So far only the user api is implemented. The methods are the following:

- `/user/all` GET. Returns all users

- `/user/create` POST. Creates a new user.

```
Resquest:
{
    "password": "",
    "username": "",
    "email": "",
    "name": "",
    "last_name": ""
}
```

- `/user/detail/<product_pk>` GET. Returns the detail of a specific user.

- `/user/update/<product_pk>` PUT. Updates a specific user.

```
Resquest:
{
    "password": "",
    "username": "",
    "email": "",
    "name": "",
    "last_name": ""
}
```

- `/user/delete/<product_pk>` DELETE. Deletes a specific user.

### Steps
1. Install Requirements.
`pip install -r requirements.txt`
2. In ecommerce_api_dfr/ecommerce_rest/ run py manage.py runserver.
3. The API will be displayed by default in http://127.0.0.1:8000/. In any case, the output of the command from point 2 shows the address of our app.