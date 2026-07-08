from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>EC2 Deployment Demo</title>
        <style>
            body{
                font-family:Arial;
                background:#f4f4f4;
                text-align:center;
                padding-top:100px;
            }
            .card{
                background:white;
                width:600px;
                margin:auto;
                padding:30px;
                border-radius:10px;
                box-shadow:0 0 15px rgba(0,0,0,0.2);
            }
            h1{
                color:#2c3e50;
            }
            p{
                font-size:18px;
            }
        </style>
    </head>

    <body>

        <div class="card">

            <h1>🚀 Python Application Hosted on Amazon EC2</h1>

            <p><b>Deployment Status:</b> Successful</p>

            <p><b>Platform:</b> Amazon EC2</p>

            <p><b>Deployment Method:</b> VS Code → GitHub → EC2</p>

            <p><b>Region:</b> ap-south-1 (Mumbai)</p>

            <p><b>Web Server:</b> Gunicorn</p>

            <p><b>Framework:</b> Flask</p>

            <p><b>Automation:</b> GitHub Actions CI/CD</p>

            <h3>✅ Application is running successfully!</h3>

        </div>

    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)