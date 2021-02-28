# Bookkeeping Project
This is a demo project for bookkeeping application.
It is based on the Vue 3, Django and Nginx.


# Preview
## Online demo
Frontend page: http://demo.zean.pro <br />
Backend:
- Endpoint list: http://api.zean.pro/
- OpenAPI schema: http://api.zean.pro/openapi
## Frontend (Vue 3)
It shows how to add a new record on the bookkeeping for current month dynamically.

![image](https://github.com/ZhuZean/bookkeeping-demo/blob/main/preview/frontend/demo.gif)

## Backend (Django)
Django rest framework is used to make the Restful APIs.

### Endpoints list
![image](https://github.com/ZhuZean/bookkeeping-demo/blob/main/preview/backend/endpoint%20list.png)
### OpenAPI schema
![image](https://github.com/ZhuZean/bookkeeping-demo/blob/main/preview/backend/openapi.png)


# How to run
The whole project supports docker, so we can use `docker-compose` to run the project in the local machine.
```
$ cd /root_path

$ docker-compose -f docker-compose-demo.yml up -d --build
```
Frontend page: http://127.0.0.1 <br />
Backend:
- Endpoint list: http://127.0.0.1:2000/
- OpenAPI schema: http://127.0.0.1:2000/openapi