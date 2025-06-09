# --------------------------------------
# Part 2: Setup CI/CD with Jenkins
# --------------------------------------

# Step 1: Install Jenkins on EC2
sudo apt update
sudo apt install openjdk-11-jdk -y

wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
echo "deb https://pkg.jenkins.io/debian-stable binary/" | sudo tee /etc/apt/sources.list.d/jenkins.list

sudo apt update
sudo apt install jenkins -y
sudo systemctl start jenkins
sudo systemctl enable jenkins

# Step 2: Access Jenkins Web UI
# URL: http://<EC2_PUBLIC_IP>:8080
sudo cat /var/lib/jenkins/secrets/initialAdminPassword

# Step 3: Install Jenkins Plugins
# - Git Plugin
# - NodeJS Plugin
# - Pipeline Plugin
# - (Optional) ShiningPanda Plugin for Python environments

# Step 4: Jenkinsfile for Flask App (flask-backend/Jenkinsfile)
pipeline {
  agent any
  stages {
    stage('Clone') {
      steps {
        git url: 'https://github.com/yourusername/flask-backend.git'
      }
    }
    stage('Install & Deploy') {
      steps {
        sh 'pip3 install -r requirements.txt'
        sh 'pm2 restart flask-app || pm2 start app.py --name flask-app'
      }
    }
  }
}

# Step 5: Jenkinsfile for Express App (express-frontend/Jenkinsfile)
pipeline {
  agent any
  stages {
    stage('Clone') {
      steps {
        git url: 'https://github.com/yourusername/express-frontend.git'
      }
    }
    stage('Install & Deploy') {
      steps {
        sh 'npm install'
        sh 'pm2 restart express-app || pm2 start server.js --name express-app'
      }
    }
  }
}

# Step 6: Create Jenkins Pipeline Jobs
# Jenkins Dashboard → New Item → Pipeline
# Provide GitHub repository link and use Jenkinsfile

# Step 7: Setup GitHub Webhook
# GitHub → Settings → Webhooks → Add Webhook
# Payload URL: http://<EC2_PUBLIC_IP>:8080/github-webhook/
# Content type: application/json
# Event: Push Events

# Step 8: Test CI/CD Flow
# Push code to GitHub → Jenkins auto-triggers → Deploys with PM2

# Final Check: View PM2 process
pm2 list
