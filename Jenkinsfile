node('docker') {

    stage 'Checkout'
        checkout scm
    stage 'Build Test Docker Images'
        sh "docker-compose -f test.yml build"
    stage 'Deploy'
        sh "(cd deployment; ./deploy.sh)"
}