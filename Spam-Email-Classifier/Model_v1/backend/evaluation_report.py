import os
import joblib
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# ── Base directory of this file (e.g., backend/) ─────────────────────────────
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# ── Relative Paths ──────────────────────────────────────────────────────────
DATASET_PATH = os.path.join(BASE_DIR, "..", "dataset", "final_dataset.csv")
VECTORIZER_PATH = os.path.join(BASE_DIR, "..", "models-&-reports", "tfidf_vectorizer.pkl")
SVM_MODEL_PATH = os.path.join(BASE_DIR, "..", "models-&-reports", "spam_svm.pkl")
XGB_MODEL_PATH = os.path.join(BASE_DIR, "..", "models-&-reports", "spam_xgb.pkl")

SVM_REPORT_DIR = os.path.join(BASE_DIR, "..", "models-&-reports", "svm_reports")
os.makedirs(SVM_REPORT_DIR, exist_ok=True)

SVM_REPORT_PATH = os.path.join(SVM_REPORT_DIR, "svm_evaluation_report.txt")
SVM_MATRIX_PATH = os.path.join(SVM_REPORT_DIR, "svm_confusion_matrix.png")
XGB_REPORT_PATH = os.path.join(SVM_REPORT_DIR, "xgb_evaluation_report.txt")
XGB_MATRIX_PATH = os.path.join(SVM_REPORT_DIR, "xgb_confusion_matrix.png")

# ── Load Dataset ────────────────────────────────────────────────────────────
df = pd.read_csv(DATASET_PATH)

# ✅ Fix Column Name if needed
if "label_num" in df.columns:
    df.rename(columns={"label_num": "label"}, inplace=True)

# ── Load TF-IDF Vectorizer and Transform Data ───────────────────────────────
vectorizer = joblib.load(VECTORIZER_PATH)
X = vectorizer.transform(df["text"])
y = df["label"]

# ── Train/Test Split ────────────────────────────────────────────────────────
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ========== SVM Evaluation ==========
svm_model = joblib.load(SVM_MODEL_PATH)
svm_pred = svm_model.predict(X_test)

svm_accuracy = accuracy_score(y_test, svm_pred)
svm_report = classification_report(y_test, svm_pred)
svm_conf_matrix = confusion_matrix(y_test, svm_pred)

with open(SVM_REPORT_PATH, "w") as f:
    f.write(f"📊 SVM Accuracy: {svm_accuracy:.4f}\n\n")
    f.write("🔍 SVM Classification Report:\n")
    f.write(svm_report + "\n")
print(f"✅ SVM Report saved at: {SVM_REPORT_PATH}")

plt.figure(figsize=(6, 5))
sns.heatmap(svm_conf_matrix, annot=True, fmt='d', cmap="Blues", xticklabels=["Ham", "Spam"], yticklabels=["Ham", "Spam"])
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("📉 SVM Confusion Matrix")
plt.savefig(SVM_MATRIX_PATH, dpi=300)
plt.close()
print(f"✅ SVM Confusion Matrix saved at: {SVM_MATRIX_PATH}")

# ========== XGBoost Evaluation ==========
xgb_model = joblib.load(XGB_MODEL_PATH)
xgb_pred = xgb_model.predict(X_test)

xgb_accuracy = accuracy_score(y_test, xgb_pred)
xgb_report = classification_report(y_test, xgb_pred)
xgb_conf_matrix = confusion_matrix(y_test, xgb_pred)

with open(XGB_REPORT_PATH, "w") as f:
    f.write(f"📊 XGBoost Accuracy: {xgb_accuracy:.4f}\n\n")
    f.write("🔍 XGBoost Classification Report:\n")
    f.write(xgb_report + "\n")
print(f"✅ XGBoost Report saved at: {XGB_REPORT_PATH}")

plt.figure(figsize=(6, 5))
sns.heatmap(xgb_conf_matrix, annot=True, fmt='d', cmap="Greens", xticklabels=["Ham", "Spam"], yticklabels=["Ham", "Spam"])
plt.xlabel("Predicted Labels")
plt.ylabel("True Labels")
plt.title("📉 XGBoost Confusion Matrix")
plt.savefig(XGB_MATRIX_PATH, dpi=300)
plt.close()
print(f"✅ XGBoost Confusion Matrix saved at: {XGB_MATRIX_PATH}")
