# Rental App Backend

Django Backend APIs for [Rental Mobile App in Flutter](https://github.com/bunny98/Rental-Flutter-App)

## Model Details

* class **RentSomething**
  * *name* : Name of the object up for rent
  * *sellerName* : Name of the person putting the above mentioned thing on rent
  * *image* : Image of the object
  * *cost* : Cost at which the object is being lent against
  * *address* & *roomNum* : Address of the person renting the object
  * *mobileNum* : Mobile number of the person renting the object

## API Endpoints

* *upload/* : GET Requests return all of the above mentioned fields
* *upload/* : POST Requests commit the posted data to the database after validating them and returns a copy of the committed data 

### Prerequisites

* Django
* rest_framework

### Running

Follow the following commands to run the server:
```
cd dictionaryOfClonedFiles
python manage.py runserver
```
Make GET/POST requests to following url:
```
http://127.0.0.1:8000/upload/
```

## Acknowledgments

* Inspired by Entrepreneurship Course at [International Institute of Technology, Naya Raipur](https://www.iiitnr.ac.in/)
