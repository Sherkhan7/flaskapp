from flask import Flask, jsonify, url_for, request
from database import get_user_attempt
import requests
from config import full_url
import json

app = Flask(__name__)


@app.route('/api', methods=['GET', 'POST'])
def api_callback():
    if request.method == 'POST':
        data = request.get_json()
        res = send_message(data)

        return jsonify({'ok': res})


def send_message(data):
    attempt_id = data['id']
    result = data['result']
    reply_text = json.dumps(result, indent=2)
    reply_text = '<pre>' + reply_text + '</pre>'

    # attempt = get_user_attempt(attempt_id)
    attempt = dict()
    attempt['user_tg_id'] = 197256155
    method = '/sendMessage'
    url = full_url + method
    params = {'chat_id': attempt['user_tg_id'], 'text': reply_text, 'parse_mode': 'HTML'}
    r = requests.get(url, params=params)

    return r.json()['ok']


if __name__ == '__main__':
    app.run()
