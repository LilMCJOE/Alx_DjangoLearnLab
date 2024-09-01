# API Project with Django REST Framework

This project is built using Django REST Framework (DRF) to provide a set of RESTful API endpoints for managing book data. The API is secured using token-based authentication, and access is restricted based on user permissions.

## Authentication Setup

The API uses token-based authentication to secure endpoints. Only authenticated users with valid tokens can access the API.

### Obtaining a Token

Users can obtain an authentication token by sending a POST request with their username and password to the `/api-token-auth/` endpoint.

Example using `curl`:

```bash
curl -X POST -d "username=songa_joel&password=joel" http://127.0.0.1:8000/api-token-auth/
