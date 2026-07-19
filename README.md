# 🏠 House Price Prediction System

An end-to-end Machine Learning project that predicts house prices based on various property features. This project covers the complete ML workflow, including data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment using Streamlit.

---

## 📌 Project Overview

The goal of this project is to build a machine learning model capable of predicting the selling price of a house using features such as area, number of bedrooms, bathrooms, stories, parking, furnishing status, and other amenities.

The project compares multiple machine learning algorithms and deploys the best-performing model as an interactive web application.

---
## 🚀 Live Demo

**Streamlit App:** https://house-price-prediction-darshan1.streamlit.app

## 🚀 Features

- Data Cleaning & Preprocessing
- Exploratory Data Analysis (EDA)
- Feature Engineering
- Model Comparison
- Hyperparameter Tuning
- Model Evaluation
- Feature Importance Analysis
- Model Serialization using Joblib
- Interactive Streamlit Web Application

---

## 📂 Dataset

- Housing Price Dataset
- Number of Records: **545**
- Number of Features: **13**

### Features Used

- Area
- Bedrooms
- Bathrooms
- Stories
- Main Road
- Guest Room
- Basement
- Hot Water Heating
- Air Conditioning
- Parking
- Preferred Area
- Furnishing Status

Target Variable:

- Price

---

## 🛠 Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

## 📊 Machine Learning Workflow

### 1. Data Preprocessing

- Checked missing values
- Checked duplicate records
- Converted categorical variables into numerical format
- One-Hot Encoding using `pd.get_dummies()`

### 2. Exploratory Data Analysis

Performed visualization and analysis to understand:

- Distribution of house prices
- Relationship between area and price
- Correlation between features
- Effect of amenities on house price

### 3. Models Trained

- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor

### 4. Hyperparameter Tuning

Performed tuning on Decision Tree and Random Forest models to improve performance.

### 5. Model Evaluation

The models were evaluated using:

- Mean Absolute Error (MAE)
- Root Mean Squared Error (RMSE)
- R² Score

The best-performing model was selected for deployment.

---

## 📈 Best Model Performance

| Metric   | Value     |
| -------- | --------- |
| MAE      | 1,022,560 |
| RMSE     | 1,401,497 |
| R² Score | 0.6114    |

---

## 📌 Feature Importance

Feature analysis showed that the most influential variables were:

- Bathrooms
- Air Conditioning
- Hot Water Heating
- Preferred Area
- Stories
- Basement
- Main Road

---

## 🌐 Streamlit Application

The trained model was deployed using Streamlit.

The application allows users to:

- Enter house details
- Predict house price instantly
- View estimated property price through an easy-to-use interface

---

## 📁 Project Structure

```
House-Price-Prediction/
│
├── app.py
├── house_price_prediction.ipynb
├── house_price_model.pkl
├── feature_names.pkl
├── Housing.csv
├── requirements.txt
├── README.md
```

---

## ▶️ How to Run

### Clone the repository

```bash
git clone <repository-link>
```

### Navigate to project folder

```bash
cd House-Price-Prediction
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Run Streamlit App

```bash
streamlit run app.py
```

---

## 🎯 Future Improvements

- Improve prediction accuracy using advanced ensemble models
- Add additional feature engineering techniques
- Enhance UI/UX of the Streamlit application
- Deploy on Streamlit Community Cloud

---

## 👨‍💻 Author

**Darshan Panchal**

Aspiring Data Scientist | Machine Learning Enthusiast

---

## ⭐ If you found this project helpful, consider giving it a star!
