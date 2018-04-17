# Demo Application for Containers Immersion Day Presentations

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

`docker build -t ecs-demo:latest .`

### Step 3: Run Docker Image

`docker run -d -p 5000:5000 -e APP_ENV=DOCKER ecs-demo`

## Demo 2 - Introduction to ECR and ECS

TBD

## Demo 3 - Task Placement and Orchestration

TBD

## Demo 4 - Continuous Deployment to ECS

TBD
