# Rota Viagem

This is a small project using Django and Django Rest Framework, which implements a situation for the situation where a person will travel and for that he needs the most cost-effective route to reach his destination. Flight routes are made available for the API via a .csv or .txt file that is made available in the files folder (the use of a database to store this data has not yet been implemented).

This is a sample of a .csv file, other samples can be found in the /files folder:
```csv
GRU,BRC,10
BRC,SCL,5
GRU,CDG,75
GRU,SCL,20
GRU,ORL,56
ORL,CDG,5
SCL,ORL,20
```
The main problem of this project, finding the best path among the flight routes, was solved using an implementation of the Dijkstra algorithm to search for the least cost path.
## Architeture
I tried to follow an architecture similar to DDD in the project, so there are three layers in the project: Application, Domain and Infrastructure.

```
|api
|---- application
|--------| serializers.py
|--------| views.py
|
|---- domain
|--------| graph_entity.py
|--------| route_domain.py
|
|----infrastructure
|--------| fileCSV.py
|--------| fileTXT.py
```

##### Application
The application layer is responsible for managing requests and is responsible for redirecting to the domain layer.In this layer, I made available the views.py and serializers.py files. 

The views.py file is where the GET and POST methods that are accepted by the API are implemented. The serializers.py file is where the structure of the data to be received and sent by the API was defined, this definition is used by views.py to validate the body of the received message.

##### Domain
The domain layer is where the entities containing the business domain are located. The business rule was applied here, so it is in this layer that the search for the best path is carried out.

##### Infrastructure
The application accepts .csv and .txt files as a way of consuming the flight routes, the implementations for reading and writing files are different for each type of file. Thus, there is a class for each type of file that implements these functions, and the determination of which to use is identified by the application through the configuration file.

rota_viagem/settings.py
```
FILE_EXAMPLE = 'files/input-file-test.csv'
```

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

What things you need to install the software and how to install them:
- docker

ou

- python3
- virtualenvwrapper
`

### Installing
A step by step series of examples that tell you how to get a development env running

##### Docker
If you are using docker just clone the project on your computer and execute the following command on root path:
```
make run
```

And to stop the execution:

```
make stop
```

##### Virtualenvwrapper
If you are using virtualenvwrapper with python3 just follow the steps below

```
mkvirtualenv rotas_viagem
workon rotas_viagem
pip install -r requirements.txt
python manage.py runserver
```

## Running the tests

Unit tests can be found in the ./test directory. They test the views calls, the features implemented in the domain classes and the features of the infrastructure classes. 

To execute them, just execute the following commands:

###### Docker

```
make test
```

###### Python3 and VirtualenvWrapper

```
pytest --cov=api api/tests/ -vv
```

### End-to-End Tests


The project can be used both as an API, and also performs a function call via shell.To execute the project through the shell, just execute the following commands:

#### Shell
Shell calls must always include the path to a .csv or .txt file that will contain flight information, exactly as described at the beginning of the documentation. The only functionality available for shell calls is the best path check.

######  Docker
Remembering that if the file must also be inside the container to be able to be executed from there. There are two files for testing that are available in the / files folder.

```shell
make shell
python3 shell_exec.py path_to_file.csv
```
```shell
Please use - to separate the locations. Ex.: ONE - ANOTHER
please enter the route: GRU-CGD
best route: GRU - BRC - SCL - ORL - CDG > $40
```

###### Python3 and VirtualenvWrapper
``` shell
python shell_exec.py path_to_file.csv
```

```shell
Please use - to separate the locations. Ex.: ONE - ANOTHER
please enter the route: GRU-CGD
best route: GRU - BRC - SCL - ORL - CDG > $40
```

#### API
It is also possible to make JSON calls to the API, so remember to have the application running as described in the Installation topic. The API has two routes available, the first one that checks the best path always based on what is the origin and which is the destination.

The second allows new routes to be inserted into the file used at the time of execution. These changes can alter the verification result by the best way, and a new better way can be discovered.

###### Best Route - GET
The queryparams are mandatory and the two fields must always be sent in this request.
- Request
localhost:8000/best-route/?from=GRU&to=CDG   

- Response Body
```json 
{
"route": "GRU - BRC - SCL - ORL - CDG",
"total_cost": 40
}
```
###### New Route - POST

- URL
localhost:8000/route/ 

- Resquest Body
```json
{"routes" : [
        {"origin" : "NewOrigin", 
        "end" : "NewDestination",
        "cost" : 5}
        ]
}
``` 

- Response
201 - No content

#### Status Code and Messaging

Status Code   | Message
------- | ------
201     | No content
400     | The nodes are not connected.
400     | Please, send two valid locations to verify: origin and destination.
400     | Invalid route attributes.
400     | {"routes": ["This field is required."]}


## Built With

* [Django](https://www.djangoproject.com/) 
* [Django Rest Framework](https://maven.apache.org/) - The web framework used
* [pytest-django](https://pytest-django.readthedocs.io/en/latest/tutorial.html) - Django Test Suite
* [pytest-cov](https://pypi.org/project/pytest-cov/) - Python Pytest Coverage

## Authors

* **Mayara Machado** - *Initial work* - [mchdax.now.sh](https://mchdax.now.sh/)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
