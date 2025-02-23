# Project4-Team2-Ad-Campaign-
## Ad Campaign Performance Prediction
 ### Data set: https://www.kaggle.com/datasets/ashaychoudhary/advertising-campaign-performance-dataset
### Overview
This project leverages machine learning to predict conversion rates for advertising campaigns using historical data. We compare Linear Regression and Random Forest models to determine the best-performing model. The project includes data preprocessing, model training, prediction analysis, and an interactive Streamlit dashboard for insights.
### 📂 Project Structure
#### 1️ Database (Extract & Store Data)
#### Files:
•	Database.ipynb → Extracts and stores ad campaign data in SQLite (ad_campaigns.db).
#### 2️ Data Preprocessing (Clean & Prepare Data)
#### Files:
•	Preprocessing.ipynb → Cleans raw data, encodes categorical features, scales numerical values.
•	cleaned_data.csv → The preprocessed dataset for training models.
#### 3️ Model Training & Prediction (Train & Evaluate Models)
 #### Files:
•	Training & Testing.ipynb → Trains Linear Regression and Random Forest models.
•	random_forest_model.pkl → Saved best-performing model (Random Forest).
•	scaler.pkl → Saved scaler for data preprocessing.
#### Performance Metrics:
R² Score → Explains variance in data.
Mean Squared Error (MSE) → Measures prediction accuracy.
### Results:
•	Random Forest: R² ≈ 0.97 (Best)
•	Linear Regression: R² ≈ 0.22
#### 4️ Model Comparison & Analysis
#### Files:
•	Comparison_Model.ipynb → Compares both models using visualization techniques.
•	model_comparison.csv → Performance results of both models.
##### Visualizations:
Bar Charts → R² Score & MSE for model comparison.
Scatter Plots → Actual vs. Predicted Conversion Rates.
Histograms → Distribution of Prediction Errors.
Heatmaps → Feature Correlations.
#### 5️ Predictions & Insights
 ### Files:
•	rf_predictions.csv → Predictions from Random Forest.
•	lr_predictions.csv → Predictions from Linear Regression.
•	analyze_predictions.ipynb → Generates detailed statistical analysis & visualizations.
#### 6️ Streamlit Dashboard (Interactive Data Insights)
 #### Files:
•	Dashboard.py → Streamlit dashboard script.
•	dashboard_reference.json → Stores category mappings (e.g., 0 = Facebook, 1 = Google).
#### 🔗 Live Dashboard URL:
https://project4-team2-ad-campaign-yhuambfq6jdaiy2krjvdcv.streamlit.app/

#### Features:   
Interactive data filtering by Platform, Content Type, Target Age, Region.
Dynamic visualizations for conversion rates, CPC impact, and platform performance.
Downloadable predictions for further analysis.

### 📊 Key Insights from the Analysis
More clicks ≠ higher conversions – Quality over quantity.
Higher CPC (Cost Per Click) drives better conversions – Premium ads perform better.
Budget alone doesn’t improve conversion rates – Targeting is crucial.
Random Forest provides the most accurate & stable predictions.
A/B testing should focus on CPC & audience targeting rather than just increasing ad spending.

#### How to Run the Project
1️ install Dependencies
pip install -r requirements.txt
2️ Run Data Preprocessing
python data_preprocessing.py
3️ Train Models
python train_models.py
4️ Run Streamlit Dashboard
streamlit run app.py

#### 🔥 Future Enhancements
 Further optimize Random Forest for even better accuracy.
improve feature engineering to boost Linear Regression.
Integrate real-time ad tracking into the dashboard.
Implement deep learning models for even more precise predictions.


## Conclusion:
This project successfully demonstrates how machine learning can optimize ad campaigns by predicting conversion rates based on historical data. By comparing Random Forest and Linear Regression, we identified the most effective model for driving data-driven advertising strategies.
### Key Takeaways:
#### Data-Driven Advertising: 
Predicting conversion rates helps optimize marketing budgets and improve targeting.
Model Comparison: Random Forest significantly outperformed Linear Regression, delivering higher accuracy and lower error rates.
Feature Importance: Click-through rate (CTR) and cost-per-click (CPC) have the strongest correlation with conversion rates.
Budget Optimization: Increasing ad spend does not always yield higher conversions—targeting high-intent users is key.
Real-Time Insights: The interactive Streamlit dashboard allows dynamic filtering and visualization of ad performance.
Error Analysis: The box plots and histograms provide a clear view of prediction errors, highlighting model reliability.
Scalability: The framework can be extended to integrate real-time ad performance tracking for continuous optimization.
### Next Steps & Improvements:
Hyperparameter Tuning: Further optimize the Random Forest model for even better accuracy.
Feature Engineering: Explore new features (e.g., engagement metrics) to improve prediction quality.

