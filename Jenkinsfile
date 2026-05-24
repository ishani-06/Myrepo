pipeline {
    agent any

    stages {

        stage('Deploy') {

            steps {

                sh '''

ssh vagrant@192.168.56.11 << EOF

rm -rf Myrepo

git clone https://github.com/ishani-06/Myrepo.git

cd Myrepo

docker build -t ishanipandaiotcs28/mypythonapp:v1 .

docker push ishanipandaiotcs28/mypythonapp:v1

docker rm -f mycontainer || true

docker run -d -p 8000:8000 \
--name mycontainer \
ishanipandaiotcs28/mypythonapp:v1

EOF

'''
            }
        }
    }
}