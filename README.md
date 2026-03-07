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
