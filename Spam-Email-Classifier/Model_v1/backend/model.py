import pandas as pd
import numpy as np
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# ✅ Load Dataset
df = pd.read_csv("../dataset/final_dataset.csv")

# ✅ Fix Column Name Issue
if "label_num" in df.columns:
    df.rename(columns={"label_num": "label"}, inplace=True)

# ✅ Improved TF-IDF Vectorization
vectorizer = TfidfVectorizer(max_features=10000, stop_words='english', ngram_range=(1,2))
X = vectorizer.fit_transform(df["text"])
y = df["label"]

# ✅ Split Data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# ✅ Train SVM Classifier with Better Settings
svm_model = SVC(kernel='linear', C=1.0, probability=True, random_state=42)
svm_model.fit(X_train, y_train)

# ✅ Train XGBoost Classifier with Optimized Parameters
xgb_model = XGBClassifier(n_estimators=300, max_depth=5, learning_rate=0.1, random_state=42)
xgb_model.fit(X_train, y_train)

# ✅ Predictions
y_pred_svm = svm_model.predict(X_test)
y_pred_xgb = xgb_model.predict(X_test)

# ✅ Evaluate
print("📊 SVM Accuracy:", accuracy_score(y_test, y_pred_svm))
print("🔍 SVM Report:\n", classification_report(y_test, y_pred_svm))

print("\n🔥 XGBoost Accuracy:", accuracy_score(y_test, y_pred_xgb))
print("🔍 XGBoost Report:\n", classification_report(y_test, y_pred_xgb))

# ✅ Save Models
joblib.dump(svm_model, "../models-&-reports/spam_svm.pkl")
joblib.dump(xgb_model, "../models-&-reports/spam_xgb.pkl")
joblib.dump(vectorizer, "../models-&-reports/tfidf_vectorizer.pkl")
