from imblearn.over_sampling import SMOTE
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

# Load dataset
df = pd.read_csv("processed_data.csv")

X = df["text"]  # Text column
y = df["label_num"]  # Labels

# Convert text to numerical features using TF-IDF
vectorizer = TfidfVectorizer()
X_tfidf = vectorizer.fit_transform(X)

# Apply SMOTE on numerical data
smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_tfidf, y)

# Convert back to DataFrame
df_balanced = pd.DataFrame({
    "text": vectorizer.inverse_transform(X_resampled),  # Convert back to words
    "label_num": y_resampled
})

# Save the balanced data
df_balanced.to_csv("smote_balanced_data.csv", index=False)

# Check distribution
print("✅ Balanced Data Distribution:")
print(df_balanced["label_num"].value_counts())
