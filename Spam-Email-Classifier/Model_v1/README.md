# 🎯 AI Spam Classifier

**An AI-powered email classifier web app that detects spam using a trained SVM model, featuring a fullstack setup with Next.js frontend and FlaskAPI backend.**


## 🔄 Workflow Overview
📌 The entire workflow follows this structure:
```plaintext
Raw Dataset → Preprocessing → SMOTE Balancing → Model Training → GUI → Next js webapp
```

---

# 📦 About `Model_v1`

## 🔑 Key Features

- ✅ **AI-Powered Spam Detection**  
  Uses a trained **SVM model** with **TF-IDF** and **SMOTE** to classify emails as *Spam* or *Ham* with around **99% accuracy**.

- 🧠 **Cleaned & Balanced Data**  
  The email text is processed using **unigrams and bigrams** with **TF-IDF**, and **SMOTE** helps balance the data for better results.

- 📊 **Model Reports & Results**  
  Includes a **classification report**, **confusion matrix**, and other details to show how well the model performs.

- 🖥️ **Easy-to-Use Web Interface**  
  Built with **Next.js + TypeScript**, the web app has a simple, responsive design with **dark/light mode** and smooth animations.

- 💾 **History Management**  
  Saves all classified emails. You can **delete**, **clear**, or **export** your history as a **CSV** file.

- 🔌 **Full Backend Integration**  
  The backend uses **FastAPI** and **SQLite** to handle predictions and save the history.

- 📁 **Organized Structure**  
  The project is neatly divided into **frontend**, **backend**, **dataset**, and **models-&-reports** for easy understanding and future updates.

- 📬 **Easy Contact Options**  
  Lets users contact the developer via **Gmail**, **Outlook**, or their default email app.


> 🧠 **Model Efficiency on Unseen Data:**  
> While the model performs with **~99% accuracy** on the training data, I believe it is around **80% efficient** when handling **unseen data**. This is because real-world email data often introduces variability that may not have been captured during training.  
>  
> 🔜 **Upcoming Version:**  
> A new version of the model is in development and will be released soon with improved accuracy for better handling of unseen data.
---

# 📁 Project Structure

This project is organized into several main folders, each with a specific role. Below is a brief description of each folder and a link to its detailed README file.

---

## 📊 `dataset/`
This folder contains the **dataset** used for training the machine learning model. It includes the raw data, along with any scripts for cleaning and preprocessing the data.

- 📄 **README**: [dataset/README.md](dataset/README.md) (For detailed instructions on dataset usage and preprocessing steps)

---

## ⚙️ `backend/`
The **backend** folder contains the server-side code responsible for handling API requests, running the model, and managing the data. It is built with **FastAPI** and uses **SQLite** for storing email classification history.

- 📄 **README**: [backend/README.md](backend/README.md) (For detailed instructions on setting up and running the backend)

---

## 🧠 `models-&-reports/`
This folder holds the **trained machine learning model**, vectorizer, and all related evaluation reports and visualizations. The model is used for classifying emails as Spam or Ham.

- 📄 **README**: [models-&-reports/README.md](models-&-reports/README.md) (For detailed instructions on how the model is trained, evaluated, and used)

---

## 🖥️ `frontend/`
The **frontend** folder contains the user interface of the web app built with **Next.js** and **TypeScript**. It allows users to input email text, classify it, view history, and manage the results.

- 📄 **README**: [frontend/README.md](frontend-Next.js/README.md) (For detailed instructions on setting up and running the frontend)

---

## 📁 How to Access Full Project

For complete functionality, it’s recommended to clone the entire project. You can access all folders (dataset, backend, models-&-reports, and frontend) for a fully integrated experience.



## 📦 Setup Instructions

### 1. Clone the Repository

**Complete Model**

```bash
# Clone the repository
git clone https://github.com/chaudhary-hadi27/Model_v1.git
cd Model_v1

# Setup and activate the conda environment for backend
conda env create -f ../environment.yml 
conda activate spam_classification

# Install frontend dependencies
cd frontend-Next.js
npm install

# Go back to backend and start the API server
cd ../backend
python app.py
```
> ✅ Once the backend is running, the frontend will automatically connect to it — no additional configuration is needed.
