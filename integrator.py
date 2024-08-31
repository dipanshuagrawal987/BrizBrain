from flask import Flask, request, jsonify, render_template
import pickle 
import numpy as np

model_path='model.pkl'
with open(model_path,'rb') as file:
    model = pickle.load(file) 
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict',  methods=['POST'])
def predict():
    int_features = [int(x) for x in request.form.values()] 
    final_features = [np.array(int_features)]

    prediction = model.predict(final_features)
    output = prediction[:] 

    return render_template('index.html', prediction_texts ='Prediction:{}'.format(output))

if __name__ == "_main__":
    app.run(debug=True)