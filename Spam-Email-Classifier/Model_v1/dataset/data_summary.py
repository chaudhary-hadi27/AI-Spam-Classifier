import pandas as pd

# Dataset Load Karna
file_path = "data.csv"  # File ka path

try:
    df = pd.read_csv(file_path)

    # Summary Print Karna
    print("\n📌 First 5 Rows:\n", df.head())
    print("\n🔍 Dataset Shape:", df.shape)
    print("\n📝 Missing Values:\n", df.isnull().sum())
    print("\n📊 Column Data Types:\n", df.dtypes)



except FileNotFoundError:
    print(f"⚠️ File not found: {file_path}. Please check the path!")
except Exception as e:
    print(f"❌ Error: {e}")
