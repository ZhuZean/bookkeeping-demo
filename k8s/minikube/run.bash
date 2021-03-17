#!/usr/bin/env bash
echo "Start deployment in minikube"
minikube_script_dir=$(cd $(dirname $0);pwd)
k8s_script_dir=$(cd $(dirname $0)/..;pwd)

echo $k8s_script_dir

# Create and deploy bill service
microservice_name="bill"
k8s_namespace="${microservice_name}-svc"

/bin/bash "${minikube_script_dir}/bill/deploy.bash"
bill_deployment_script_dir="${k8s_script_dir}/deployment/bill"

kubectl apply -f "${bill_deployment_script_dir}/deployment.yaml" -n $k8s_namespace
kubectl apply -f "${bill_deployment_script_dir}/service.yaml" -n $k8s_namespace
kubectl apply -f "${bill_deployment_script_dir}/ingress.yaml" -n $k8s_namespace

# Create and deploy web service
microservice_name="web"
k8s_namespace="${microservice_name}-svc"

/bin/bash "${minikube_script_dir}/web/deploy.bash"
bill_deployment_script_dir="${k8s_script_dir}/deployment/web"

kubectl apply -f "${bill_deployment_script_dir}/deployment.yaml" -n $k8s_namespace
kubectl apply -f "${bill_deployment_script_dir}/service.yaml" -n $k8s_namespace
kubectl apply -f "${bill_deployment_script_dir}/ingress.yaml" -n $k8s_namespace

echo "Done."
echo