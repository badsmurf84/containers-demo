# Demo Application for Containers Immersion Day Presentations

## Run App Locally

```
export APP_ENV=LOCAL
FLASK_APP=application.py flask run
```

## Prerequisites

### Install Mu: https://github.com/stelligent/mu

```
curl -s https://getmu.io/install.sh | sudo sh
```

### Launch Mu Pipeline

```
mu pipeline up
```

### Confirm Deployment Through Prod

```
mu svc show
```
* Will require a manual approval in CodePipeline

## Demos

* Demo 1 - Introduction to Images and Containers
* Demo 2 - Introduction to ECR and ECS
* Demo 3 - Task Placement and Orchestration
* Demo 4 - Continuous Deployment to ECS

## Demo 1 - Introduction to Images and Containers

### Step 1: Review Files

* Dockerfile
* .dockerignore

### Step 2: Build Docker Image

```
docker build -t containers-demo:latest .
```

### Step 3: Run Docker Image

```
docker run -d -p 5000:5000 -e APP_ENV=DOCKER containers-demo
```
* Browse to application: http://localhost:5000

## Demo 2 - Introduction to ECR and ECS

* Environment Walkthrough
* Container Images (ECR)
* Task Definitions
* Services
* Launch Types: FARGATE vs EC2

## Demo 3 - Task Placement and Orchestration

* Placement Constraints
* Task Placement (Placement Templates)
* ECS vs FARGATE differences

## Demo 4 - Continuous Deployment to ECS

* Mu Overview
* Update File

```
git add .
git commit -m "Demo Update"
git push -u origin master
```
