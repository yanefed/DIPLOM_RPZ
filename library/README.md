# Airline-Delay-Analysis-Prediction

This repository contains a comprehensive data science/machine learning project aimed at analyzing and predicting flight delays using the U.S. Department of Transportation's Airline On-Time Performance Dataset. The project covers data exploration, feature engineering, machine learning models, and visualizations to provide insights into flight delays, cancellations, and diversions.

## Overview

The primary objective of this project is to uncover patterns and causes of flight delays, cancellations, and diversions, and to build predictive models that forecast delays. This analysis is useful for airlines, airports, and passengers looking to improve operational efficiency and minimize travel disruptions.

## Project Link

Access the full analysis and visualizations in the Jupyter notebooks provided in this repository.

Medium Article: [Analyzing and Predicting Airline Delays: A Comprehensive Data Science Approach](https://medium.com/@rvora3/analyzing-and-predicting-airline-delays-a-comprehensive-data-science-approach-c08d5de14a10)

## Project Features

The project includes the following components:

**1. Data Exploration and Preprocessing**
- Dataset Overview: Introduction to the structure and key variables of the dataset, which includes over 4 million records and 110 features.
- Flight Status Classification: Categorization of flights into early, on-time, delayed, canceled, and diverted flights.

**2. Exploratory Data Analysis (EDA)**
- Flight Count by Airline: Visualization of the number of flights operated by different airlines.
- Delay Distribution by Month: Line plots showing average delays over time, highlighting peak delay periods.
- Cause of Delays: Analyzing the breakdown of delays caused by carriers, weather, and other factors.

**3. Machine Learning Models**
- Feature Engineering: Creation of relevant features such as departure and arrival delays, distance, and day-of-week to improve predictive modeling.
- Model Training: Using various machine learning algorithms like Linear Regression, Random Forest, and XGBoost to predict delays.
- Model Evaluation: Evaluating model performance using metrics like Mean Squared Error (MSE) and R-Squared scores.
  
**4. Visualizations**
- Delay by Airline: Bar charts showing delay distribution across airlines.
- Flight Status Breakdown: Pie and bar charts visualizing early, on-time, and delayed flight proportions.
- Top Delayed Airports: Insights into which airports experience the highest delays.

## Dataset

The data used in this project is sourced from the [U.S. Department of Transportation's Airline](https://www.transtats.bts.gov/DL_SelectFields.aspx?gnoyr_VQ=FGJ&QO_fu146_anzr=b0-gvzr) On-Time Performance Dataset, covering flight information from January 2024 to July 2024.

Data Features: Includes details like flight dates, departure and arrival times, delays, cancellations, diversion status, and more.
Size: **4,095,932 records and 110 columns.**


## How to Use

To explore the project:

1. Clone or download this repository to your local machine
2. Create a virtual environment and activate it
3. Install the required packages
4. Ensure the dataset is available in the data directory
5. Open and run the Jupyter notebook
