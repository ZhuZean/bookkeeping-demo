#!/usr/bin/env bash
echo "Start deployment in minikube"
minikube_script_dir=$(cd $(dirname $0);pwd)



# Create and deploy bill service
microservice_name="bill"
k8s_namespace="${microservice_name}-svc"
bill_script_dir="${minikube_script_dir}/bill/deployment"

/bin/bash "${bill_script_dir}/deploy.bash"
kubectl apply -f "${bill_script_dir}/deployment.yaml" -n $k8s_namespace
kubectl apply -f "${bill_script_dir}/service.yaml" -n $k8s_namespace
kubectl apply -f "${bill_script_dir}/ingress.yaml" -n $k8s_namespace

echo $script_dir


echo "Done."
echo