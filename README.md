# Bookkeeping Project
This is a demo project for bookkeeping application.
It is based on the Vue 3, Django and Nginx.

## Workflow
Managed by the GitHub [Kanban board](https://github.com/ZhuZean/bookkeeping-demo/projects/1)

## Deployment with Kubernetes :star2: 
See more details in this [page](https://github.com/ZhuZean/bookkeeping-demo/tree/main/k8s)

## Preview
### Online demo
Prototype
- [Figma link](https://www.figma.com/file/IYx7WBAG9HOsNzagNVBuBN/Personal-bookkeeping-web?node-id=0%3A1)

Frontend:
- Web page: http://demo.k8s.zean.pro

Backend:
- Endpoint list: http://api.k8s.zean.pro/bill/
- OpenAPI schema: http://api.k8s.zean.pro/bill/openapi

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
