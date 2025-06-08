########################################
# CI/CD Deployment Assignment - Bash
# Flask + Express on EC2 with Jenkins
########################################

# -------------------------------
# 1. Update System & Install Dependencies
# -------------------------------
sudo apt update && sudo apt upgrade -y
sudo apt install -y git curl python3-pip nodejs npm openjdk-17-jdk

# -------------------------------
# 2. Install Jenkins
# -------------------------------
curl -fsSL https://pkg.jenkins.io/debian/jenkins.io-2023.key | sudo tee \
  /usr/share/keyrings/jenkins-keyring.asc > /dev/null

echo deb [signed-by=/usr/share/keyrings/jenkins-keyring.asc] \
  https://pkg.jenkins.io/debian binary/ | sudo tee \
  /etc/apt/sources.list.d/jenkins.list > /dev/null

sudo apt update
sudo apt install -y jenkins
sudo systemctl enable jenkins
sudo systemctl start jenkins

# -------------------------------
# 3. Note Jenkins Password
# -------------------------------
sudo cat /var/lib/jenkins/secrets/initialAdminPassword

# -------------------------------
# 4. Install PM2 Globally
# -------------------------------
sudo npm install -g pm2

# -------------------------------
# 5. Clone Project Repository
# -------------------------------
cd ~
git clone https://github.com/AzamCloudOps/aws-Jenkins-pipeline.git
cd aws-Jenkins-pipeline

# -------------------------------
# 6. Setup Backend (Flask)
# -------------------------------
cd backend-flask
pip3 install -r requirements.txt
pm2 start app.py --interpreter python3 --name flask-app

# -------------------------------
# 7. Setup Frontend (Express)
# -------------------------------
cd ../frontend-express
npm install
pm2 start index.js --name express-app

# -------------------------------
# 8. Setup PM2 Startup Script (Optional)
# -------------------------------
pm2 startup systemd
pm2 save

# -------------------------------
# 9. Access Apps in Browser
# -------------------------------
# Flask App  : http://<EC2-PUBLIC-IP>:5000
# Express App: http://<EC2-PUBLIC-IP>:3000

# -------------------------------
# 10. Jenkins Pipelines Configuration (manual in UI)
# -------------------------------
# Job 1: flask-pipeline
#   → Pipeline from SCM
#   → Repo: https://github.com/AzamCloudOps/aws-Jenkins-pipeline.git
#   → Script Path: backend-flask/Jenkinsfile

# Job 2: express-pipeline
#   → Pipeline from SCM
#   → Repo: https://github.com/AzamCloudOps/aws-Jenkins-pipeline.git
#   → Script Path: frontend-express/Jenkinsfile

# -------------------------------
# 11. Setup GitHub Webhook (Optional)
# -------------------------------
# Go to GitHub Repo > Settings > Webhooks > Add Webhook
# URL: http://<EC2-PUBLIC-IP>:8080/github-webhook/
# Content Type: application/json
# Event: Just the push event

# Done ✅
