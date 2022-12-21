from flask import Flask
from flask_cors import CORS
app = Flask(__name__)
CORS(app)
@app.route('/')
def hello():
    return 'Hello, World!'

myData= [{"name":"eli","age":26},{"name":"avi","age":20}]
@app.route('/students')
def students():
    return myData
 
 
if __name__ == '__main__':
    app.run(debug=True)