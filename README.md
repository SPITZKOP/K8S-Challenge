# ToDoList Application

## Introduction
The above represents a simplified form of our a production application and it can give you an idea of what the app looks like in production.

The goal is to create a flask application that implements a very simple todo list. It would have an HTML form that accepts a new todo and displays a list of todos. You can also delete todo.
The todos are persisted in the `postgres-main` database and replicated to `postgres-replica`.

## Implementation
* I developpeted the application with python: "app.py"

* The folder templates contains "index.html".
    
* flask_deployment.yaml contains :
  - the deployment of flask application
  - the service of "flask_application" with type "nodePort", the "port=30000". I use service nodePort fort the test.
  - the deployment of pod running "postgre-main" database.    
  - the deployment of "postgres-replicas" pod related to the main database.
  - the postgres-service
  - "requirement.txt": contains the ependances of the applications: flask and psycopg2-binary
    
* The Dokerfile of application contains : the copy and run of application copy of requirements, the run of dependances
   The application is exposed on port 5000. and the export of environments

## Infrastructure
* cluster EKS

## Deployment
* To deploy the application, I used the command: "apply -f flask_deployment.yaml"
  
* To check the pods, services and deployments :
  - kubectl get pods
  - kubectl get service
  - kubectl get deployment

* To build the application and push it in Docker-Hub:
  - docker build -t flask .
  - docker tag flask:latest ilhemb/flask:v14
  - docker push ilhemb/flask:v14

## Test
* To test tha application in my machine:
  - docker run -p 5000:5000 flask 
  - curl  http://127.0.0.1:5000
  
* To connect to the database locally:
   docker run --name some-postgres -e POSTGRES_PASSWORD=mysecretpassword -d postgres
 
 

