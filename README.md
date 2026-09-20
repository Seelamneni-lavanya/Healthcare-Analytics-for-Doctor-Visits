# Healthcare Analytics for Doctor Visits

## 📌 Project Overview

This project analyzes healthcare data to understand the factors associated with doctor visits.

The analysis focuses on patient characteristics such as gender, age, income, illness level, health status, reduced activity, and chronic conditions.

The project uses Python for data cleaning, exploratory data analysis, visualization, and correlation analysis.

---

## 🎯 Objectives

- Analyze the distribution of patients by gender and age.
- Understand the distribution of doctor visits.
- Compare doctor visits between genders.
- Analyze the relationship between illness level and doctor visits.
- Study health status in relation to doctor visits.
- Analyze income and doctor visits.
- Examine age and doctor visits by gender.
- Analyze chronic-condition information.
- Identify relationships between numerical variables using correlation analysis.

---

## 📂 Dataset

The dataset contains **5,190 patient records** and **13 columns**.

### Important Columns

| Column | Description |
|---|---|
| visits | Number of doctor visits |
| gender | Patient gender |
| age | Patient age value |
| income | Patient income value |
| illness | Illness level |
| reduced | Number of days with reduced activity |
| health | Health status |
| private | Private insurance information |
| freepoor | Free/poor insurance information |
| freerepat | Free/repatriation insurance information |
| nchronic | Chronic-condition information |
| lchronic | Long-term chronic-condition information |

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- VS Code

---

## 📊 Data Analysis

The project includes the following visualizations:

1. Gender Distribution
2. Age Distribution
3. Distribution of Doctor Visits
4. Average Doctor Visits by Gender
5. Average Doctor Visits by Illness Level
6. Health Status vs Doctor Visits
7. Chronic Conditions vs Doctor Visits
8. Income vs Doctor Visits
9. Age vs Doctor Visits by Gender
10. Correlation Heatmap

---

## 🔍 Key Findings

- The dataset contains 5,190 patient records.
- Female patients have a higher average number of doctor visits than male patients in this dataset.
- Most patients have zero doctor visits, while higher numbers of visits occur less frequently.
- Average doctor visits increase across the illness levels in the dataset.
- The correlation analysis shows a positive relationship between doctor visits and reduced activity.
- Illness also shows a positive relationship with doctor visits.

---

## ▶️ How to Run the Project

### Step 1: Install Python

Make sure Python is installed on your computer.

### Step 2: Install Required Libraries

Open the VS Code terminal and run:

```bash
pip install pandas numpy matplotlib seaborn