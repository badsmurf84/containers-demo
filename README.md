# Demo Application for Containers Immersion Day Presentations

# Update

## Prerequisites

### Repo

* Fork Repo (If you want to test CI/CD)
* Clone Repo Locally

### OAuth Token

* https://github.com/stelligent/devops-essentials/wiki/Prerequisites#create-an-oauth-token-in-github

### Install Mu: https://github.com/stelligent/mu

```
curl -s https://getmu.io/install.sh | sudo sh
```

### Install Flask (Assumes working Python Installation):

```
pip install -r requirements.txt
```

## Install Docker

http://www.docker.com

### Update mu.yml

```
environments:
  - name: acceptance
    provider: ecs-fargate
  - name: production
    provider: ecs-fargate
service:
  port: 5000
  healthEndpoint: /
  pathPatterns:
  - /*
  environment:
    APP_ENV: ECS
  pipeline:
    source:
      provider: GitHub
      repo: you/your-repo
    build:
      disabled: false
    notify:
      - you@email.com
```

### Launch Mu Pipeline

```
mu -r us-east-1 pipeline up
```

### Confirm Deployment Through Prod

```
mu -r us-east-1 svc show
```
* Will require a manual approval in CodePipeline

## Demos

* Demo 1 - Introduction to Images and Containers
* Demo 2 - Introduction to ECR and ECS
* Demo 3 - Task Placement and Orchestration
* Demo 4 - Continuous Deployment to ECS

## Demo 1 - Introduction to Images and Containers

## Step 1: Run Application Locally

```
export APP_ENV=LOCAL
FLASK_APP=application.py flask run
```

### Step 2: Review Files

* Dockerfile
* .dockerignore

### Step 3: Build Docker Image

```
docker build -t containers-demo:latest .
```

### Step 4: Run Docker Image

```
docker run -d -p 5000:5000 -e APP_ENV=DOCKER containers-demo
```
* Browse to application: http://localhost:5000

## Demo 2 - Introduction to ECR and ECS

* Environment Walkthrough
* Container Images (ECR)

```
aws ecr describe-images --repository-name mu-containers-demo --region us-east-1
```

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
