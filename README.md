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

### Step 1: Push Image to ECR

```
aws ecr get-login --no-include-email --region us-west-2
docker tag contaners-demo:latest [YOUR REPO URI]:latest
docker push [YOUR REPO URI]:latest
```
### Step 2: Create ECS Cluster
### Step 3: Create Task Definition
### Step 4: Create Task

## Demo 3 - Task Placement and Orchestration

### Step 1: Delete Task
### Step 2: Create Service
### Step 3: Configure Service Discovery
### Step 4: Show Route 53 Service Registration
### Step 5: Discuss Task Placement (EC2 vs. FARGATE)

## Demo 4 - Continuous Deployment to ECS

### Step 1: Create Deployment Pipeline
### Step 2: Setup GitHub Source
### Step 3: New CodeBuild
* Add Environment Variables(IMAGE_REPO_NAME, AWS_ACCOUNT_ID, AWS_DEFAULT_REGION)
### Step 4: Deploy to EC2
* Use Existing Role or Create New Role
### Step 5: Update CodeBuild Role to add AmazonEC2ContainerRegistryFullAccess Policy
