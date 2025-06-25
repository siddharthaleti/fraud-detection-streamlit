
# 💳 Real-Time Fraud Detection System

A machine learning-powered web app to detect fraudulent financial transactions in real-time using **XGBoost** and **Streamlit**.


## 🚀 Live Demo

👉 [Click here to use the app](https://fraud-detection-app-113.streamlit.app)

---

## 📦 Project Overview

This project simulates a real-time fraud detection system built with:

- 🧠 **XGBoost** for classification
- 🌐 **Streamlit** for interactive UI
- 🧾 **Streamlit Cloud** for deployment
- 📦 `joblib`, `pandas`, `scikit-learn`, `numpy` for preprocessing and model handling

It takes input features and predicts whether a transaction is **fraudulent or legitimate**, along with the **fraud probability**.

---

## 🧠 Dataset

We used a **credit card transaction dataset** with anonymized features.  
Each feature `V1` to `V28` is a principal component derived from PCA (for confidentiality), along with `Amount`, `Time`, and the target `Class`:

- `V1` to `V28`: PCA components of original transaction features
- `Amount`: Transaction amount
- `Time`: Seconds since the first transaction
- `Class`: 1 = Fraud, 0 = Legitimate

---

## 🛠 Features

- 🔢 Manual input for real-time transaction testing
- 📈 Fraud prediction with probability score
- ⚠️ Clean error handling for malformed input
- ☁️ Deployed and accessible globally

---

## 📁 File Structure

```

fraud-detection-streamlit/
├── streamlit\_app.py           # Streamlit app source code
├── xgboost\_fraud\_model.pkl    # Trained XGBoost model
├── Requirements.txt           # All required dependencies
└── README.md                  # You're reading it!

````

---

## 🔧 Setup Instructions (Local)

### 1. Clone the Repository

```bash
git clone https://github.com/siddharthaleti/fraud-detection-streamlit.git
cd fraud-detection-streamlit
````

### 2. Create a Virtual Environment & Install Requirements

```bash
pip install -r Requirements.txt
```

### 3. Run the App

```bash
streamlit run streamlit_app.py
```

---

## 🌐 Deployment

This app is deployed using **Streamlit Cloud**.
To deploy your own version:

1. Push code to GitHub
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your repo
4. Set main file path to `streamlit_app.py`
5. Done!

---

## ✅ Future Improvements

* ✅ Add file upload option for bulk prediction
* ✅ Add visualizations of fraud trends
* 🔒 Integrate login/authentication for secure access
* 📈 Include performance metrics like confusion matrix and ROC

---

## 👨‍💻 Author

**Siddharth Aleti**
📫 [GitHub](https://github.com/siddharthaleti) 
