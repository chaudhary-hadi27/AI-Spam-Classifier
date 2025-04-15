import pandas as pd
import re
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud
import os

# -------------------------------
# 1. Load the dataset
# -------------------------------
df = pd.read_csv("smote_balanced_data.csv")

# -------------------------------
# 2. Clean the text column using regex
# -------------------------------
def clean_text(text):
    # Extract words enclosed in single quotes using regex
    words = re.findall(r"'(.*?)'", text)
    if words:
        return " ".join(words)  # Join the words with a space
    else:
        return text  # If no quotes found, return the original text

# Apply cleaning to the text column
df["text"] = df["text"].apply(clean_text)

# -------------------------------
# 3. Remove duplicate text rows
# -------------------------------
before = df.shape[0]
df = df.drop_duplicates(subset="text")
after = df.shape[0]

print(f"\n✅ Removed {before - after} duplicate rows based on 'text' column.")
print(f"🔢 Remaining rows after duplicate removal: {after}")

# -------------------------------
# 4. Save the cleaned and de-duplicated dataset
# -------------------------------
cleaned_path = "final_dataset.csv"
df.to_csv(cleaned_path, index=False)
print("✅ Data cleaned, duplicates removed, and saved successfully!")

# -------------------------------
# 5. Data Summary
# -------------------------------
print("\n🔍 Checking first 5 rows:")
print(df.head())

print("\n🔍 Checking middle 5 rows:")
middle_start = len(df) // 2 - 2
middle_end = middle_start + 5
print(df.iloc[middle_start:middle_end])

print("\n🔍 Checking last 5 rows:")
print(df.tail())

print("\n📐 Dataset Shape:", df.shape)
print("\n🚫 Missing Values:")
print(df.isnull().sum())

print("\n📊 Label Distribution:")
print(df["label_num"].value_counts())

# -------------------------------
# 6. Visualizations
# -------------------------------

# Create folder for visualizations if it doesn't exist
viz_folder = "final_data_visualizations"
if not os.path.exists(viz_folder):
    os.makedirs(viz_folder)

# 6.1. Plot label distribution
plt.figure(figsize=(6, 4))
sns.countplot(x="label_num", data=df, palette="viridis")
plt.title("Label Distribution")
plt.xlabel("Label (0 = Ham, 1 = Spam)")
plt.ylabel("Count")
label_dist_path = os.path.join(viz_folder, "label_distribution.png")
plt.savefig(label_dist_path)
plt.show()

# 6.2. Plot text length distribution
df["text_length"] = df["text"].apply(len)
plt.figure(figsize=(8, 5))
sns.histplot(df["text_length"], bins=30, kde=True, color="blue")
plt.title("Text Length Distribution")
plt.xlabel("Text Length (characters)")
plt.ylabel("Frequency")
text_length_path = os.path.join(viz_folder, "text_length_distribution.png")
plt.savefig(text_length_path)
plt.show()

# 6.3. Generate a word cloud for spam emails (label 1)
spam_text = " ".join(df[df["label_num"] == 1]["text"])
wordcloud = WordCloud(width=800, height=400, background_color="black").generate(spam_text)
plt.figure(figsize=(10, 5))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud for Spam Emails (Label 1)")
wordcloud_path = os.path.join(viz_folder, "spam_wordcloud.png")
plt.savefig(wordcloud_path)
plt.show()

print("✅ Visualizations saved in folder:", viz_folder)
