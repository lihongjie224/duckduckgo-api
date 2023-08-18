from flask import Flask, request, jsonify
from duckduckgo_search import DDGS
app = Flask(__name__)

@app.route('/search')
def search():  # put application's code here
    keywords = request.args.get('q')
    limit = int(request.args.get('limit', 10))  # 新增一个参数limit,默认值为10
    region = request.args.get('region', 'cn-zh')  # 新增一个参数region,默认值为'cn-zh'
    backend = request.args.get('backend', 'api')  # 新增一个参数backend,默认值为'api'
    with DDGS() as ddgs:
        results = ddgs.text(keywords, region=region, safesearch='off', timelimit='y', backend=backend)  # 使用新的参数替换原来的参数
        results_list = [dict(item) for item in results][:limit]  # 限制results_list的条数
        return jsonify(results_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0')