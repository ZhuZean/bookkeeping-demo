# Bookkeeping Project
This is a demo project for bookkeeping application.
It is based on the Vue 3, Django and Nginx.

## Workflow
Managed by the GitHub [Kanban board](https://github.com/ZhuZean/bookkeeping-demo/projects/1)

## Architecture [WIP]
Currently the project is deployed with docker, but I plan to move it with Kubernetes.

<img src="https://github.com/ZhuZean/bookkeeping-demo/blob/main/preview/architecture/k8s.png" width="70%" height="70%">

## Preview
### Online demo
Prototype
- [Figma link](https://www.figma.com/file/IYx7WBAG9HOsNzagNVBuBN/Personal-bookkeeping-web?node-id=0%3A1)

Frontend:
- Web page: http://demo.zean.pro

Backend:
- Endpoint list: http://api.zean.pro/
- OpenAPI schema: http://api.zean.pro/openapi

### Frontend (Vue 3)
It shows how to add a new record on the bookkeeping for current month dynamically.

![image](https://github.com/ZhuZean/bookkeeping-demo/blob/main/preview/frontend/demo.gif)

### Backend (Django)
Django rest framework is used to make the Restful APIs.

#### Endpoints list
![image](https://github.com/ZhuZean/bookkeeping-demo/blob/main/preview/backend/endpoint%20list.png)
#### OpenAPI schema
![image](https://github.com/ZhuZean/bookkeeping-demo/blob/main/preview/backend/openapi.png)


## Run in the local machine
The whole project supports docker, so we can use `docker-compose` to run the project in the local machine.
```
$ cd /bookkeeping-demo

$ docker-compose -f docker-compose-demo.yml up -d --build
```
Frontend:
- Webpage: http://127.0.0.1

Backend:
- Endpoint list: http://127.0.0.1:2000/
- OpenAPI schema: http://127.0.0.1:2000/openapi
