#!/usr/bin/env bash
echo "Start deployment in minikube"
minikube_script_dir=$(cd $(dirname $0);pwd)

echo $k8s_script_dir

# Create and deploy bill service
microservice_name="bill"
k8s_namespace="${microservice_name}-svc"

bill_deployment_script_dir="${minikube_script_dir}/bill"
/bin/bash "${bill_deployment_script_dir}/deploy.bash"

kubectl apply -f "${bill_deployment_script_dir}/deployment.yaml" -n $k8s_namespace
kubectl apply -f "${bill_deployment_script_dir}/service.yaml" -n $k8s_namespace
kubectl apply -f "${bill_deployment_script_dir}/ingress.yaml" -n $k8s_namespace

# Create and deploy web service
microservice_name="web"
k8s_namespace="${microservice_name}-svc"

web_deployment_script_dir="${minikube_script_dir}/web"
/bin/bash "${web_deployment_script_dir}/deploy.bash"

kubectl apply -f "${web_deployment_script_dir}/deployment.yaml" -n $k8s_namespace
kubectl apply -f "${web_deployment_script_dir}/service.yaml" -n $k8s_namespace
kubectl apply -f "${web_deployment_script_dir}/ingress.yaml" -n $k8s_namespace

echo "Done."
echo