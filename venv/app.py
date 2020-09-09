import os
import pandas as pd
from flask import Flask
from flask import abort
from flask import request
from flask_cors import CORS
from flask import jsonify, make_response

# I guess we created a Flask instance globally (?) // jk this created the flask app
# app = Flask(name of current Python module, location for the template)
# template is a text file with static HTML code as well as some special markup denoting dynamic content
app = Flask(__name__, template_folder="templates")

# a simple route so you can see the application working. Creates a connection with URL /price
# not sure where the price function is yet
@app.route('/price')
def portfolio():
    ticker = request.args.get('ticker')

    if ticker is None:
        app.logger.info('tickers not set')
        abort(400)
    # os.path.dirname --> return the diretory name of pathname path
    # ps.path.realpath --> return the canonical path of the specified filename, elimating any symbolic links encountered in the path
    path = '{}/data/{}.csv'.format(os.path.dirname(os.path.realpath(__file__)), ticket)
    df = pd.read_csv(path, index_col = 'Date', parse_dates = True, usecols=['Date', 'Close'], na_values=['nan'])

    port_series = []
    for index, row in df.iterrows():
        port_series.append({'name': index.strftime("%Y-%m-%d"), 'value': df.loc[index, 'Close']})
    
    resp = make_response(jsonify([{'name': ticket, 'series': port_series}]), 200)
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    CORS(app)
    app.run(debug = True)
