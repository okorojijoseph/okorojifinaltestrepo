from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_cloud():
  return "Welcome to Okoroji Final Test API Server".

app.run(host='0.0.0.0')
