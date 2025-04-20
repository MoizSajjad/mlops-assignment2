# MLOps Assignment 2 - Full Stack Microservices App Deployment with Minikube

### 👨‍💻 Author: Muhammad Moiz Sajjad

---

## 📌 Project Overview
This project is developed for **MLOps Assignment 2**. It demonstrates the end-to-end deployment of a full-stack microservices application using:

- **Frontend:** React (Login, Signup, Forgot Password)
- **Backend:** Flask (API & Authentication)
- **Database:** PostgreSQL
- **Authentication:** JWT (JSON Web Tokens)
- **Containerization:** Docker
- **Orchestration:** Kubernetes (Minikube)

---

## 📁 Directory Structure
```
ML_OPS_Assignemnt2/
├── backend/
│   ├── app/                  # Flask app source
│   ├── Dockerfile            # Backend Docker image
│   └── requirements.txt      # Python dependencies
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── Login.jsx
│   │   ├── Signup.jsx
│   │   └── ForgotPassword.jsx
│   └── Dockerfile            # Frontend Docker image
├── k8s/                      # Kubernetes YAML manifests
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   ├── database-deployment.yaml
│   ├── database-service.yaml
│   ├── configmap.yaml
│   └── secrets.yaml
├── docker-compose.yml       # For local testing
├── .env                      # Environment variables (frontend)
└── README.md                 # Project documentation
```

---

## 🚀 Features
- ✅ Signup, Login, and Forgot Password forms (React)
- ✅ JWT-based authentication (Flask)
- ✅ PostgreSQL integration
- ✅ Docker containerization of all services
- ✅ Kubernetes deployment using Minikube

---

## 🛠️ Setup Instructions

### 1. Prerequisites
- Docker Desktop ✅
- Minikube ✅
- kubectl ✅
- VS Code or any code editor

### 2. Run Locally with Docker Compose
```bash
docker-compose up --build
```
Visit: `http://localhost` to access the frontend.

### 3. Deploy on Minikube (Kubernetes)
```powershell
# Point Docker to Minikube daemon
& minikube -p minikube docker-env --shell powershell | Invoke-Expression

# Build images inside Minikube Docker daemon
docker build -t ml_ops_assignemnt2-backend:latest -f backend/Dockerfile ./backend

docker build -t ml_ops_assignemnt2-frontend:latest -f frontend/Dockerfile ./frontend

# Apply Kubernetes configs
kubectl apply -f k8s

# Access frontend via NodePort
minikube service frontend
```

---

## ❌ Known Issues
- Due to environment config issues, `ImagePullBackOff` error may appear if Docker images are not properly built *inside* Minikube context.
- Make sure `docker info` returns `Name: minikube` before building images.

---

## 📫 Submission
GitHub Repo: [https://github.com/MoizSajjad/mlops-assignment2](https://github.com/MoizSajjad/mlops-assignment2)

---

## 📷 Screenshots (Optional)
_Add screenshots here if required by instructor._

---

## ✅ Status
- [x] Authentication System (Login, Signup, Forgot Password)
- [x] Docker Containerization
- [x] Kubernetes Deployment
- [ ] ✅ Pods for frontend/backend not running due to ImagePullBackOff

---

Feel free to fork, improve, or ask questions if you'd like to explore more!
