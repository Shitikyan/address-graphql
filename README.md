## How to use this app

1. First step you need to create or activate conda or venv
2.  for conda you can use:
    ```commandline
       conda activate
    ```
    - Conda tutorial [link](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html)
    - If you want to use venv. [venv tutorial](https://docs.python.org/3/library/venv.html)
3. you need to install all modules that need for correct working.
    - for this you need to use this command
    ```commandline
    pip install -r requirements.txt
    ```
4. then you will need to make migrationsm (be sure that you are in root directory)
    ```commandline
    python manage.py migrate
    ```
5. then just run application with command
    ```commandline
    python manage.py runserver
    ```
6. open browser go to url http://127.0.0.1:8000/graphql/

## Queries for usage
this is query examples that will help you tu understand how it will work ...

1. get by zip_code and address
```graphQl
{
    building (zipCode: "11222", address: "156, NOBLE STREET, C4-3A") {
      id,
     address,
     state
    }
}
```
2. fetch data from NYC api and append to database 
```graphQl
mutation {
    createCategory: createCategory{
        status
    }
}
```
3. get all dates from db
```graphQl
{
    buildings {
        id,
        address,
        state
    }
}
```

also you can use documentation in browser page for more details