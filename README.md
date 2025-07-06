# Multivariate Analysis of Membrane Properties using PLS

This repository contains the code, analysis, and report for a project conducted as part of the **ChE208: Process Data Analysis** course at IIT Indore. The objective was to investigate interdependencies among membrane properties and their relationship to membrane quality using multivariate statistical techniques, particularly **Partial Least Squares (PLS) Regression**.

## 📊 Project Overview

A dataset containing **120 membrane samples** with **8 predictor variables (X)** — representing mechanical, electrical, and transport properties — and **1 response variable (y)** representing membrane quality was analyzed.

The goals were:

* To explore **correlations** and **multicollinearity** among predictor variables.
* To assess the performance of **Multiple Linear Regression (MLR)** and identify its limitations.
* To develop a **Partial Least Squares (PLS)** model to characterize the relationship between X and y.

## 🧪 Dataset

* **120 rows** (samples)
* **8 X-variables** (continuous, no missing values)
* **1 Y-variable** (quality metric)
* Data was already cleaned and normalized for analysis

## 📈 Methodology

1. **Data Preprocessing**

   * Organized into suitable format
   * Centered and scaled
   * Verified absence of missing values

2. **Exploratory Data Analysis (EDA)**

   * Heatmaps to inspect multicollinearity
   * Q-Q plots and residual plots to assess MLR assumptions

3. **Modeling Approaches**

   * **MLR**: Showed poor predictive power and suffered from multicollinearity and non-linearity
   * **PLS Regression**:

     * 2-component model selected using cross-validation
     * Explained 45.5% of variance in Y
     * Cross-validated Q²: 0.348

## 📌 Key Results

* **MLR** failed due to:

  * High multicollinearity among X1, X3, X5
  * U-shaped residuals indicating non-linearity
  * Poor generalization (Q² = 0.33)

* **PLS** was more robust:

  * R<sup>2</sup>(cum) = 0.455
  * Q<sup>2</sup>(cum) = 0.348
  * Key influential variables:

    * Positive: X3, X5, X8
    * Negative: X2

## 🖼️ Visualizations

* **Loadings Plot**: Showed X3 and X5 highly correlate with Y
* **Scores Plot**: Detected outliers like Sample 14
* **Regression Coefficient Plot**: Confirmed direction and strength of influence for each predictor

## 📚 Tools Used

* **SIMCA** software for PLS modeling and visualization
* **Python (optional)**: For any pre/post processing or plots (not provided here)

## Presentation
You can view the [Canva presentation](https://www.canva.com/design/DAGl44T3lBU/WkSRb3MJeDz8vfo_PTLVsQ/edit)

## 🧑‍💻 Team Members

* Abhinav Singh (230008002)
* Garvit Kumbhat (230008014)
* Mohak Dadhich (230008023)
* Vighnehs Mandwaria (230008039)

## 📝 Conclusion

PLS regression proved to be a more reliable and interpretable approach compared to MLR for this membrane dataset, offering insights into which properties most affect quality. Future work could involve:

* Non-linear modeling techniques
* Larger datasets for better generalization
* Feature selection methods to improve Q<sup>2</sup>
