# 🚀 Model Training & Evaluation

A machine learning pipeline for spam email classification using SVM and XGBoost, built with a Flask + Next.js stack.

## 🔄 Workflow Overview

📌 The entire workflow follows this structure:

```plaintext
Raw Dataset → Preprocessing → SMOTE Balancing → Model Training → GUI → Next.js Web App
```

## 📂 Dataset Preparation

- **Dataset File:** [`final_dataset.csv`](dataset/final_dataset.csv)
- The **label column** is renamed (if needed) to ensure consistency.
- We use **TF-IDF Vectorization** to convert text data into numerical features.

## 📊 Feature Extraction with TF-IDF

- Applied `TfidfVectorizer` with **max features = 10,000** and **bigram support (1,2)**.
- Removed stop words to improve model performance.

## 🔥 Model Training

We train two models for comparison:

### 1️⃣ Support Vector Machine (SVM) ✅

- Kernel: `linear`
- Regularization (C): `1.0`
- Probability estimates enabled
- Trained on `80%` of the dataset
- **SVM performs better than XGBoost!** 🎯

### 2️⃣ XGBoost Classifier 

- Estimators: `300`
- Max Depth: `5`
- Learning Rate: `0.1`
- Trained on the same dataset split as SVM

## 📈 Model Evaluation

**File Reference:** [`evaluation_report.py`](evaluation_report.py) 
- **SVM Accuracy:** 📊 `99%` (Good results for real world)
- **XGBoost Accuracy:** 🔥 `99%` (Not good for real world)
- Detailed **Classification Reports** are generated for both models.

## 📊 Saved Reports & Visualization


Evaluation results are saved in the [`models/svm_reports/`](models/svm_reports/) directory:

- 📊 **SVM Confusion Matrix:** ![svm_confusion_matrix.png](../models-%26-reports/svm_reports/svm_confusion_matrix.png)
  - 📜 **SVM Evaluation Report:**
    ```plaintext
      📊 SVM Accuracy: 0.9939
      🔍 SVM Classification Report:
                precision    recall  f1-score   support

             0       1.00      0.99      0.99       735
             1       0.99      1.00      0.99       734

       accuracy                           0.99      1469
       macro avg       0.99      0.99      0.99      1469
    weighted avg       0.99      0.99      0.99      1469
      ```


## 🛠️ Random Testing

We perform random testing on sample emails using the trained models:

**File Reference:** [`random_testing.py`](random_testing.py)

- Example test emails include spam and ham messages.
- The models make predictions using the **TF-IDF vectorizer** and output results.

📝 Sample Predictions:
```plaintext
📧 Email: "Win a free iPhone! Click here to claim your prize now!"
🔍 SVM Prediction: Spam (✅ More accurate)
🔥 XGBoost Prediction: Spam
```

## 💾 Model Saving

All trained models and vectorizers are stored in the [`models/`](models/) directory:

✅ [`spam_svm.pkl`](models/spam_svm.pkl) – **Best Performing Model** 🎯  
✅ [`spam_xgb.pkl`](models/spam_xgb.pkl) – XGBoost Model  
✅ [`tfidf_vectorizer.pkl`](models/tfidf_vectorizer.pkl) – Saved TF-IDF Vectorizer  

# 📝 History Management in Backend
**File Reference:** [`app.py`](app.py)
## 🚀 History Functionalities

After model training and evaluation, we also manage a **history of prompts** in the backend. This functionality ensures that previously used prompts can be stored and accessed for future use. A user-friendly GUI is provided where the user's input and the corresponding responses are saved into the history.

### 1️⃣ Backend API to Save Prompts

The backend uses a **Flask API** to handle storing and retrieving prompts. The `/api/savePrompt` endpoint accepts **POST** requests with a **JSON payload** containing:

- **text**: The prompt's content.
- **classification**: The classification label (e.g., spam/ham).

#### Example of a POST request to save a prompt:

```json
{
  "text": "Your free gift is waiting! Click here now!",
  "classification": "Spam"
}
```



# 🚀 Flask Backend API

This is the **Flask-based backend** for the Spam Email Classifier app.  
It loads a pre-trained SVM model, exposes REST APIs for prediction and database interaction, and also auto-starts a Next.js frontend.

---

## 🔍 Spam Prediction API

- **Endpoint:** `POST /predict`  
- **Accepts:** email `text` in JSON body  
- **Returns:** prediction:
  - `0` = **Ham** (Not Spam)
  - `1` = **Spam**

### 📦 Example Request
```
json :
   POST /predict
{
  "text": "Congratulations! You’ve won a free iPhone."
}
```

# 📤 Example Response
```
json: 
  {
    "prediction": "1"
  }
```
**⚠️ Note: In the frontend, the prediction is shown as:**

- "1" → Spam

- "0" → Ham (Not Spam)

# ✅ Key Features
- ✅ Loads a pre-trained **SVM model** and **TF-IDF vectorizer** to classify emails as spam (`1`) or not spam (`0`).
- ✅ Provides RESTful **API endpoints** to:
  - Predict spam (`/predict`)
  - Save, retrieve, and delete prompts from a local **SQLite database**
- ✅ Automatically **creates the database** and required tables using SQLAlchemy if not already present.
- ✅ Enables **CORS** for cross-origin communication with the frontend.
- ✅ Auto-launches the **Next.js frontend** on server start via a subprocess.

🔧 How to Run

# Start Flask backend and frontend together
```bash
python app.py
```

- Flask Backend will run at: http://127.0.0.1:8000
- Next.js Frontend (auto-launched) runs at: http://localhost:3000

---
