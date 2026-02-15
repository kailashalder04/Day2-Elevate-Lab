# 🚢 Titanic Dataset – Exploratory Data Analysis (EDA)

![Python](https://img.shields.io/badge/Python-3.10-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-yellow)
![Matplotlib](https://img.shields.io/badge/Matplotlib-Visualization-orange)
![Seaborn](https://img.shields.io/badge/Seaborn-Statistical%20Plots-lightblue)
![Plotly](https://img.shields.io/badge/Plotly-Interactive%20Visualization-darkblue)


![titanic](https://github.com/user-attachments/assets/2cbcde83-fea2-48f5-b0ea-0d0a90cc78aa)

## 📌 Project Overview

This project performs Exploratory Data Analysis (EDA) on the Titanic dataset to understand:

1. Data distribution

2. Feature relationships

3. Outliers

4. Survival patterns

5. Data quality issues

---

## 📂 Dataset Information

- Source: Kaggle Titanic Dataset  
- Rows: 891  
- Target Variable: `Survived`  
- Problem Type: Binary Classification

---

## 📌 Tools Used:

Python

Pandas

Matplotlib

Seaborn

Plotly

---

## 📊  Dataset Overview

Target Variable: Survived

Total Features: Passenger demographics, ticket information, family size, fare, etc.

Objective: Identify patterns affecting survival.

---

## 📈 Visual Analysis & Insights

## 1️⃣ Age Distribution
![Boxplot of Age](eda_outputs/box_Age.png)


### 🔎 Insights:

Majority of passengers aged between 20–40 years.

Slight right skew.

Few elderly outliers (65+).

Age alone is not a strong survival predictor.

---

## 2️⃣ Fare Distribution
![Boxplot of Fare](eda_outputs/box_Fare.png)

### 🔎 Insights:

Highly right-skewed distribution.

Most fares below 50.

Extreme high-value outliers (100–500+).

Outliers represent first-class passengers.

Log transformation recommended for modeling.

---

## 3️⃣ Parch (Parents/Children Aboard)
![Boxplot of Parch](eda_outputs/box_Parch.png)

### 🔎 Insights:

Most passengers traveled without parents/children.

Few large family outliers.

Feature may help in family survival analysis.

---

## 4️⃣ PassengerId
![Boxplot of PassengerId](eda_outputs/box_PassengerId.png)

### 🔎 Insights:

Uniform distribution.

Pure identifier.

Not useful for modeling.

Should be removed.

---

## 5️⃣ Passenger Class (Pclass)
![Boxplot of Pclass](eda_outputs/box_Pclass.png)

### 🔎 Insights:

Majority passengers were in 3rd class.

Strong relationship between class and survival.

Higher class → better survival probability.

---

## 6️⃣ SibSp (Siblings/Spouse Aboard)
![Boxplot of SibSp](eda_outputs/box_SibSp.png)

### 🔎 Insights:

Most passengers traveled alone.

Some large family groups exist.

Family size may influence survival.

---

## 7️⃣ Survival Distribution
![Boxplot of Survived](eda_outputs/box_Survived.png)

### 🔎 Insights:

Binary target variable.

Better visualized using countplot.

Class imbalance present.

---

## 🔥 Correlation Analysis
![Boxplot of Correlation Matrix](eda_outputs/correlation_matrix.png)

### 🔎 Key Findings:

Fare positively correlated with survival.

Pclass negatively correlated with survival.

No severe multicollinearity detected.

---

## 📌 Key Business-Level Insights

Gender and Passenger Class strongly influence survival.

Fare is highly skewed and contains extreme values.

Most passengers traveled alone.

Data requires preprocessing before modeling (handling missing values & skewness).

---

## 🛠 Data Preprocessing Recommendations

Impute missing Age values.

Drop PassengerId.

Handle Cabin (high missing ratio).

Apply log transformation on Fare.

Encode categorical variables.

---

## 🎯 Conclusion

EDA successfully identified:

Survival-driving factors

Outlier presence

Skewness in numeric features

Feature importance direction

Dataset is ready for feature engineering and model development.
