from flask import Flask, jsonify, url_for, request
from database import get_user_attempt, update_attempt_status
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
    reply_text = json.dumps(data, indent=2)
    reply_text = '<pre>' + reply_text + '</pre>'

    attempt = get_user_attempt(attempt_id)
    method = '/sendMessage'
    url = full_url + method
    params = {'chat_id': attempt['user_tg_id'], 'text': reply_text, 'parse_mode': 'HTML'}
    r = requests.get(url, params=params)
    r = r.json()['ok']

    if r:
        update_attempt_status(attempt_id, 'answered')

    return r


if __name__ == '__main__':
    app.run()
