from flask import Flask, jsonify, url_for, request

app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def hello_world():
    data = request.get_json()

    if request.method == 'POST':
        print('data: ', data)

        return {'status': 200}


if __name__ == '__main__':
    app.run()
