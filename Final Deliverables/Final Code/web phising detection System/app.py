import numpy as np 
from flask import Flask, request, jsonify, render_template 
import pickle #importing the inputScript file used to analyze the URL 
import InputScript
#Redirects to the page to give the user iput URL. @app.route('/predict')
app=Flask(__name__) 
model = pickle.load(open('Phishing_website.pkl', 'rb'))
@app.route('/',methods=['POST','GET'])
def predict(): 
  return render_template('index.html')
#Fetches the URL given by the URL and passes to inputScript
@app.route('/y_predict', methods=['POST','GET'])
def y_predict(): 
  url = request.form['URL']
  checkprediction = InputScript.main(url)
  print(checkprediction)
  prediction = model.predict(checkprediction)
  print(prediction)
  output=prediction [0]
  print(output)
  if(output==1): 
    pred="safe"
    print(pred)
  else:
    pred=" not safe" 
    print(pred)
  print(pred)
  return render_template('index.html', prediction_text='{}'.format(pred), url=url)
@app.route('/predict_api', methods=['POST'])
def predict_api():
#Takes the input parameters fetched from the URL by inputScript and returns the predictions 
  data = request.get_json(force=True)
  prediction = model.y_predict ( [np.array(list(data.values()))])
  output=prediction[0]  
  return jsonify (output)

if __name__== '__main__': 
  app.run(host='0.0.0.0', debug=True)
