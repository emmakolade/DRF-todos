### Features
* CRUD (Create, Read, Update, and Delete) functionality for todo tasks
* Authentication and Authorization using DRF's built-in token-based authentication
* Filtering and ordering of todo tasks
* Pagination for large lists of tasks

### Endpoints
The API has the following endpoints:
* /todos/: This endpoint allows you to create, read, update, and delete todo tasks.
* /auth/: This endpoint allows you to obtain a token for authentication and authorization.

### Authentication and Authorization
The API uses DRF's built-in token-based authentication. To obtain a token, send a POST request to the /auth/ endpoint with a valid username and password. Once you have a token, you must include it in the Authorization header of your requests to the /todos/ endpoint in the format Token <token>.

Filtering and Ordering
You can filter and order the todo tasks by sending query parameters in the GET request to the /todos/ endpoint.

* Filtering: You can filter the tasks by passing the field name and desired value as query parameters. For example, to get all tasks with a done status of True, you would send a GET request to /todos/?done=True.
* Ordering: You can order the tasks by passing the field name and desired order as query parameters. For example, to get all tasks ordered by their created_at field in descending order, you would send a GET request to /todos/?ordering=-created_at.

### Test coverage
This API has a test coverage that covers all the endpoints and functionalities. The test coverage is calculated using the coverage library.

### Examples
#### Obtain Token

```python
POST /auth/

{
    "username":"test",
    "password":"test"
}
```
#### Create Todo

```python
POST /todos/

{
    "title": "Clean the house",
    "description": "Wipe down surfaces and vacuum",
    "done": false
}
```
#### Get Todo
```python
GET /todos/1/
```
#### Update Todo
```python
PATCH /todos/1/

{
    "title": "Clean the apartment",
}
```
#### Delete Todo
```python
DELETE /todos/1/
```
