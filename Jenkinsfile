pipeline {
environment { // Declaration of environment variables
DOCKER_ID = "ilhemb" // replace this with your docker-id
DOCKER_IMAGE = "flask"
DOCKER_TAG = "v.${BUILD_ID}.0" // we will tag our images with the current build in order to increment the value by 1 with each new build
}
agent any // Jenkins will be able to select all available agents
stages {  
    stage('Clone repository') 
    { // git clone repo of image stage
        git credentialsId: '', url: 'https://github.com/SPITZKOP/K8S-Challenge'
    }
    
    stage('Build image') 
    { // docker build image stage
       dockerImage = docker.build("ilhemb/flask")
    }
    
 stage('Push image') 
    {//we pass the built image to our docker hub account
        withDockerRegistry([ credentialsId: "DOCKER_HUB_PASS", url: "" ]) 
        {
        dockerImage.push()
        }
    }    
}
}