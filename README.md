# 📬 Spam Email Classifier - ML Pipeline (SVM & XGBoost)

Welcome to the **Spam Email Classification Project**, designed to detect spam emails using state-of-the-art machine learning models.
This project follows an end-to-end ML pipeline involving **data preprocessing**, **TF-IDF vectorization**, **model training**, and a **full-stack interface** built with **Flask + Next.js**.

---

## 🚀 Current Version: `Model_v1`

Our current stable release is:

* ✅ `Model_v1`: Trained using **SVM** and **XGBoost**
* 🧠 Based on real-world testing, **SVM** shows better generalization and is currently the preferred model.

📘 For complete details about the dataset, training/evaluation, and backend/frontend integration:

➡️ **Check the full documentation here:**
[`Model_v1/README.md`](Model_v1/README.md)

---

## 📊 SVM Model Results

Here are some sample results from the **SVM classifier**:

![SVM Results](Model_v1/models/svm_results.png)

These results demonstrate the **high accuracy** and **balanced precision-recall** achieved in spam detection.

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
```

---

## 🖥️ Run This Model Locally

Follow these steps to set up and run **Spam Email Classifier - Model\_v1** on your machine.

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/<your-username>/Spam-Email-Classifier.git
cd Spam-Email-Classifier
```

---

### 2️⃣ Set Up the Environment

We provide a ready-to-use **`environment.yml`** for `conda`.

```bash
conda env create -f environment.yml
conda activate ai-spam-classifier-v1
```

`environment.yml`:

```yaml
name: ai-spam-classifier-v1
channels:
  - defaults
  - conda-forge
dependencies:
  - python=3.10
  - flask=3.1.0
  - ipynb=0.5.1
  - flask-sqlalchemy=3.1.1
  - flask-cors=3.0.10
  - imbalanced-learn=0.13.0
  - joblib=1.4.2
  - matplotlib=3.10.0
  - numpy=1.26.4
  - pandas=2.2.3
  - seaborn=0.13.2
  - scikit-learn=1.6.0
  - wordcloud=1.9.4
  - xgboost=3.0.0
```

---

### 3️⃣ Start the Backend (Flask API)

Navigate to the backend folder and start the API server:

```bash
cd Model_v1/backend
python app.py
```

* The backend will start on **`http://127.0.0.1:5000`** by default.

---

### 4️⃣ Start the Frontend (Next.js UI)

Open a new terminal, navigate to the frontend folder, and run:

```bash
cd Model_v1/frontend
npm install
npm run dev
```

* The frontend will start on **`http://localhost:3000`**.

---

### 5️⃣ Access the App

Open your browser and go to:

🔗 **[http://localhost:3000](http://localhost:3000)**

Here, you can:

* Upload email text
* Classify it as **Spam** or **Not Spam**
* View probability scores

---

### ⚡ Quick Recap

```plaintext
conda env create -f environment.yml
conda activate ai-spam-classifier-v1
# Start Backend
cd Model_v1/backend && python app.py
# Start Frontend
cd Model_v1/frontend && npm install && npm run dev
```

---

## 💡 Notes

* **Preferred Model:** SVM (better generalization in testing)
* **Frontend Tech:** Next.js
* **Backend Tech:** Flask API
* **Dataset:** Preprocessed with TF-IDF

---

## 📚 License

This project is released under the MIT License.
