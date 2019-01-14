node('docker') {

    stage 'Checkout'
        checkout scm
    state 'Deploy Project'
        sh "(cd ./deployment; ls)"
}