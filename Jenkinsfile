pipeline {
    agent any

    stages {

        stage('Run Ansible Playbook') {
            steps {
                sh '''
                cd /var/lib/jenkins/ansible
                ansible-playbook -i inventory.ini deploy.yml
                '''
            }
        }

    }
}