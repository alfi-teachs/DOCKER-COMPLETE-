


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
```bash

from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>Python Docker Website</title>
        <style>
            body {
                margin: 0;
                font-family: Arial, sans-serif;
                background: linear-gradient(to right, #4facfe, #00f2fe);
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
            }

            .container {
                background: white;
                padding: 40px;
                border-radius: 20px;
                text-align: center;
                box-shadow: 0 10px 30px rgba(0,0,0,0.2);
                width: 400px;
            }

            h1 {
                color: #0077ff;
                font-size: 36px;
            }

            p {
                color: #444;
                font-size: 20px;
            }

            button {
                background: #0077ff;
                color: white;
                border: none;
                padding: 12px 25px;
                font-size: 18px;
                border-radius: 10px;
                cursor: pointer;
                margin-top: 20px;
            }

            button:hover {
                background: #0056cc;
            }
        </style>
    </head>
    <body>
        <div class='container'>
            <h1>Python Docker Website</h1>
            <p>Docker Container is Running Successfully 🚀</p>
            <button>Welcome</button>
        </div>
    </body>
    </html>
    """

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
```

2️⃣ Create requirements.txt

```bash
flask
```
3️⃣ Create Dockerfile
```bash

FROM python:3.11

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD ["python", "app.py"]

```
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





