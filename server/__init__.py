from flask import Flask, jsonify, request
from flask_restful import Resource, Api
from flask_cors import CORS

from collections import Counter

import cv2
import numpy as np

app = Flask(__name__)
api = Api(app)
CORS(app)

#Regular Flask implementation
app.route('/')

def most_frequent(List):
    occurence_count = Counter(List)
    return occurence_count.most_common(1)[0][0]

@app.route('/shape', methods=['POST'])
def shape():
    file_storage = request.files['file']
    byte_array = file_storage.read()
    # file_storage.save('./assets/lol.png')

    nparr = np.frombuffer(byte_array, np.uint8)
    img_np = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    cv2.imwrite('newImage.png',img_np)

    return 'hi'


# Run
if __name__ == '__main__':
    app.run(use_reloader=True, host='0.0.0.0', port=5001)
