
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
