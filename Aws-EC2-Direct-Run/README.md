# -----------------------------
# Step 1: Update & Install Dependencies
# -----------------------------

sudo apt update -y
sudo apt install -y python3 python3-pip git

# Node.js 18 Installation
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
sudo apt install -y nodejs

# Install PM2 globally
sudo npm install -g pm2

# -----------------------------
# Step 2: Clone Your Project Repo
# -----------------------------

cd ~
git clone https://github.com/AzamCloudOps/aws-Jenkins-pipeline.git
cd aws-Jenkins-pipeline

# -----------------------------
# Step 3: Setup Flask App
# -----------------------------

cd backend-flask
pip3 install -r requirements.txt

# Start Flask app on port 5000 using PM2
pm2 start app.py --interpreter python3 --name flask-app

# -----------------------------
# Step 4: Setup Express App
# -----------------------------

cd ../frontend-express
npm install

# Start Express app on port 3000 using PM2
pm2 start index.js --name express-app

# -----------------------------
# Step 5: Enable PM2 on Boot
# -----------------------------

pm2 startup
# Follow the instructions shown (usually a sudo command like "sudo env PATH=... pm2 startup systemd -u ubuntu --hp /home/ubuntu")

pm2 save

# -----------------------------
# Step 6: Check Apps
# -----------------------------

pm2 list
pm2 logs

# -----------------------------
# Access in Browser:
# Flask App:    http://<Your-EC2-IP>:5000
# Express App:  http://<Your-EC2-IP>:3000
# -----------------------------
