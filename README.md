# Code-IT-Final-Internship-Project  
This project is part of the final internship in Data Science with Python for Code-IT.  

# 📊 Sales Analytics Dashboard & Profit Prediction System

## 📌 Overview
This project is a complete **Sales Analytics and Profit Prediction System** built using Python, Machine Learning, and Streamlit.

It includes:
- Data preprocessing & feature engineering  
- Exploratory Data Analysis (EDA)  
- KPI generation  
- Machine learning model (Linear Regression)  
- Interactive dashboard using Streamlit  
- Exported datasets for visualization  

---

## 🎯 Objectives
- Analyze sales performance across time, region, and categories  
- Identify key factors affecting profit  
- Build a machine learning model to predict profit  
- Create an interactive dashboard for business insights  

---

## 📊 Dataset
Dataset used: **Supermart Grocery Sales - Retail Analytics Dataset**

### 📌 Features include:
- Order ID  
- Customer Name  
- Category  
- Sub Category  
- City  
- Order Date  
- Region  
- Sales  
- Discount  
- Profit  
- State  

---

## 🛠️ Technologies Used
- Python  
- Pandas  
- NumPy  
- Matplotlib  
- Plotly  
- Scikit-learn  
- Streamlit  
- OpenPyXL  
- Pickle  

---

## 🔍 Project Workflow

### 1. Data Preprocessing
- Converted `Order Date` to datetime  
- Extracted:
  - Year  
  - Month  
  - Month Name  
- Created new feature:

```python
Profit Margin % = (Profit * 100 / (Sales - Discount))




 ### 2. KPI Calculation
Key business metrics were calculated to summarize overall performance:

- **Total Sales**: Sum of all sales values  
- **Total Orders**: Count of unique order IDs  
- **Total Profit**: Sum of all profit values  
- **Average Order Value**: Total sales divided by total orders  
- **Profit Margin %**: Percentage of profit relative to total sales  

These KPIs were structured into a separate dataset (`kpi_data`) for easy integration into the dashboard.

---

### 3. Exploratory Data Analysis (EDA)
Exploratory analysis was performed to identify trends and patterns in the data:

- Sales trends across years were analyzed to understand growth  
- Monthly sales patterns were studied to identify seasonality  
- Sales distribution across regions was examined  
- Sub-category and product-level performance were evaluated  

Visualizations such as bar charts and line graphs were used to make insights more interpretable.

---

### 4. Feature Engineering
Categorical variables such as **Category** and **Region** were transformed into numerical format using encoding techniques. This step was necessary to make the data compatible with machine learning algorithms.

New features like **Profit Margin %** also enhanced the predictive power of the model.

---

### 5. Model Development
A **Linear Regression model** was developed to predict profit based on key features:

- Sales  
- Discount  
- Profit Margin %  
- Category  
- Region  

The dataset was split into training and testing sets to evaluate model performance effectively.

---

### 6. Model Evaluation
The model was evaluated using standard regression metrics:

- **R² Score** to measure how well the model explains variance  
- **Mean Absolute Error (MAE)** to measure average prediction error  
- **Root Mean Squared Error (RMSE)** to penalize larger errors  
- **Mean Squared Error (MSE)** for overall error measurement  

The results indicated that the model performs well and generalizes effectively without significant overfitting.

---

### 7. Data Export for Dashboard
Processed datasets and aggregated results were exported into a single Excel file with multiple sheets.  

This file serves as the data source for the Streamlit dashboard and includes:

- KPI data  
- Yearly sales  
- Monthly sales  
- Sales by region  
- Sales by sub-category  
- Top and bottom performing products  

---

### 8. Model Saving
The trained machine learning model and encoders were saved using serialization techniques.  

Saved files include:
- Trained regression model  
- Category encoder  
- Region encoder  

These files are later loaded into the Streamlit application for real-time profit prediction.

---




# Project Dependencies (requirements.txt)

This document explains the libraries used in the **Sales Analytics Dashboard & Profit Prediction** project. These libraries are listed in the `requirements.txt` file so that anyone cloning the repository can easily install the required dependencies.

---

## requirements.txt

```
streamlit
pandas
numpy
scikit-learn
plotly
openpyxl
```

---

## Library Explanation

### Streamlit

Used to build the interactive dashboard for visualizing sales data, KPIs, and machine learning results.

### Pandas

Used for data cleaning, manipulation, and analysis of the sales dataset.

### NumPy

Provides numerical operations and array processing used during data preparation.

### Scikit-Learn

Used to build the machine learning model (Linear Regression) and evaluate performance metrics such as R², MAE, MSE, and RMSE.

### Plotly

Creates interactive visualizations such as sales charts, category comparisons, and trend analysis graphs.

### OpenPyXL

Allows Python to read and write Excel files used for storing processed datasets and analysis outputs.

---
How to Run the Project

1. Clone the repository:
https://github.com/Feian-osa/Code-IT-Internship-project.git


2.Install dependencies
## Installing the Dependencies

To install all required libraries, run the following command in the terminal:

```
pip install -r requirements.txt
```

This command installs all the libraries required to run the Streamlit dashboard and the machine learning model for the project.

---

## Purpose of requirements.txt

The `requirements.txt` file ensures that anyone who downloads or clones the project can recreate the same environment with the exact libraries needed to run the code successfully.
