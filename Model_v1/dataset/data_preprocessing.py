import pandas as pd
import re

# 📌 Dataset Load Karna
file_path = "data.csv"
df = pd.read_csv(file_path)

# ✅ Step 1: Unwanted Columns Remove Karna
if "Unnamed: 0" in df.columns:
    df.drop(columns=["Unnamed: 0"], inplace=True)

# ✅ Step 2: Text Cleaning Function
def clean_text(text):
    text = text.lower()  # Convert to lowercase
    text = re.sub(r"http\S+|www\S+|https\S+", "", text, flags=re.MULTILINE)  # URLs remove
    text = re.sub(r"\d+", "", text)  # Numbers remove
    text = re.sub(r"[^\w\s]", "", text)  # Punctuation remove
    return text.strip()

df["text"] = df["text"].astype(str).apply(clean_text)  # Apply Cleaning

# ✅ Step 3: Final Summary
print("\n📌 Cleaned Data Sample:\n", df.head())

# ✅ Step 4: Preprocessed Data Save Karna
df.to_csv("processed_data.csv", index=False)
print("\n✅ Preprocessed data saved as 'dataset/processed_data.csv' ")
