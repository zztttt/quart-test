from quart import Quart

app = Quart(__name__)

@app.route('/hello')
def hello():
    return "hello, zzt"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8001')