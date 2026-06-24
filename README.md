# 💳 Credit Card Fraud Detection

## 📌 Project Overview

This project aims to detect fraudulent credit card transactions using Machine Learning techniques. Due to the highly imbalanced nature of the dataset, special preprocessing techniques such as SMOTE were applied to improve fraud detection performance.

A Streamlit dashboard has also been developed to allow users to enter transaction details and predict whether a transaction is fraudulent or legitimate in real time.

---

## 🎯 Objectives

* Understand and analyze the credit card transaction dataset.
* Handle class imbalance effectively.
* Train and compare multiple machine learning models.
* Evaluate models using appropriate metrics.
* Build an interactive dashboard for fraud prediction.

---

## 📂 Dataset

Dataset Source:

https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud?resource=download

### Dataset Information

* Total Transactions: 284,807
* Fraudulent Transactions: 492
* Features: 30
* Target Variable:

  * 0 → Legitimate Transaction
  * 1 → Fraudulent Transaction

Features include:

* Time
* V1 to V28 (PCA-transformed features)
* Amount

---

## 🏗️ Project Architecture

```text
Dataset
   │
   ▼
Data Understanding & EDA
   │
   ▼
Data Preprocessing
   ├── Missing Value Check
   ├── Feature Scaling
   ├── Train-Test Split
   └── SMOTE Oversampling
   │
   ▼
Model Training
   ├── Logistic Regression
   ├── Decision Tree
   └── Random Forest
   │
   ▼
Model Evaluation
   ├── Accuracy
   ├── Precision
   ├── Recall
   ├── F1 Score
   └── Confusion Matrix
   │
   ▼
Model Selection
   │
   ▼
Model Serialization (.pkl)
   │
   ▼
Streamlit Dashboard
   │
   ▼
Fraud Prediction
```

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Imbalanced-Learn (SMOTE)
* SHAP
* Streamlit
* Pickle

---

## 🧹 Data Preprocessing

* Checked for missing values
* Separated features and target variable
* Applied train-test split
* Performed feature scaling
* Handled class imbalance using SMOTE

---

## 🤖 Machine Learning Models

### 1. Logistic Regression

Used as a baseline model for binary classification.

### 2. Decision Tree

Used to capture non-linear relationships within the dataset.

### 3. Random Forest

Selected as the final model due to superior overall performance.

---

## 📊 Model Performance

| Model               | Accuracy (%) | Precision (%) | Recall (%) | F1 Score (%) |
| ------------------- | ------------ | ------------- | ---------- | ------------ |
| Logistic Regression | 97.461       | 5.890         | 91.837     | 11.070       |
| Decision Tree       | 99.754       | 39.286        | 78.571     | 52.381       |
| Random Forest       | 99.954       | 89.130        | 83.673     | 86.316       |

---

## 🏆 Final Model Selection

Random Forest Classifier was selected as the final model because it achieved the best balance between Precision and Recall, resulting in the highest F1 Score among all evaluated models.

---

## 📈 Evaluation Metrics

The following metrics were used:

* Accuracy
* Precision
* Recall
* F1 Score
* Confusion Matrix

### Why Accuracy Can Be Misleading

The dataset is highly imbalanced. A model can achieve high accuracy by predicting most transactions as legitimate while still failing to identify fraudulent transactions effectively.

### Most Important Metric

Recall is particularly important because missing fraudulent transactions can lead to financial losses. F1 Score was also considered to ensure a balance between Precision and Recall.

---

## 🔍 Model Explainability

SHAP (SHapley Additive exPlanations) was used to understand feature importance and improve model interpretability.

---

## 🖥️ Streamlit Dashboard

The project includes a Streamlit-based dashboard that:

* Loads the trained model (.pkl)
* Accepts transaction feature inputs
* Predicts whether a transaction is fraudulent or legitimate
* Displays model performance metrics
* Displays model comparison visualizations

---

## 📁 Repository Structure

```text
Credit_Card_Fraud_Detection/
│
├── Credit_Card_Fraud_Detection.ipynb
├── fraud_model.pkl
├── app.py
├── requirements.txt
├── README.md
├── model_comparison.png
└── shap_summary.png
```

---

## 🚀 How to Run

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Launch Dashboard

```bash
streamlit run app.py
```

---

## 👨‍💻 Author

Aryan Agrawal

B.Tech Student | IIIT Nagpur

Machine Learning & Data Engineering Enthusiast
