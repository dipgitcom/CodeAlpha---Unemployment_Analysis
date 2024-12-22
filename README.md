# Unemployment Analysis Project

This project analyzes unemployment data to uncover patterns and trends using data visualization and machine learning. The app is built with Python and Streamlit, integrating a Random Forest Classifier for prediction and analysis.

---

## 📖 Introduction

Unemployment is a critical economic issue that affects individuals, families, and entire nations. This project aims to explore, visualize, and predict unemployment trends using historical data. The app provides insights through interactive visualizations and implements machine learning to predict unemployment rates based on key features.

---

## ✨ Features

- **Interactive Dashboard**: Analyze unemployment trends using visualizations like line plots, heatmaps, and geographical scatter plots.
- **Machine Learning**: Predict unemployment rates using a Random Forest Classifier.
- **Data Filtering**: View unemployment statistics for specific regions, dates, and other parameters.
- **Correlation Analysis**: Understand relationships between employment, labor participation, and other factors.
- **Geographical Analysis**: Visualize unemployment rates across different regions on a map.

---

## 🛠️ Tools and Technologies Used

- **Programming Language**: Python
- **Framework**: Streamlit
- **Data Manipulation**: Pandas, NumPy
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: Scikit-learn (Random Forest Classifier)
- **IDE**: Jupyter Notebook / VS Code / PyCharm

---

## 📊 Dataset Description

The dataset used in this project contains the following columns:

- `Date`: The date of data collection.
- `Region`: The state or region in focus.
- `Estimated Unemployment Rate (%)`: Unemployment rate in the given region.
- `Estimated Employed`: Number of employed individuals.
- `Estimated Labour Participation Rate (%)`: Participation rate in the workforce.
- `Longitude` and `Latitude`: Coordinates for geographical mapping.

The dataset is cleaned and preprocessed to ensure quality analysis.

---

## 🔍 Algorithms

### Random Forest Classifier
The Random Forest Classifier is used for predicting unemployment rates based on historical data. This ensemble learning method provides high accuracy and handles missing data effectively.

---

## ⚙️ Workflow

1. **Data Loading and Preprocessing**:
   - Clean the dataset by removing null values and standardizing column names.
   - Convert dates to a suitable format for time-series analysis.

2. **Exploratory Data Analysis**:
   - Visualize unemployment trends using line charts, histograms, and heatmaps.
   - Analyze geographical impacts using interactive maps.

3. **Feature Engineering**:
   - Extract key features like month, year, and region.

4. **Model Training**:
   - Train the Random Forest Classifier on a portion of the dataset.
   - Evaluate model accuracy and performance.

5. **Prediction and Insights**:
   - Use the model to predict unemployment rates.
   - Display predictions and insights in the Streamlit app.

---

## 🚀 Steps to Run the Project

### Prerequisites
- Python 3.8 or above
- Pip

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/unemployment-analysis.git
   cd unemployment-analysis
