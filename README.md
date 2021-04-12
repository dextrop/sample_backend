
# samplebackend

##### Project Installation Script

```
cd path/to/project/folder
./install.sh
```

##### Project Migration Script

```
cd path/to/project/folder
./migrate.sh
```

The script will install all required packages from pip and do server migration.

##### Packages installed from script

- django ( 2.2 )
- djangorestframework ( 3.10.3 )
- django-cors-headers ( 3.4.0 )
- python-json-logger ( 0.1.11 )
- requests
     
##### Running Server

```
python manage.py runserver
```

##### Make sure python environment is properly configured with python 3.7+. 
##### Working over pycharm is preferred

# Project Structure
#### Python Packages:

- `src`: This will be application for backend project samplebackend. i.e All models, controllers and views will be stores inside src folder.
- `src/lib`: Libraries for custom exception handler, custom response, authentication class and loggin class will be stored inside src/lib folder.
- `src/models`: The python package will hold all Models related to project.
- `src/views`: The python package will hold all Views related to project.
- `src/controllers`: The python package will hold all Controllers related to project.
- `logs`: API logs store location

#### Project Files :
    
- `src/lib/customexceptionhandler.py`: The module is responsible for handling exceptions.
- `src/lib/customresponse.py`: The module is responsible for returning JSON Response.
- `src/lib/loggingmixin.py`: The class is responsible for handling API Logs.
- `src/lib/authentication.py`: Authentication class 
- `src/lib/permissions.py`: Permission class
- `src/views/statusview.py`: Sample view showing api status, can be excessed using http://localhost:8000/
- `src/views/helpers.py`: Helper functions will be stored here
- `requirements`: Python Package Requirements file.


## API's

### Status API
`GET`: `http://localhost:8000/`

##### Response
```
{
  "status": true,
  "payload": true,
  "message": "Server Is Up and Running"
}
```

## UsersAPI GET Api
`GET`: `http://localhost:8000/v1/users/`

#### Headers
`{"Content-type": "application/json"}`

#### Response
```json
{
  "status": true,
  "payload": [
    {
  "name": "NAME",
  "phoneno": "PHONENO",
  "_id": 1,
  "_created": "2021-04-12 13:22:54.129818",
  "_updated": "2021-04-12 13:22:54.129864"
}
  ],
  "message": "UsersAPI GET Api view"
}
```

## UsersAPI POST API
`POST`: `http://localhost:8000/v1/users/`

#### Headers
{"Content-type": "application/json"}

#### Request

```json
{
  "name": "NAME",
  "phoneno": "PHONENO"
}
```

#### Response
```json
{
  "status": true,
  "payload": {
  "name": "NAME",
  "phoneno": "PHONENO",
  "_id": 1,
  "_created": "2021-04-12 13:22:54.129818",
  "_updated": "2021-04-12 13:22:54.129864"
},
  "message": "UsersAPI GET POS view"
}
```

## UsersAPI PUT API
`PUT`: `http://localhost:8000/v1/users/`

#### Headers
{"Content-type": "application/json"}

#### Request

```json
{
  "name": "NAME",
  "phoneno": "PHONENO"
}_WITH_ID
```

#### Response
```json
{
  "status": true,
  "payload": {
  "name": "NAME",
  "phoneno": "PHONENO",
  "_id": 1,
  "_created": "2021-04-12 13:22:54.129818",
  "_updated": "2021-04-12 13:22:54.129864"
},
  "message": "UsersAPI PUT Api view"
}
```

## UsersAPI DELETE API
`DELETE`: `http://localhost:8000/v1/users/`

#### Headers
{"Content-type": "application/json"}

#### Request
```json
{
    "_id": "ID of object to be deleted.
}
```

#### Response
```json
{
  "status": true,
  "payload": "Object Deleted Successfully",
  "message": "UsersAPI DELETE Api view"
}
```

#### Error Missing Key

```
# Response
{
  "status": false,
  "payload": null,
  "message": "Missing Key 'KEY_NAME' in request data",
  "error": {
    "code": 400
  }
}
```
