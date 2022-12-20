from flask import Flask
from flask_cors import CORS
api = Flask(__name__)
CORS(api)
@api.route('/')
def hello():
    return 'Hello, World!'

myData= [{"name":"eli","age":26},{"name":"avi","age":20}]
@api.route('/students')
def students():
    return myData
 
 
if __name__ == '__main__':
    api.run(debug=True)