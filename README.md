# DataPy-CI-Pipeline

Simple workshop to gain an introduction to the concepts of Continuous Integration with Python.

## How to install Jenkins?

### Using Docker 

1. Make sure you have [Docker](https://www.docker.com/) installed on the system where you want to run Jenkins. 
2. Run: 

```bash
docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts
```

ℹ️ From the Docker documentation: 

> All Jenkins data lives in the `/var/jenkins_home` workspace; the `-v jenkins_home:/var/jenkins_home` option will
> make `/var/jenkins_home` an explicit volume, so that you can manage it and attach it to another container for 
> upgrades.

3. On the browser, go to [http://localhost:8080](http://localhost:8080)
4. Enter the initial Admin password, that is visible in the terminal console, below:
```bash
Jenkins initial setup is required. An admin user has been created and a password generated.
Please use the following password to proceed to installation:
```
4. Click on: _Install suggested plugins_ and wait for the installation.
5. Create an admin user.
6. Configure the Jenkins URL.
7. Jenkins is ready! 🙌🏼