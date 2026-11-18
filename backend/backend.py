import requests
from flask import Flask

app = Flask(__name__)


@app.route("/cat_get")
def hello_world():
    try:
        resp = requests.get(
            'https://api.thecatapi.com/v1/images/search',
            timeout=3
        )
        cat_json = resp.json()
        if cat_json and len(cat_json) > 0:
            return cat_json[0].get('url', '')
    except Exception as e:
        print(f"API Error: {e}")
    return ''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3001)
