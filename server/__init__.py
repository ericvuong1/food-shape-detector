from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS

app = Flask(__name__)
api = Api(app)
CORS(app)

#Regular Flask implementation
app.route('/')

@app.route('/shape', methods=['POST'])
def shape():
    print('hi')
    print(request)
    file_storage = request.files['file']
    print(file_storage.filename)
    # file_storage.save('./assets/lol.png')
    return 'Yes'

# Run
if __name__ == '__main__':
    app.run(use_reloader=True, port=5001)
