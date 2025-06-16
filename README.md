# 🍽️ Swiggy’s Restaurant Recommendation System using Streamlit

A machine learning-based restaurant recommender that suggests restaurants based on user preferences like city, cuisine, cost, and rating. Built with Python and Streamlit.

---

## 🎯 Project Objectives

- Clean and preprocess restaurant data
- Encode categorical features using One-Hot Encoding
- Apply similarity-based recommendation (Cosine Similarity)
- Build a Streamlit app for user interaction and recommendation display

---

## 🧠 Skills Gained

- Data Cleaning & Preprocessing  
- One-Hot Encoding  
- Cosine Similarity & Recommendation Systems  
- Streamlit App Development  
- Python for Data Science  

---

## 🧾 Dataset Description

Original columns in dataset:
- `id`, `name`, `city`, `rating`, `rating_count`, `cost`, `cuisine`, `lic_no`, `link`, `address`, `menu`

### 🔧 Features Used:
- **Categorical**: `name`, `city`, `cuisine`  
- **Numerical**: `rating`, `rating_count`, `cost`

---

## 🧹 Data Preprocessing

1. Removed duplicates and missing values
2. Cleaned `cost` column (removed currency symbols)
3. Applied One-Hot Encoding on `city`, `cuisine`, and `name`
4. Saved cleaned dataset to `cleaned_data.csv`
5. Saved encoded dataset to `encoded_data.csv`
6. Saved encoder model to `encoder.pkl`

---

## 📁 Download Required Files

### ⚠️ Note:
GitHub does not allow files larger than 25 MB. Please manually download the encoded dataset from the following link:

📥 **Download `encoded_data.csv` here**:  
👉 [Click to Download](https://drive.google.com/uc?export=download&id=1rSnO6xRz42tTE9xjTNdxJlmndNCPrGZ_)

> Place the downloaded file in the root directory of this project.

---

## 🧠 Recommendation Methodology

- Cosine Similarity is used to compare user input vector with restaurant vectors in the encoded dataset
- Top N most similar restaurants are selected and displayed

---

## 🖥️ Streamlit App Features

- User inputs: `city`, `cuisine`, `cost`, `rating`
- Displays a table of recommended restaurants
- Clean and intuitive UI for end-users

---

## 🚀 How to Run

1. Install dependencies:

```bash
pip install pandas scikit-learn streamlit
