pipeline {
    agent any

    stages {
        stage('Pull data form git') {
            steps {
                git branch: 'master', url: 'https://github.com/SiddhantMisal/jen-prac.git'
            }
        }
        
        stage('Build Image') {
            steps {
                sh 'ls -l'
                sh 'docker build -t siddhant1001/mysid .'
            }
        }
        
        stage('push image') {
            steps {
                sh 'docker push siddhant1001/mysid'
            }
        }

        stage('remove existing service') {
            steps {
                sh 'docker service rm flask2'
            }
        }
        
	stage('creat service') {
            steps {
                sh 'docker service create --name flask2  -p 4000:4000 --replicas 2 siddhant1001/mysid'
            }
        }
    }
}
