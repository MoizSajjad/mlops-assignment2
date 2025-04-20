# 🚀 MLOps Assignment 2 – Full-Stack Microservices Deployment on Minikube

## 📌 Project Overview

This project demonstrates building and deploying a full-stack microservices application using Docker and Kubernetes (Minikube). The system is composed of a **React frontend**, **Flask backend**, and **PostgreSQL database**, integrated with **JWT-based authentication** (Login, Signup, Forgot Password).

---

## 🧱 Architecture

```
React (Frontend)
   ⬇️ Axios HTTP
Flask (Backend REST API)
   ⬇️ SQLAlchemy ORM
PostgreSQL (Database)
```

All services are containerized using **Docker** and deployed on **Minikube Kubernetes cluster** with **Kubernetes manifests**.

---

## ✅ Features Implemented

- 🔐 User Authentication System:
  - Signup
  - Login
  - Forgot Password (mock email simulation)
- 🐳 Docker Compose multi-container app (fully working)
- ⚙️ Kubernetes YAMLs for:
  - Deployments (3 replicas each)
  - Services
  - ConfigMaps & Secrets

---

## 📁 Folder Structure

```
ML_OPS_Assignment2/
├── backend/
│   └── app/         # Flask app & auth routes
├── frontend/
│   └── src/         # React components (Login, Signup, ForgotPassword)
├── k8s/             # Kubernetes YAMLs
├── docker-compose.yml
└── README.md
```

---

## 🧪 Running Locally with Docker Compose

1. **Navigate to project root:**
   ```bash
   cd ML_OPS_Assignment2
   ```

2. **Run containers:**
   ```bash
   docker-compose up --build
   ```

3. Visit:
   - Frontend: [http://localhost:3000](http://localhost:3000)
   - Backend API: [http://localhost:5000/api/auth](http://localhost:5000/api/auth)

---

## ☸️ Kubernetes Deployment (Minikube)

> Kubernetes manifests are located in the `/k8s` folder.

### 1. Start Minikube
```bash
minikube start
```

### 2. Use Minikube's Docker Daemon
```powershell
& minikube -p minikube docker-env --shell powershell | Invoke-Expression
```

### 3. Build Docker Images inside Minikube
```bash
docker build -t ml_ops_assignemnt2-backend:latest -f backend/Dockerfile ./backend
docker build -t ml_ops_assignemnt2-frontend:latest -f frontend/Dockerfile ./frontend
```

### 4. Apply Kubernetes Manifests
```bash
kubectl apply -f k8s
```

### 5. Access the App
```bash
minikube service frontend
```

---

## ⚠️ Known Issues

- ❌ `ImagePullBackOff` in Kubernetes due to local Docker images not being available to Kubernetes when not built inside Minikube’s Docker environment.
- ✅ Fully functional using Docker Compose.
- 🔄 Kubernetes YAML files created and applied correctly, just need image resolution fix for Minikube pods.

---

## 📚 Technologies Used

- Frontend: React + Axios
- Backend: Flask + SQLAlchemy + JWT
- Database: PostgreSQL
- Docker: Multistage builds
- Kubernetes: Minikube, YAML Deployments, ConfigMaps, Secrets
- OS: Windows 11 with Docker Desktop

---

## 👤 Author

**Muhammad Moiz Sajjad**  


---

## 📜 License

This project is for academic demonstration purposes only.
