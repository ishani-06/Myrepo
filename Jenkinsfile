pipeline {
    agent any

    stages {

        stage('Run Ansible Playbook') {
            steps {

                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {

                    sh '''
                    cd /var/lib/jenkins/ansible
                    ansible-playbook -i inventory.ini deploy.yml \
                    --extra-vars "docker_username=$USER docker_password=$PASS"
                    '''
                }
            }
        }

    }
}