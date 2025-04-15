import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# Load processed data
df = pd.read_csv("processed_data.csv")

# Create "visualizations" folder if not exists
import os
if not os.path.exists("visualizations"):
    os.makedirs("visualizations")

# 📊 Class Distribution
plt.figure(figsize=(6, 4))
sns.countplot(x="label", data=df, palette="viridis")
plt.title("Ham vs Spam Email Distribution")
plt.xlabel("Email Type")
plt.ylabel("Count")
plt.savefig("visualizations/class_distribution.png")  # ✅ Save image
plt.show()

# 📏 Message Length Distribution
df["text_length"] = df["text"].apply(len)
plt.figure(figsize=(8, 5))
sns.histplot(df["text_length"], bins=30, kde=True, color="blue")
plt.title("Distribution of Email Lengths")
plt.xlabel("Message Length")
plt.ylabel("Frequency")
plt.savefig("visualizations/message_length_distribution.png")  # ✅ Save image
plt.show()

# ☁️ Word Cloud for Spam Messages
spam_words = " ".join(df[df["label"] == "spam"]["text"])
spam_wordcloud = WordCloud(width=800, height=400, background_color="black").generate(spam_words)

plt.figure(figsize=(10, 5))
plt.imshow(spam_wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Most Common Words in Spam Emails")
plt.savefig("visualizations/spam_wordcloud.png")  # ✅ Save image
plt.show()
