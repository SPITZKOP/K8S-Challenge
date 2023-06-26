node {// Jenkins will be able to select all available agents

    stage('Clone repository') 
    { // git clone repo of image stage
        git branch: 'main', url: 'https://github.com/SPITZKOP/K8S-Challenge.git'
    }
    
    stage('Build image') 
    { // docker build image stage
       dockerImage = docker.build("ilhemb/flask:latest")
    }
    
 stage('Push image') 
    {//we pass the built image to our docker hub account
        withDockerRegistry([ credentialsId: "dockerpasswd", url: "" ]) 
        {
        dockerImage.push()
        }
    }    
}
