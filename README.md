Build API views to manage listings and bookings, and ensure the endpoints are documented with Swagger.


# alx_travel_app_0x01

## Objective
Implement CRUD API endpoints for Listings and Bookings using Django REST Framework, and document them with Swagger.

## Features
- ViewSets for `Listing` and `Booking` models.
- RESTful API endpoints under `/api/`.
- Interactive Swagger documentation at `/swagger/`.

## Tools
- Django
- Django REST Framework
- drf-yasg (Swagger)
- Postman

## Testing
Use Postman or the Swagger UI to perform:
- GET, POST, PUT, DELETE on `/api/listings/` and `/api/bookings/`

## Expected Output
A working CRUD API with documented endpoints and verified responses.

## Swagger docs: 
http://127.0.0.1:8000/swagger/

## ReDoc: 
http://127.0.0.1:8000/redoc/

## Test Endpoints in Postman

Test each CRUD operation:

Endpoint	Method	Description
/api/listings/	GET	Retrieve all listings
/api/listings/	POST	Add new listing
/api/listings/{id}/	GET	Retrieve listing by ID
/api/listings/{id}/	PUT	Update listing
/api/listings/{id}/	DELETE	Delete listing
/api/bookings/	Same pattern	CRUD for bookings

Author

Developed by Ikgopoleng Mophuting for ALX Backend Development 

Django REST API module.
