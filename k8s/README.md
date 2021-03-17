# Bookkeeping Project
Deployment with minikube, development environment in the local machine. 

## Minikube



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
