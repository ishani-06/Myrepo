pipeline {
    agent any

    stages {

        stage('Run Ansible Playbook') {
            steps {
                sh '''
                cd /home/vagrant/ansible
                ansible-playbook -i inventory.ini deploy.yml
                '''
            }
        }

    }
}