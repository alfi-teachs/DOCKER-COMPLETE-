


# DOC-LAB-7-PYTHON-PROJECT

📁 Project Structure

Create a folder named python-webapp

Inside the folder create these files:

python-webapp/
│

├── app.py

├── requirements.txt

└── Dockerfile

1️⃣ Create app.py

2️⃣ Create requirements.txt
3️⃣ Create Dockerfile
4️⃣ Open VS Code Terminal
5️⃣ Build Docker Image
```bash
docker build -t pythonapp .
```
6️⃣ Run Docker Container
```bash
docker run -d --name py-cont -p 5000:5000 pythonapp
```
Explanation:

-d → run in background

-p 5000:5000 → connect container port to your PC

--name py-cont  → container name

pythonapp → image name you created with docker build

7️⃣ Open Website

Open browser:

```bash
http://localhost:5000
```
You will see:

Welcome to Python Docker Website

Docker is working!

8️⃣ Useful Docker Commands
Check running containers
```bash
docker ps
```
```
docker stop <containerid>
```
Start container again
```bash
docker start mypython
```
Remove container
```bash
docker rm -f mypython
```
Check images
```bash
docker images
```
# What You Learned

Created a Python Flask website

Created Dockerfile

Built Docker image

Ran Docker container

Accessed website in browser





