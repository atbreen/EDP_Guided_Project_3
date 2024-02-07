import pickle
import pandas as pd
from flask import Flask, request, jsonify
from sklearn.tree import DecisionTreeClassifier

app = Flask(__name__)

# @app.route('/', methods =["GET", "POST"])

@app.route('/api/predict', methods=['POST'])
def predict():
    print(request.data)
    #data = request.get_json()
    #print(data)

    homeworld = request.form['homeworld']
    unit_type = request.form['unit_type']

    data = [homeworld,unit_type]
    
    with open('../trained_model.pkl', 'rb') as file:
        model = pickle.load(file)
    


    df = pd.DataFrame([data], columns=['homeworld','unit_type'])
    #print(df)
    X_encoded = pd.get_dummies(df[['homeworld','unit_type']])
    #print(X_encoded)
    predict = model.predict(X_encoded)

    print(predict)



    #print()
    #df = pd.DataFrame([[homeworld,unit_type]], columns=['homeworld','unit_type'])
    #X_encoded = pd.get_dummies(df['homeworld','unit_type'])
    #predict = model.predict(df)
    return jsonify({'predicted_values':True})

if __name__ == '__main__':
    app.run(port = 5000)


    #  flask --app server run