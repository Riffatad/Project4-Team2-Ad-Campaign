
 ## 📊 Ad Campaign Performance Prediction
A machine learning project focused on predicting conversion rates for advertising campaigns using historical performance data. Developed as part of the Rutgers Data Science Bootcamp, this project compares Linear Regression and Random Forest models to determine the most effective prediction method, with an interactive Streamlit dashboard for actionable insights.

## 🚀Project Overview
This project analyzes ad campaign data to help stakeholders make data-driven decisions on ad spend, targeting, and strategy.
It covers:

Data extraction & storage in SQLite

Data cleaning, encoding, and scaling

Model training & evaluation (Linear Regression vs. Random Forest)

Visualization of results and prediction analysis

Interactive dashboard for campaign insights

By comparing model performance, we found Random Forest to be the best predictor of conversion rates (R² ≈ 0.97).

### 🧠 Objectives
Extract and store ad campaign data in a database

Clean and preprocess raw data (handle missing values, encode categories, scale features)

Train and evaluate prediction models

Compare model performance using multiple metrics

Build a dashboard for interactive campaign analysis

Provide strategic recommendations to improve conversions

###🗃️Dataset
Name: Advertising Campaign Performance Dataset

Source: Provided via Rutgers Bootcamp

Format: CSV → stored in SQLite database (ad_campaigns.db)

Key Features:

Platform (e.g., Facebook, Google)

Content Type

Target Age

Region

CPC (Cost Per Click)

Budget

Clicks

Conversions

Conversion Rate (target variable)

### 🛠️Technologies Used
Python 3.10+

Pandas / NumPy – Data manipulation & numerical computing

Matplotlib / Seaborn – Data visualization

scikit-learn – Model training & evaluation

SQLite – Data storage

Streamlit – Interactive dashboard

Jupyter Notebook – Development & documentation

## 📂Project Structure
Project4-Team2-Ad-Campaign/
│
├── data/                  # Raw & processed datasets
│   ├── cleaned_data.csv
│   ├── rf_predictions.csv
│   ├── lr_predictions.csv
│
├── database/
│   ├── Database.ipynb     # Extract & store in SQLite
│   ├── ad_campaigns.db
│
├── preprocessing/
│   ├── Preprocessing.ipynb
│   ├── scaler.pkl
│
├── models/
│   ├── Training & Testing.ipynb
│   ├── random_forest_model.pkl
│   ├── Comparison_Model.ipynb
│   ├── model_comparison.csv
│
├── analysis/
│   ├── Analyze_predictions.ipynb
│
├── dashboard/
│   ├── app.py
│   ├── dashboard_reference.json
│
├── images/                # Visuals for reports & README
│
└── README.md              # Project documentation
### 📈 Exploratory Data Analysis (EDA)
Checked and cleaned missing values

Encoded categorical variables

Scaled numerical features

Created bar charts for model comparisons (R² & MSE)

Built scatter plots for actual vs. predicted conversion rates

Generated histograms of prediction errors

Visualized heatmaps for feature correlations

### 🔍 Key Insights
More clicks ≠ higher conversions – quality of audience matters more than quantity

Higher CPC ads tend to convert better – premium ads outperform low-cost ones

Budget alone doesn’t drive conversions – targeting is critical

Random Forest outperforms Linear Regression significantly (R² ≈ 0.97 vs. 0.22)

A/B testing should focus on CPC & audience targeting rather than increasing ad spend

### 📊 Model Performance
Model	R² Score	MSE	Notes
Random Forest	0.97	Low	Best-performing model
Linear Regression	0.22	High	Struggled with non-linear patterns

### 💻Streamlit Dashboard Features
Interactive filtering by platform, content type, target age, and region

Visualizations for conversion rates, CPC impact, and platform performance

Downloadable predictions for further analysis

Real-time exploration of campaign data

Live Dashboard: [Add Link Here]

### ✅ Future Work
Further optimize Random Forest hyperparameters

Improve feature engineering for Linear Regression

Integrate real-time ad tracking into dashboard

Experiment with deep learning models for improved prediction accuracy

### 🧠 Learnings
Practical application of database management with SQLite

Hands-on experience with preprocessing pipelines in scikit-learn

Model comparison and performance evaluation techniques

Building an interactive dashboard to communicate data insights

📬 Contact
Riffat Adnan
LinkedIn
📧 riffat.email@example.com
---

## 🛡️ License

This project is licensed for educational purposes only. Attribution appreciated.

