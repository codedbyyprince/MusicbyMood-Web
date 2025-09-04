from flask import Flask, render_template, request, jsonify
import os
from function import process_image

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect():
    image = request.files['image']
    # Ensure the directory exists
    os.makedirs('static', exist_ok=True)
    image_path = os.path.join('static', 'temp.png')
    image.save(image_path)
    emotion = process_image(image_path)
    if emotion not in ['happy', 'neutral']:
        emotion = 'neutral'
    return jsonify({'emotion': emotion})

if __name__ == '__main__':
    app.run(debug=True)