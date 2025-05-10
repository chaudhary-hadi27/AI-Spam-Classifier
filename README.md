# 📬 Spam Email Classifier - ML Pipeline (SVM & XGBoost)

Welcome to the **Spam Email Classification Project**, designed to detect spam emails using state-of-the-art machine learning models.  
This project follows an end-to-end ML pipeline involving **data preprocessing**, **TF-IDF vectorization**, **model training**, and a **full-stack interface** built with **Flask + Next.js**.

---

## 🚀 Current Version: `Model_v1`

Our current stable release is:

- ✅ `Model_v1`: Trained using **SVM** and **XGBoost**
- 🧠 Based on real-world testing, **SVM** shows better generalization and is currently the preferred model.

📘 For complete details about the dataset, training/evaluation, and backend/frontend integration:

➡️ **Check the full documentation here:**  
[`Model_v1/README.md`](Model_v1/README.md)

---

## 📁 Project Structure

```plaintext
📦 Spam-Email-Classifier/
│
├── Model_v1/         # Current working model version (SVM & XGBoost)
│   ├── backend/      # Flask API for model serving
│   ├── frontend/     # Next.js frontend
│   ├── dataset/      # Dataset used for training
│   └── models/       # Saved models and evaluation reports
│
└── README.md         # Main project overview (this file)
