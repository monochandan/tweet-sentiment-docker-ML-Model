from flask import Flask, jsonify, request, send_from_directory
from utilities import predict_pipeline
from flask_cors import CORS

app = Flask(__name__)
# enable cors for all routes
CORS(app)

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')

@app.post('/predict')
def predict():
    data = request.get_json()
    try:
        sample = data['text']
    except KeyError:
        return jsonify({'error': 'No text sent'})

    sample = [sample]
    predictions = predict_pipeline(sample)
    # try:
    #     result = jsonify(predictions[0])
    # except TypeError as e:
    #     result = jsonify({'error': str(e)})
    #print(predictions)
    result = jsonify(predictions[0])
    return result

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)