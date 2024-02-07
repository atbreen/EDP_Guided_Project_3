import pickle
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/api/predict', methods=['POST'])
def predict():
    with open('model2.pkl', 'rb') as file:
        model = pickle.load(file)

    data = request.get_json()
    df = pd.DataFrame(data, columns=['homeworld','unit_type'])
    predict = model.predict(df)
    return jsonify({'predicted_values': predict.tolist()})

if __name__ == '__main__':
    app.run(debug=True)