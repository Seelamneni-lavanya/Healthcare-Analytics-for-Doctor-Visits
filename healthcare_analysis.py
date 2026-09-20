# ============================================
# HEALTHCARE ANALYTICS FOR DOCTOR VISITS
# ============================================

# 1. Import libraries

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ============================================
# 2. Load Dataset
# ============================================

df = pd.read_csv("healthcare_doctor_visits.csv")

print("\nDataset loaded successfully!")
print(df)


# ============================================
# 3. First 5 Rows
# ============================================

print("\n--- First 5 Rows ---")
print(df.head())


# ============================================
# 4. Last 5 Rows
# ============================================

print("\n--- Last 5 Rows ---")
print(df.tail())


# ============================================
# 5. Dataset Shape
# ============================================

print("\n--- Dataset Shape ---")
print(df.shape)


# ============================================
# 6. Dataset Information
# ============================================

print("\n--- Dataset Information ---")
print(df.info())


# ============================================
# 7. Statistical Summary
# ============================================

print("\n--- Statistical Summary ---")
print(df.describe())


# ============================================
# 8. Missing Values
# ============================================

print("\n--- Missing Values ---")
print(df.isnull().sum())


# ============================================
# 9. Gender Distribution
# ============================================

plt.figure(figsize=(6, 4))

sns.countplot(data=df, x="gender")

plt.title("Gender Distribution")
plt.xlabel("Gender")
plt.ylabel("Number of Patients")

plt.tight_layout()
plt.show()


# ============================================
# 10. Age Distribution
# ============================================

plt.figure(figsize=(8, 5))

sns.histplot(data=df, x="age", bins=20, kde=True)

plt.title("Age Distribution")
plt.xlabel("Age")
plt.ylabel("Number of Patients")

plt.tight_layout()
plt.show()


# ============================================
# 11. Doctor Visits Distribution
# ============================================

plt.figure(figsize=(8, 5))

sns.histplot(data=df, x="visits", bins=20, kde=True)

plt.title("Distribution of Doctor Visits")
plt.xlabel("Number of Doctor Visits")
plt.ylabel("Number of Patients")

plt.tight_layout()
plt.show()


# ============================================
# 12. Average Doctor Visits by Gender
# ============================================

avg_visits_gender = df.groupby("gender")["visits"].mean()

print("\n--- Average Doctor Visits by Gender ---")
print(avg_visits_gender)

plt.figure(figsize=(6, 4))

avg_visits_gender.plot(kind="bar")

plt.title("Average Doctor Visits by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Visits")

plt.xticks(rotation=0)
plt.tight_layout()
plt.show()


# ============================================
# 13. Illness vs Doctor Visits
# ============================================

illness_visits = df.groupby("illness")["visits"].mean()

print("\n--- Average Visits by Illness Level ---")
print(illness_visits)

plt.figure(figsize=(7, 5))

sns.barplot(
    x=illness_visits.index,
    y=illness_visits.values
)

plt.title("Average Doctor Visits by Illness Level")
plt.xlabel("Illness Level")
plt.ylabel("Average Visits")

plt.tight_layout()
plt.show()


# ============================================
# 14. Health vs Doctor Visits
# ============================================

plt.figure(figsize=(8, 5))

sns.boxplot(data=df, x="health", y="visits")

plt.title("Health Status vs Doctor Visits")
plt.xlabel("Health Status")
plt.ylabel("Doctor Visits")

plt.tight_layout()
plt.show()


# ============================================
# 15. Chronic Conditions vs Doctor Visits
# ============================================

plt.figure(figsize=(8, 5))

sns.boxplot(data=df, x="nchronic", y="visits")

plt.title("Chronic Conditions vs Doctor Visits")
plt.xlabel("Number of Chronic Conditions")
plt.ylabel("Doctor Visits")

plt.tight_layout()
plt.show()


# ============================================
# 16. Income vs Doctor Visits
# ============================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="income",
    y="visits",
    hue="gender"
)

plt.title("Income vs Doctor Visits")
plt.xlabel("Income")
plt.ylabel("Doctor Visits")

plt.tight_layout()
plt.show()


# ============================================
# 17. Age vs Doctor Visits
# ============================================

plt.figure(figsize=(8, 5))

sns.scatterplot(
    data=df,
    x="age",
    y="visits",
    hue="gender"
)

plt.title("Age vs Doctor Visits by Gender")
plt.xlabel("Age")
plt.ylabel("Doctor Visits")

plt.tight_layout()
plt.show()


# ============================================
# 18. Correlation Heatmap
# ============================================

numeric_df = df.select_dtypes(include=np.number)

plt.figure(figsize=(10, 7))

sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)

plt.title("Correlation Heatmap")

plt.tight_layout()
plt.show()


# ============================================
# 19. Key Findings
# ============================================

print("\n============================================")
print("KEY FINDINGS")
print("============================================")

print("""
1. The dataset contains information about doctor visits,
   demographic factors, health conditions and healthcare access.

2. Doctor visits can be analyzed across different gender groups.

3. Illness and health-related variables can be compared
   with the number of doctor visits.

4. Chronic health conditions can be examined in relation
   to healthcare utilization.

5. Age and income can be explored to understand their
   relationship with doctor visits.

6. The correlation heatmap provides an overview of
   relationships between numerical variables.
""")

print("\nProject analysis completed successfully!")