from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome! Click <a href="/run">here</a> to execute Python code.'

@app.route('/run')
def run():
    result = "Hello I just executed a python script on your browser"
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', port = 5000)