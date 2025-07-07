# Multivariate Analysis of Membrane Properties Using Partial Least Squares (PLS)

> **Course Project · IIT Indore · ChE 208 — Process Data Analysis**
> **Key Skills:** Multivariate Statistics · PLS Regression · Python · SIMCA · Data Visualization · Chemical Engineering

---

## 💡 Executive Summary

* Engineered and validated a **2‑component Partial Least Squares (PLS) model** that **explains 45.5 %** of membrane‑quality variance and delivers a **Q² = 0.348**—a **+6 % lift** over a baseline Multiple Linear Regression (MLR) model.
* Diagnosed and mitigated **multicollinearity** among mechanical, electrical, and transport properties, reducing model error **27 %** versus MLR.
* Detected and flagged critical outliers (e.g., *Sample 14*) through **scores & loadings analysis**, strengthening data integrity.

---

## 📦 Dataset

| Samples | Predictors *(X)*                                          | Target *(y)*            | Cleaning Status                |
| ------- | --------------------------------------------------------- | ----------------------- | ------------------------------ |
| 120     | 8 continuous features (mechanical, electrical, transport) | Membrane quality metric | No missing values · Normalized |

---

## 🔧 Tech Stack & Tools

* **Python 3.11**: *pandas*, *numpy*, *matplotlib*, *scikit‑learn*
* **SIMCA 17**: PLS modeling & cross‑validation
* **Git / GitHub**: Version control & CI‑ready repo
* **Markdown & Canva**: Technical reporting & slide deck

---

## 🚀 Methodology

1. **Data Preprocessing**
   ▸ Centered & scaled features
   ▸ Verified zero missing entries

2. **Exploratory Data Analysis (EDA)**
   ▸ Heatmap correlation matrix uncovered **X1–X3–X5** multicollinearity
   ▸ Q‑Q & residual plots revealed MLR non‑linearity

3. **Model Development**
   **Multiple Linear Regression (MLR)**
   ▸ Baseline; underperformed with **Q² = 0.33**

   **Partial Least Squares (PLS) Regression**
   ▸ **2 latent variables** selected via 10‑fold cross‑validation
   ▸ **R²(cum) 0.455 | Q²(cum) 0.348**
   ▸ Important loadings: **(+)** X3 X5 X8, **(−)** X2

---

## 📊 Key Visualizations

* **Loadings Plot** — Highlights X3 & X5 synergy with membrane quality.
* **Scores Plot** — Uncovered outlier *Sample 14*, prompting further QC.
* **Regression Coefficient Plot** — Clarifies positive vs negative feature impact.

> Visual assets are stored in `/figures` and showcased in the [Canva slide deck](https://www.canva.com/design/DAGl44T3lBU/WkSRb3MJeDz8vfo_PTLVsQ/edit).

---

## 📝 Results & Impact

| Metric  | MLR   | PLS (🔹 **Best**) |
| ------- | ----- | ----------------- |
| R²(cum) | 0.402 | **0.455**         |
| Q²(cum) | 0.330 | **0.348**         |
| RMSE    | 0.158 | **0.115**         |

*PLS reduced RMSE by **27 %** and improved predictive stability, making it the preferred model for membrane quality forecasting.*

---

## 🌟 Achievements

* **Optimized Model Complexity:** Balanced variance explained vs overfitting using **K‑fold CV**.
* **Actionable Insights:** Identified high‑impact variables (**X3, X5, X8**) guiding future membrane design.
* **Collaborative Workflow:** Orchestrated a 4‑member team with Git branching, PR reviews, and milestone tracking.

---

## 👥 Contributors

| Name                             | Role                          | Email                                                               |
| -------------------------------- | ----------------------------- | ------------------------------------------------------------------- |
| Abhinav Singh *(230008002)*      | Data Preprocessing & EDA Lead | [che230008002@iiti.ac.in](mailto:che230008002@iiti.ac.in)           |
| Garvit Kumbhat *(230008014)*     | Modeling & Validation Lead    | [che230008014@iiti.ac.in](mailto:che230008014@iiti.ac.in)         |
| Mohak Dadhich *(230008023)*      | Visualization & Reporting Lead     | [che230008023@iiti.ac.in](mailto:che230008023@iiti.ac.in)           |
| Vighnesh Mandwaria *(230008039)* | Documentation & Preprocessing Lead          | [che230008039@iiti.ac.in](mailto:che230008039@iiti.ac.in) |

---

## 🔮 Future Work

* Explore **non‑linear kernels** (e.g., **Kernel‑PLS**, **SVR**) for potential accuracy gains.
* Increase sample size or augment with synthetic data to strengthen generalization.
* Integrate **feature selection** (VIP > 1 thresholding) to enhance Q².

---

## 📂 Repository Structure

```
├── data/              # Raw & processed datasets (CSV)
├── notebooks/         # Jupyter notebooks for EDA & modeling
├── scripts/           # Reproducible Python pipelines
├── figures/           # Generated plots & visuals
└── report/            # PDF report & slide deck
```

---

## ▶️ Getting Started

1. **Clone** the repository:

   ```bash
   git clone https://github.com/<username>/membrane-pls.git
   cd membrane-pls
   ```
2. **Create env & install deps:**

   ```bash
   python -m venv .venv && source .venv/bin/activate
   pip install -r requirements.txt
   ```
3. **Reproduce analysis:**

   ```bash
   jupyter notebook notebooks/01_pls_analysis.ipynb
   ```

---



