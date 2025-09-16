## 🩸 Blood Group Detection Using Fingerprint (Biometric Health Platform)

📌 **Blood Group Detection Overview**
This project introduces an innovative system that predicts a person’s blood group using biometric data—specifically, their fingerprint. It integrates machine learning with image processing to simplify and accelerate blood group identification, which can be essential in emergency medical scenarios.

📝 **Abstract**
The goal of this project is to develop a cost-effective and contactless method to determine a person’s blood group using fingerprint analysis. By leveraging deep learning models and feature extraction, the system classifies fingerprints into respective blood groups. This helps in critical health cases where rapid and accurate blood group detection is crucial.

🚀 **Features**

* User Authentication System
* Fingerprint Image Upload
* Blood Group Prediction 
* Interactive User Interface
* User-Friendly Interface for Medical Use
* Security Features

🛠️ **Technologies Used**

* **Development Platform:** Python , MangoDM
* **Libraries & Tools:** Flask, keras , TensorFlow , Numpy , PIL
* **Machine Learning Model:** Resnet based CNN


📝 **Installation Steps**

1. **Clone the repository:**

   ```bash
   git clone https://github.com/<your-repo>/Blood_group-detection-using-fingerprint-main.git
   ```
2. **Install dependencies:**

   ```bash
   pip install opencv-python scikit-learn numpy Pillow
   ```
3. **Run the application:**

   ```bash
   python main.py
   ```

📁 **Folder Structure**

```
Blood_group-detection-using-fingerprint-main/
│
├── app.py                           # Main Flask application (routes, API, ML inference, MongoDB)
├── requirements.txt                 # Python dependencies for reproducibility
├── model_blood_group_detection_resnet.keras   # Pre-trained ResNet model for blood group detection
│
├── static/                          # Static assets (CSS, JS, images)
│   └── css/
│       └── style.css                # Custom CSS styles for UI
│
├── templates/                       # Jinja2 HTML templates (rendered by Flask)
│   ├── index.html                   # Homepage
│   ├── signin.html                  # Login page
│   ├── signup.html                  # Registration page
│   └── upload.html                  # Upload fingerprint & show predictions
│
└── README.md                        # Project description 

```

🔬 **Conclusion**
This project demonstrates a practical implementation of biometric blood group prediction using fingerprints. It combines the accuracy of machine learning with the accessibility of image processing tools to create a healthcare aid that can be crucial in emergencies or rural healthcare setups.

