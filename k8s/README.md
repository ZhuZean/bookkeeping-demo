# Bookkeeping Project
Deployment with minikube, development environment in the local machine. 

## Deployment in Minikube
#### Install minikube
Install minikube by this [documentation](https://minikube.sigs.k8s.io/docs/start/)

#### Enable ingress controller
`minikube addons enable ingress`

#### Enable istio
Install Istio by this [documentation](https://istio.io/latest/docs/setup/getting-started/#download)

#### Deploy
1. run the following bash script in root path
```
$ cd /bookkeeping-demo
$ sh ./k8s/minikube/run.bash
```

2. Check minikube external IP address

`$ kubectl get ingress -n bill-svc`

Get ingress information:

```
NAME           CLASS    HOSTS                   ADDRESS        PORTS   AGE
bill-ingress   <none>   api.minikube.zean.pro   172.16.247.6   80      15m 
```

2. Setup local DNS

Add `172.16.247.6` (shown in the ingress above) in your `/etc/hosts` file
```
172.16.247.6 api.minikube.zean.pro
172.16.247.6 demo.minikube.zean.pro
```

#### Visit the website
Frontend:
- Webpage: http://demo.minikube.zean.pro/

Backend:
- Endpoint list: http://api.minikube.zean.pro/bill/
- OpenAPI schema: https://api.minikube.zean.pro/bill/openapi
