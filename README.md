# 📊 A/B Testing: Comparison of Conversion Rates Between Bidding Methods
![ımages](https://github.com/AylinOguz/AB_Testing/blob/main/Images/AB-Testing.png?raw=true)


## 📝 Project Overview
This project analyzes and compares Maximum Bidding and Average Bidding methods using A/B testing techniques. The goal is to determine if the change in bidding strategy leads to a statistically significant difference in user behavior and revenue generation.

## 📚 Dataset Description

- __click__: Number of clicks on those ads

- __purchase__: Number of purchases made after clicking the ads

- __earning__: Revenue generated from purchases

The dataset is stored in the file ab_testing.xlsx, with separate sheets for the control and test groups.

### 🔍 Objective
To perform a complete A/B testing process to evaluate the effectiveness of a new bidding method by:

__1.__ Preparing and cleaning the dataset

__2.__ Conducting exploratory data analysis (EDA)

__3.__ Performing normality and variance homogeneity tests

__4.__ Applying independent two-sample t-tests

__5.__ Interpreting statistical results 

### 🛠️ Tools & Libraries
- Python

- pandas, numpy

- matplotlib, seaborn

- statsmodels

- scipy

### 📈 Key Steps in the Notebook
- Data loading and merging of control/test groups

- Summary statistics and group-wise comparisons

- Hypothesis formulation and testing

- Interpretation of p-values to reach conclusions

### ✅ Conclusion
This notebook concludes with a statistical evaluation of the effectiveness of the Average Bidding strategy compared to Maximum Bidding, aiding data-driven decision making for marketing strategies.
