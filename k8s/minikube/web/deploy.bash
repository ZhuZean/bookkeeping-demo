#!/usr/bin/env bash
echo
script_dir=$(cd $(dirname $0);pwd)

microservice_name="web"
DEV_CLUSTER_NAME=development-cluster

# Automatic k8s namespace creation
k8s_namespace=${microservice_name}-svc
k8s_namespace_grep=$(kubectl get namespaces | grep ${k8s_namespace})
if [ ! -z "$k8s_namespace_grep" ]; then
    echo "Kubernetes namespace '${k8s_namespace}' exists. Skipping creation."
else
    echo "Kubernetes namespace '${k8s_namespace}' not found..."
    kubectl create namespace ${k8s_namespace}
fi


echo "Done."
echo