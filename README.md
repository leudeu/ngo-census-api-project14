## Requirements
- Docker
- kubectl
- Minikube

## Run
minikube start
docker build -t census-api:latest .
kubectl apply -f k8s/namespaces.yaml
kubectl apply -f k8s/dev/
kubectl port-forward -n dev svc/census-service 5000:5000
