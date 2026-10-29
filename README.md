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
├── MLR_analysis.ipynb             # Original MLR notebook
├── PS/MembranePROB2data.txt       # Bundled numeric data: 120 samples, 8 predictors + target
├── PS/Group 2.pdf                # Assignment
├── Images (Simca)/               # SIMCA visualizations
├── Project Report Group 2 PDA.pdf
├── requirements.in              # Selected direct Python dependencies
├── requirements.lock            # Pinned dependencies with artifact hashes
└── scripts/                     # Setup, notebook execution, and JupyterLab
```

---

## ▶️ Getting Started

Install [uv](https://docs.astral.sh/uv/getting-started/installation/) and Git, then run these commands in Bash on Linux or macOS:

```bash
git clone https://github.com/Abhinav072004/Multivariate-Analysis-of-Membrane-Properties.git
cd Multivariate-Analysis-of-Membrane-Properties
bash scripts/setup.sh
.venv/bin/python scripts/run-analysis.py
```

Setup installs Python 3.11.14, creates `.venv`, installs the hash-locked dependencies, and registers a notebook kernel. It can be run again to refresh the environment. It requires access to GitHub/Python download assets and PyPI. Keep your configured proxy and CA trust; installation verifies TLS and artifact hashes.

The analysis helper executes a generated copy of `MLR_analysis.ipynb` from a clean kernel. It supplies the bundled dataset and redirects the original Google Drive CSV read to that local file, preserving the original notebook. This handles two existing notebook issues: an undefined `dataset` variable and a hard-coded `/content/drive/MyDrive/new.csv` path. Running the original notebook directly still requires those inputs.

Successful execution checks all 120 samples, eight predictor-count cross-validation calculations, finite predictions and residuals, and six diagnostic/validation plots. It writes:

- `outputs/MLR_analysis.executed.ipynb` — executed notebook with the local input adapter.
- `outputs/MLR_analysis.html` — shareable rendered analysis.
- `outputs/readiness.json` — current validation results and model metrics.

On the bundled data, the Python MLR workflow gives training R² ≈ 0.468477 and five-fold Q² ≈ 0.319124. The PLS/SIMCA results reported above belong to the separate course-project report; this repository does not contain an executable Python PLS implementation. SIMCA is proprietary and optional for the Python workflow.

### Interactive notebooks

```bash
bash scripts/start-jupyter.sh
```

JupyterLab uses token authentication on loopback port 8888. Open `outputs/MLR_analysis.executed.ipynb` and select the **Python (Membrane)** kernel. Start the server again in each new session; installed files persist, running processes do not.

Environment folders, runtime files, and generated outputs are ignored by Git. To update the dependency lock intentionally:

```bash
uv pip compile --python 3.11.14 --generate-hashes requirements.in -o requirements.lock
bash scripts/setup.sh
.venv/bin/python scripts/run-analysis.py
```
