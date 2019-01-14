node('docker') {

    stage 'Checkout'
        checkout scm
    stage 'Build Test Docker Images'
        sh "docker-compose -f test.yml build"
    stage 'Test Project'
        sh "docker-compose -f test.yml up --force-recreate --abort-on-container-exit"
        sh "docker-compose -f docker-compose.integration.yml down -v"
}