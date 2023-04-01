from flask import Flask, request
from flask_ngrok import run_with_ngrok

app = Flask(__name__)
run_with_ngrok(app)

@app.route("/")
def index():
    return "This is the server for upwork API"

@app.route('/callback', methods=['POST'])
def handle_callback():
    # Handle the callback here
    data = request.json
    print(data)
    return 'OK'

if __name__ == '__main__':
    app.run()