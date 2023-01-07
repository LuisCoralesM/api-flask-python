# Python Pet Project

## Run the API

This project mainly focuses on the Flask API, so to run it you must first go to the `api/` folder.

```
cd api
flask --app main.py run
```

These are the current endpoints:

- **GET** `/` to get the index page WIP
- **GET** `/pokemon/` to get all Pokemon
- **GET** `/pokemon/<id>` to get a Pokemon by id
- **POST** `/pokemon/` to add a new Pokemon, send a body with `name` and `type`

## Dependencies

This project has `pre-commit` as a dependency.

### Install dependencies

`pip install -r requirements.txt`

### Current linter

`Pylint`
