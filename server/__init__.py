from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS
import shape_detector 

app = Flask(__name__)
api = Api(app)
CORS(app)
# Detect food shape
class Shape(Resource):
    def post(self):

#Regular Flask implementation
app.route('/')

@app.route('/shape', methods=['POST'])
def shape():
    request_json = request.get_json()

    # return ("{}".format(bmr))
    return jsonify(bmr)

# Run
if __name__ == '__main__':
    app.run(use_reloader=True)
