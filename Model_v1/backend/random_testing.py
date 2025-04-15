import joblib
import numpy as np

# ✅ Load the trained models
svm_model = joblib.load("../models-&-reports/spam_svm.pkl")
xgb_model = joblib.load("../models-&-reports/spam_xgb.pkl")
vectorizer = joblib.load("../models-&-reports/tfidf_vectorizer.pkl")

# ✅ Define test emails for random checking
test_emails = [
    "Win a free iPhone! Click here to claim your prize now!",
    "Hey John, just checking if you're available for the meeting tomorrow.",
    "Congratulations! You have been selected for a $1000 Walmart gift card.",
    "Let's catch up this weekend for coffee!",
    "URGENT: Your bank account has been compromised! Click the link to secure it."
]

# ✅ Convert emails to TF-IDF features
X_test = vectorizer.transform(test_emails)

# ✅ Predict using SVM & XGBoost
svm_predictions = svm_model.predict(X_test)
xgb_predictions = xgb_model.predict(X_test)

# ✅ Display Results
for i, email in enumerate(test_emails):
    print("📧 Email:", email)
    print("🔍 SVM Prediction:", "Spam" if svm_predictions[i] == 1 else "Ham")
    print("🔥 XGBoost Prediction:", "Spam" if xgb_predictions[i] == 1 else "Ham")
    print("-" * 50)
