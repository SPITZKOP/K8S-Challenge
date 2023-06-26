agent any // Jenkins will be able to select all available agents
stages {  
    stage('Clone repository') 
    { // git clone repo of image stage
        git url: 'https://github.com/SPITZKOP/K8S-Challenge'
    }
    
    stage('Build image') 
    { // docker build image stage
       dockerImage = docker.build("ilhemb/flask:latest")
    }
    
 stage('Push image') 
    {//we pass the built image to our docker hub account
        withDockerRegistry([ credentialsId: "DOCKER_HUB_PASS", url: "" ]) 
        {
        dockerImage.push()
        }
    }    
}
