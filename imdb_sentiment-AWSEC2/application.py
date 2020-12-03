from flask import Flask
from flask import request, jsonify,render_template

import numpy as np

from flask_cors import CORS

app = Flask(__name__,static_folder='static',template_folder='templates')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

import model

@app.route('/',methods=['POST','GET'])
def main():
  if(request.method=='GET'):
    return render_template('sentiment.php')

@app.route('/predict',methods=['POST','GET'])
def predict():
    if request.method == "POST":
        #data = request.form.get('input') works if u give data as form
        data = request.json.get('input')
        pred, p, n = model.predict("posiwords.txt", "negawords.txt", "allwords.txt", data)
        return str(pred)
    else:
        return "No review available"


if __name__=='__main__':
  # We need to run the app to run the server
  app.run(host='0.0.0.0',port=8080) #use this command when deployed on ec2
  #app.run(debug=False)

