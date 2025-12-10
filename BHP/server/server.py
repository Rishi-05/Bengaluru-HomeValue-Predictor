from flask import Flask, request, jsonify
import util
import warnings
warnings.filterwarnings("ignore")

app = Flask(__name__)

@app.route('/')
def hello():
    return 'hello'

@app.route('/loc')
def get_loc_name():
    response = jsonify({
        'location': util.get_loc_name()
    })
    response.headers.add('Access-Control-Allow-Origin','*')
    return response

@app.route('/home_price', methods=['POST'])
def pred_home_price():
    total_sqft = float(request.form['total_sqft'])
    location = request.form['location']
    bhk = int(request.form['bhk'])
    bath = int(request.form['bath'])

    response = jsonify({
        'estimated_price' : util.get_estimated_price(location, total_sqft, bhk, bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

if __name__ == '__main__':
    print('something is cooking over there.')
    app.run(debug=True)


































# flask is python web framework
from flask import Flask, request, jsonify
app = Flask(__name__)

@app.route('/')
def hello():
    return 'hi'

if __name__=='__main__': # ENTRY POINT OF A PROGRAM
    print('starting python flask server for house price prediction')
    app.run(debug=True)