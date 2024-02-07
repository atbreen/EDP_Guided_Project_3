# server.py
from flask import Flask, request, jsonify
import Guided_Project_3 as gp 
import pandas as pd

app = Flask(__name__)

# TODO:  load dataframe
df = gp.df_trained

@app.route('/api/get_result', methods=['POST'])
def get_result():
    # Retrieve input from the request
    data = request.json

    # get stuff from dataframe
    predictions = data.get('predictions')
    print(predictions)
    result = df[predictions].unique().tolist()
    
    # Return the result as JSON
    return jsonify(result= result)

if __name__ == '__main__':
    app.run(debug=False)
