PROJECT TITTLE : 🚨 Real-Time Crisis Management System

A powerful, real-time web application that monitors, predicts, and visualizes critical situations such as floods, earthquakes, and other emergencies using enriched datasets and machine learning — all through a sleek **dark-themed dashboard** built with **Python** and **Streamlit**.

---

## 🔎 Overview

🎯 **Purpose:**  
To provide a centralized system for detecting and responding to real-time crisis events with clarity and speed.

🧰 **Core Functions:**  
- Live crisis data visualization  
- Severity prediction using ML  
- Email alerts for high-risk zones  
- Role-based access (Admin & User)  
- Premium dashboard module with advanced analytics  

---

## ✨ Key Features

🟢 **Real-Time Analysis** – Reads updated 24-hour dataset and displays panic zones  
🧠 **ML-Based Predictions** – Predicts crisis severity from input data  
📩 **Email Alerts** – Sends real-time notifications using SMTP  
🔒 **Secure Login System** – Basic authentication for Admin & User  
💎 **Premium Features** – Extended insights, advanced filters, export option  
🖼️ **Crisis Gallery** – Visuals for awareness (e.g., floods, earthquakes)  
📊 **Interactive Charts** – Scrollable data table & real-time metrics  
⚡ **Lightweight & Fast** – Runs entirely in browser with Streamlit

---

## 📦 Libraries Used

- **Streamlit** – for building the web dashboard  
- **Pandas** – for data manipulation and filtering  
- **NumPy** – for numerical operations  
- **Scikit-learn** – for crisis severity prediction using trained models  
- **Matplotlib & Seaborn** – for generating graphs and visualizations  
- **SMTP (smtplib, email.mime)** – for sending alert notifications  
- **uuid** – for unique alert/session identifiers  
- **datetime** – for time-based updates and filtering  
- **os** – for image/file path management  
- **PIL (Pillow)** – for handling gallery image rendering  

---

## 🏗️ How the Code is Developed

1. **Data Ingestion:**  
   The system loads a 24-hour enriched dataset (`RealTime_Crisis_24Hours_India.csv`) containing crisis types, timestamps, severity scores, and locations.

2. **Authentication:**  
   A simple login system using hardcoded credentials allows role-based access to different modules (`termpaper.py` for Admin, `termpaperuser.py` for Users).

3. **Visualization:**  
   Uses Streamlit widgets like `st.metric`, `st.dataframe`, `st.image`, and `st.line_chart` to render dynamic metrics and tables.

4. **Machine Learning Integration:**  
   A pre-trained ML model (`model.pkl`) is loaded to predict severity scores and identify "panic states."

5. **Email Alerts:**  
   Upon detecting high-severity events, the admin can trigger email alerts using SMTP with automated message formatting.

6. **Premium Module:**  
   Users with premium access unlock deeper analytics like extended historical data, filters, and downloadable reports.

7. **UI Design:**  
   A dark-themed CSS-inspired design using Streamlit's built-in theming and a custom image gallery enhances the user experience.

---

## 📁 Project Structure

```
real-time-crisis-management-system/
│
├── 📄 README.md
├── 📄 requirements.txt
├── 📄 termpaper.py                ← Admin module
├── 📄 termpaperuser.py            ← User module
├── 📄 RealTime_Crisis_24Hours_India.csv  ← Crisis dataset
├── 📁 images/                     ← Visual gallery (flood.jpg, etc.)
└── 📁 .streamlit/                 ← Optional configs
    └── config.toml
```

---

## 🚀 Getting Started

### 🖥️ Run Locally

1. **Clone this repository**  
   ```bash
   git clone https://github.com/your-username/real-time-crisis-management-system.git
   cd real-time-crisis-management-system
   ```

2. **Install required packages**  
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the application**  
   - 🛠️ For Admin access:
     ```bash
     streamlit run termpaper.py
     ```
   - 👤 For User access:
     ```bash
     streamlit run termpaperuser.py
     ```

4. **Login Credentials**  
   ```
   👤 Username: admin
   🔑 Password: admin
   ```

---

## 🛠️ Built With

- 🐍 **Python 3.10+**
- 📊 **Streamlit**
- 📚 **Pandas / NumPy**
- 🤖 **Scikit-learn**
- 📨 **SMTP (for Email Notifications)**
- 📈 **Matplotlib / Seaborn**

---

## 🖼️ UI Preview

> 📍 Real-time metrics for total events and panic zones  
> 📉 Graphical ML predictions and alert zones  
> 🖼️ Gallery with disaster images  
> 🔐 Secure Admin-only panels and CSV controls  

---

## 📜 License

📝 This project is licensed under the **MIT License** — allowing open use, modification, and distribution for personal or commercial purposes.
💡 If you use or build upon this project, giving credit is appreciated.

---

🔧 **Designed & Developed with dedication by KAZA SRAVANI**
