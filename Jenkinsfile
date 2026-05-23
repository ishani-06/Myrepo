pipeline {
    agent any

    stages {

        stage('Deploy on Docker Server') {

            steps {

                sh '''
ssh vagrant@192.168.56.11 << EOF

rm -rf Myrepo

git clone https://github.com/ishani-06/Myrepo.git

cd Myrepo

docker build -t mypythonapp .

docker rm -f mycontainer || true

docker run --name mycontainer mypythonapp

EOF
                '''
            }
        }
    }
}