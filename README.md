# 🚀 Production-Grade Microservices DevOps Project

## 📌 Overview

This project demonstrates a complete end-to-end DevOps pipeline by building and deploying a production-grade microservices application using modern tools and cloud infrastructure.

The application consists of multiple Python-based microservices that are containerized, deployed on Kubernetes (AWS EKS), and managed through an automated CI/CD pipeline.

---

## 🧱 Architecture

* Microservices-based application (User Service & Product Service)
* Containerized using Docker
* Orchestrated using Kubernetes (EKS)
* Infrastructure provisioned using Terraform
* CI/CD automated using GitHub Actions

---

## ⚙️ Tech Stack

* **Backend:** Python (FastAPI)
* **Containerization:** Docker
* **Orchestration:** Kubernetes (Minikube + AWS EKS)
* **CI/CD:** GitHub Actions
* **Infrastructure as Code:** Terraform
* **Cloud Provider:** AWS
* **Monitoring:** Prometheus & Grafana (optional)
* **Logging:** ELK Stack (optional)

---

## 🏗️ Project Structure

```
Microservices/
│
├── user-service/
│   ├── main.py
│   └── Dockerfile
│
├── product-service/
│   ├── main.py
│   └── Dockerfile
│
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
│
├── terraform/
│   ├── main.tf
│   ├── eks.tf
│   ├── provider.tf
│   └── variables.tf
│
└── .github/workflows/
    └── cicd.yaml
```

---

## 🔄 CI/CD Pipeline

* Triggered on push to `main` branch
* Builds Docker images for both services
* Pushes images to DockerHub
* Ready for deployment on Kubernetes

---

## ☸️ Kubernetes Deployment

* Deployments created for each microservice
* Services used to expose applications
* LoadBalancer used for external access (EKS)
* Pods scaled using replicas

---

## ☁️ Infrastructure (Terraform)

* VPC with custom CIDR block
* Public subnets across multiple Availability Zones
* Internet Gateway and Route Tables
* Security Groups for access control
* EC2 instance (for initial setup)
* EKS Cluster with managed node groups

---

## 🚀 How to Run

### 🔹 1. Build & Push Docker Images

```bash
docker build -t itstechutsav/user-service ./user-service
docker push itstechutsav/user-service

docker build -t itstechutsav/product-service ./product-service
docker push itstechutsav/product-service
```

---

### 🔹 2. Provision Infrastructure

```bash
cd terraform
terraform init
terraform apply
```

---

### 🔹 3. Connect to EKS

```bash
aws eks update-kubeconfig --region ap-south-1 --name my-eks-cluster
kubectl get nodes
```

---

### 🔹 4. Deploy Application

```bash
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

---

### 🔹 5. Access Application

```bash
kubectl get svc
```

Open the external IP in browser.

---

## 📊 Features

* Microservices architecture
* Containerized deployment
* Automated CI/CD pipeline
* Infrastructure as Code
* Cloud-native deployment on AWS
* Scalable and production-ready design

---

## 💡 Key Learnings

* Hands-on experience with Kubernetes and EKS
* End-to-end CI/CD pipeline implementation
* Terraform-based infrastructure provisioning
* Debugging real-world deployment issues
* IAM & RBAC handling in EKS

---

## 🏆 Resume Highlight

> Built a production-grade microservices application deployed on Kubernetes (EKS) with automated CI/CD pipeline and infrastructure provisioned using Terraform.

---

## 👨‍💻 Author

* UTSAV SHARMA
