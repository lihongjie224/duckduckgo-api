from flask import Flask, request
from duckduckgo_search import DDGS
app = Flask(__name__)


@app.route('/search')
def search():  # put application's code here
    keywords = request.args.get('q')
    with DDGS() as ddgs:
        results = ddgs.text(keywords, backend='lite')
    print(results)
    return results


if __name__ == '__main__':
    app.run(host='0.0.0.0')