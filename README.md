api endpoints to test:

- http://127.0.0.1:8000/restaurant/menu/

- http://localhost:8000/restaurant/booking/tables
  it will throw an authentication error
  to get access:
    register a user at http://127.0.0.1:8000/auth/users/
    use it to log in at http://127.0.0.1:8000/auth/token/login and get a token
    call again the endpoint http://localhost:8000/restaurant/booking/tables but in insomnia add an auth with bearer token <token> and prefix Token

- a sample static page with an image is visible at http://127.0.0.1:8000/restaurant/
