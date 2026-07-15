<div align="center">
  <h1>🍃 AI Plant Disease Detection System</h1>
  <p><strong>A Deep Learning-powered web app for real-time plant disease detection.</strong></p>
</div>

---

# 📝 Description
A Flask-based web application that uses TensorFlow/Keras models to accurately identify plant leaf diseases from user-uploaded images, featuring automated background retraining.

---

# 📖 Overview
Upload a plant leaf image to instantly receive AI-based disease predictions. The system uses independently trained models for each crop to maximize accuracy and supports continuous learning.

---

# ✨ Features
- 🌿 Real-time leaf disease prediction
- 🔄 Automated background model retraining
- 🛡️ Smart image validation (blur, blank, and duplicate detection)
- 👥 Secure User and Admin authentication
- 📊 Admin Dashboard for dataset and training management

---

# 🌱 Supported Crops
- 🍅 Tomato
- 🥔 Potato
- 🥭 Mango

---

# 🛠️ Technology Stack
- **Backend:** Python, Flask
- **AI/ML:** TensorFlow, Keras (MobileNetV2), OpenCV, ImageHash
- **Frontend:** HTML5, CSS3, JavaScript

---

# 📁 Project Structure
```text
plant/
│── app.py                 # Main Flask application
│── train.py               # Background training script
│── requirements.txt       # Dependencies
│── app_data/              # Local JSON database
│── crop_datasets/         # Categorized training images
│── models/                # Trained .keras models
│── user_uploads/          # Validated user image uploads
└── templates/             # UI templates
```

---

# 📂 Dataset
Models are trained on publicly available datasets (Kaggle, Mendeley Data). 
Structure: `Crop > Category > Disease/Healthy`.

---

# 🚀 Installation
```bash
git clone https://github.com/nvnpalani/crop-identification.git
cd crop-identification
python -m venv venv

# Windows
venv\Scripts\activate
# Linux / macOS
# source venv/bin/activate

pip install -r requirements.txt
python app.py
```

---

# 💻 Usage
- **User:** Register, upload a leaf image, and view the disease prediction.
- **Admin:** Monitor dataset volume, manage users, and trigger model retraining.

---

# 🧠 AI Workflow
`Upload Image` ➔ `Validation` ➔ `Prediction` ➔ `Store Valid Image` ➔ `Background Retraining` ➔ `Updated Model`

---

# 🚀 Future Enhancements
- Expand support for more crops and fruit diseases.
- Cloud deployment and mobile application integration.

---

# 📌 Note
> Large trained AI models (`.keras`) and original datasets are not included in this repository.

---

# ✍️ Author
**N. V. N. Palani** | [GitHub](https://github.com/nvnpalani)
