from flask import Flask

app = Flask(__name__)
count = 0

@app.route('/')
def hello_world():
    global count
    count += 1
    return f'Hello, World! Number of requests: {count}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
