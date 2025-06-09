# --------------------------------------------------
# Part 1: Deploy Flask and Express on Single EC2
# --------------------------------------------------

# Step 1: Launch EC2 (Ubuntu 22.04), open ports 22, 3000, 5000

# Step 2: SSH into EC2
ssh -i my-key.pem ubuntu@<EC2_PUBLIC_IP>

# Step 3: Install Required Packages
sudo apt update
sudo apt install python3-pip nodejs npm git -y

# Step 4: Clone App Repositories
git clone https://github.com/yourusername/flask-backend.git
git clone https://github.com/yourusername/express-frontend.git

# Step 5: Install Dependencies
cd flask-backend
pip3 install -r requirements.txt

cd ../express-frontend
npm install

# Step 6: Ensure Flask runs on port 5000 and Express on 3000
# Modify app.py and server.js as needed

# Step 7: Start Apps with PM2
sudo npm install -g pm2

cd ~/flask-backend
pm2 start app.py --name flask-app

cd ~/express-frontend
pm2 start server.js --name express-app

pm2 save
pm2 startup

# Verify:
# - http://<EC2_PUBLIC_IP>:5000 (Flask)
# - http://<EC2_PUBLIC_IP>:3000 (Express)
