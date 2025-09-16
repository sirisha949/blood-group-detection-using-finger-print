
from flask import Flask, request, jsonify, render_template, redirect, url_for, flash, session
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.imagenet_utils import preprocess_input
from flask_pymongo import PyMongo
from werkzeug.security import generate_password_hash, check_password_hash
import numpy as np
import io

app = Flask(__name__)
app.secret_key = 'e3f8a1cd5e5ef9b741c9c3646d2e7acb17b6c9e06dce9850cb2e3163a9f5d470'

# MongoDB config — replace URI with your actual MongoDB connection string
app.config["MONGO_URI"] = "mongodb://localhost:27017/fingerprint_bloodgroup"
mongo = PyMongo(app)
users = mongo.db.users  # users collection

model = load_model("model_blood_group_detection_resnet.keras")
labels = {0: 'A+', 1: 'A-', 2: 'AB+', 3: 'AB-', 4: 'B+', 5: 'B-', 6: 'O+', 7: 'O-'}

@app.route('/')
def index():
    return render_template('index.html')  # serve index.html at root

@app.route('/upload')
def upload():
    return render_template('upload.html')  # serve upload.html at /upload

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        password = request.form.get('password')

        user = users.find_one({'email': email})
        if user and check_password_hash(user['password'], password):
            session['user'] = email
            flash("Logged in successfully!", "success")
            return redirect(url_for('upload'))
        else:
            flash("Invalid email or password", "danger")
            return redirect(url_for('signin'))
    return render_template('signin.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email').lower()
        password = request.form.get('password')

        if users.find_one({'email': email}):
            flash("Email already exists", "warning")
            return redirect(url_for('signup'))

        hashed_password = generate_password_hash(password)
        users.insert_one({'name': name, 'email': email, 'password': hashed_password})

        flash("Account created! Please sign in.", "success")
        return redirect(url_for('signin'))

    return render_template('signup.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        if 'file' not in request.files:
            return jsonify({'error': 'No file uploaded'}), 400

        file = request.files['file']
        if file.filename == '':
            return jsonify({'error': 'No file selected'}), 400

        img_bytes = file.read()
        img_stream = io.BytesIO(img_bytes)

        img = image.load_img(img_stream, target_size=(256, 256), color_mode='rgb')

        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = preprocess_input(x)

        result = model.predict(x)
        predicted_class = np.argmax(result)
        predicted_label = labels[predicted_class]
        confidence = result[0][predicted_class] * 100

        return jsonify({
            'prediction': predicted_label,
            'confidence': f"{confidence:.2f}%"
        })

    except Exception as e:
        print("[ERROR]", e)
        return jsonify({'error': str(e)}), 500

@app.route('/logout')
def logout():
    session.pop('user', None)
    flash("Logged out successfully", "info")
    return redirect(url_for('signin'))


if __name__ == '__main__':
    app.run(debug=True)
