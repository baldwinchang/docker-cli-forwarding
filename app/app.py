import os
import requests
from flask import Flask

app = Flask(__name__)

@app.route('/')
def docker_cli_response():
    try:
        request = requests.get("http://localhost:3476/docker/cli")
        return request.text
    except requests.exceptions.Timeout:
        return ''
    except requests.RequestException:
        return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)