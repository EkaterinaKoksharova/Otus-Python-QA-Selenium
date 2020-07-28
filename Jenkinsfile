properties([disableConcurrentBuilds()])

pipeline {
    agent { label 'master' }
    options {
        buildDiscarder(logRotator(numToKeepStr: '10', artifactNumToKeepStr: '10'))
        timestamps()
    }
    stages {
        stage ('Building opencart_test_image') {
            steps {sh 'docker build -t opencart_test_image .'}
        }
//         stage ('Removing opencart_test_container') {
//             steps {sh 'docker rm opencart_test_container'}
//         }
        stage ('Creating opencart_test_container') {
            steps {sh 'docker create --name opencart_test_container -v /logs/allure-log:/logs/allure-results opencart_test_image'}
        }
        stage ('Starting opencart_test_container') {
            steps {sh 'docker start -a opencart_test_container'}
        }
        stage ('Collecting allure report') {
            steps {sh 'ls'}

            post {
                always {
                    script {
                        allure ([
                        includeProperties: false,
                        jdk: '',
                        reportBuildPolicy: 'ALWAYS',
                        report: '/target/allure-report',
                        results: [[path: '/target/allure-results']]])
                    }
                }
            }
        }
    }
}