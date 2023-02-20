# mock-server-client

A simple webserver and client using FastAPI and Requests. (Coding exercise)

## Introduction

A simple webserver and client built with [FastAPI](https://fastapi.tiangolo.com) and [Requests](https://requests.readthedocs.io/en/latest/).

## Webserver

### How to Run:

**Requirement**: Python 3.9 or above

1. [optional] Create a python virtual environment:  `python -m venv venv` and activate using: `./venv/bin/activate`
2. Install the dependencies: `pip install -r requirements.txt`
3. We can now start the server using: `python main.py`.  
**Note:** Default port is 8000 and URL is: [http://127.0.0.1:8000](http://127.0.0.1:8000)
4. The API documentation can be found in the Swagger UI at [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs).The Swagger UI gives an interactive UI to play around with the two API endpoints.

### Walkthrough
The webserver app is available at `./app/` and is divided into different files:
1. [`endpoints.py`](https://github.com/s1dharth-s/mock-server-client/blob/main/app/endpoints.py): The two API endpoints are defined over here. Some basic error handling capablilities such as returning `404` error when an ID is not found has been added. But much more improvements could be made.

2. [`database.py`](https://github.com/s1dharth-s/mock-server-client/blob/main/app/database.py): A simple SQLite database to store the data. I have chosen to use SQLAlchemy ORM to work with the database because I find working with ORMs much easier and intuitive.

    [`model.py`](https://github.com/s1dharth-s/mock-server-client/blob/main/app/models.py) is where the ORM model of the database is defined.

3. [`schema.py`](https://github.com/s1dharth-s/mock-server-client/blob/main/app/schema.py): A big reason why I like working with FastAPI is [pydantic](https://docs.pydantic.dev/). It helps in data validation and type management. The pydantic model for the API request and response body is defined here.

## Client

The client can be found at `client.py` and is even simpler than the webserver. I have implemented it as a class and the methods can be imported and used to call the GET and PUT API methods of our websever with ease.

## Further Improvements

* Logging: Logging is quite important for any application. Here I have not implemented logging yet as it is a barebones program, but given time it will be the next addition.
* We can dockerize the application, making its deployment and management even easier.
* Tests: Testing is also an important thing I have overlooked here.
* Configuration file: A lot of values like the webserver port, client application URL etc are hardcoded now. Ideally these values should be configurable and read from a configuration file (eg: config.ini).
* Additional error handling capabilites for the client: I ran out of time by the time I reached this part!
* Mechanism to generate unique IDs instead of using integers.
