from flask import Flask, request, jsonify
from duckduckgo_search import DDGS
app = Flask(__name__)


@app.route('/search')
def search():  # put application's code here
    keywords = request.args.get('q')
    with DDGS() as ddgs:
        results = ddgs.text(keywords, region='cn-zh', safesearch='off', timelimit='y')
        results_list = [dict(item) for item in results]
        return jsonify(results_list)



if __name__ == '__main__':
    app.run(host='0.0.0.0')