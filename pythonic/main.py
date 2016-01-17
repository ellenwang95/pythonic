from pythonic import app
from flask import render_template, url_for, jsonify, make_response, request
from parse import pythonic_parse
import os

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

# parse api 
@app.route('/pythonic/api/parse', methods=['POST'])
def parse_code():
    code = {
    	'code': request.json['code'],
    	'date': request.json['date'],
    	'parsed': False
    }

    code['code'] = pythonic_parse(code['code']);

    return jsonify({'parsed': code}), 201


# to avoid caching css files
# taken from: http://flask.pocoo.org/snippets/40/
@app.context_processor
def override_url_for():
    return dict(url_for=dated_url_for)

def dated_url_for(endpoint, **values):
    if endpoint == 'static':
        filename = values.get('filename', None)
        if filename:
            file_path = os.path.join(app.root_path,
                                     endpoint, filename)
            values['q'] = int(os.stat(file_path).st_mtime)
    return url_for(endpoint, **values)


