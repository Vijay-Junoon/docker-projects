# Docker Projects Repository 🐳

A collection of Docker projects created while learning and practicing containerization, image creation, application deployment, and DevOps fundamentals.

## About

This repository contains various projects that have been containerized using Docker. The goal is to understand Docker concepts through hands-on implementation, including:

- Creating Docker images
- Writing Dockerfiles
- Managing containers
- Working with Python applications in Docker
- Using Docker networking and volumes
- Multi-container applications
- Docker Compose
- Containerized development workflows

## Repository Structure

```text
docker-projects/
│
├── docker-01/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── my_app.py
|   └── README.md
│
├── docker-02/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── game.py
|   └── README.md
|
└── README.md
```

## Projects

### 1. Flask Application

A basic Flask web application running inside a Docker container.

#### Concepts Practiced

- Web application containerization
- Port mapping
- Environment configuration

### 2. Python Game

A simple Python application containerized using Docker.

#### Concepts Practiced

- Dockerfile creation
- Python dependency management
- Building and running Docker images


## Prerequisites

- Docker Desktop or Docker Engine
- Git
- Basic knowledge of Python and command line

## Common Docker Commands

### Build an Image

```bash
docker build -t image-name .
```

### Run a Container

```bash
docker run image-name
```

### Run a Container with Port Mapping

```bash
docker run -p 5000:5000 image-name
```

### List Running Containers

```bash
docker ps
```

### List Docker Images

```bash
docker images
```

### Stop a Container

```bash
docker stop <container-id>
```

## Learning Objectives

Through these projects, I am exploring:

- Docker fundamentals
- Container lifecycle management
- Image optimization
- Docker Compose
- Networking and volumes
- Application deployment
- DevOps best practices
- MLOps integration with Docker

## Future Additions

- Flask + MySQL application
- Docker Compose projects
- ML model deployment with Flask
- Airflow in Docker
- MLflow integration
- End-to-End MLOps pipelines
- CI/CD with GitHub Actions and Docker

## Author

**V Vijay**

Passionate about Software Development, Machine Learning, MLOps, and DevOps.

## License

This repository is intended for learning and educational purposes.
