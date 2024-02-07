import pickle
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

# @app.route('/', methods =["GET", "POST"])

@app.route('/api/predict', methods=['GET','POST'])
def predict():
    
    with open('../trained_model.pkl', 'rb') as file:
        model = pickle.load(file)
    
    homeworld = request.form.get("homeworld")
    
    print("hjello server")
    print(homeworld)
    unit_type = request.form.get("unit_type")
    print(unit_type)

    print()
    df = pd.DataFrame(data, columns=['homeworld','unit_type'])
    predict = model.predict(df)
    return jsonify({'predicted_values': predict.tolist()})

if __name__ == '__main__':
    app.run(port = 5000)


    #  flask --app server run