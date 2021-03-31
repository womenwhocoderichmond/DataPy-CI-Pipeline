# DataPy-CI-Pipeline

Simple workshop to gain an introduction to the concepts of Continuous Integration with Python.

 🎥 Recording of the workshop is [here](https://www.youtube.com/watch?v=0pfRRYza2yQ).

## How to install Jenkins?

### Using Docker 

1. Make sure you have [Docker](https://www.docker.com/) installed on the system where you want to run Jenkins. 
2. Run:
```bash
docker-compose up
```
⚠️ Do not use this [docker-compose.yml](docker-compose.yml) file for production implementations, since the docker  
container us running in _privileged_ mode 😱 This file is only meant for local development and practical purposes.

3. On the browser, go to [http://localhost:8080](http://localhost:8080)
4. Enter the initial Admin password, that is visible in the terminal console, below:
```bash
Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:
```
5. Click on: _Install suggested plugins_ and wait for the installation.
6. Create an admin user.
7. Configure the Jenkins URL.
8. Jenkins is ready! 🙌🏼

## Pipeline setup 

Since, the `docker` agent is used as part of the [Jenkinsfile](Jenkinsfile) of this project, you will need to 
install the following plugins, in the Plugin Manager [http://localhost:8080/pluginManager/](http://localhost:8080/pluginManager/):

1. [Docker](https://plugins.jenkins.io/docker-plugin/)
2. [Docker Pipeline](https://plugins.jenkins.io/docker-workflow/)
