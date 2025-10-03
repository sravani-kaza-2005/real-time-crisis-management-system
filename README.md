PROJECT TITTLE : 🚨 Real-Time Crisis Management System

A powerful, real-time web application that monitors, predicts, and visualizes critical situations such as floods, earthquakes, and other crisis emergencies using enriched datasets and machine learning techniques — built with **Python** and **Streamlit**.

---

## 🔎 Overview

🎯 **Purpose:**  
The Real-Time Crisis Management System is a Python-based platform designed to detect, analyze, and respond to critical situations in real time. It leverages multi-source data including weather APIs, social media feeds, IoT sensors, and public reports to provide actionable insights during emergencies. The system is aimed at improving disaster response, public safety, and decision-making efficiency.
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
   👤 Username: sravani
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
**Login Authentication**

<img width="1908" height="1000" alt="image" src="https://github.com/user-attachments/assets/f27542be-873f-4e73-ae40-5f852f2c9dd1" />
<img width="1918" height="942" alt="image" src="https://github.com/user-attachments/assets/ad0a9644-d478-4a65-aaa5-2572262b9408" />

-----
# 🛡️ Admin Module

<img width="1910" height="992" alt="image" src="https://github.com/user-attachments/assets/2976a7e3-7f83-4c25-9cce-efe528fcfb50" />
<img width="1914" height="647" alt="image" src="https://github.com/user-attachments/assets/7df2a457-bcb7-47bd-be71-192004014a6c" />
<img width="1911" height="644" alt="image" src="https://github.com/user-attachments/assets/54caf182-4fcf-4c0e-b9a4-45fb9b283c90" />
<img width="1915" height="1057" alt="image" src="https://github.com/user-attachments/assets/2c6a8e3f-2341-46e9-8d3e-e8e0bb5b3af6" />
<img width="1910" height="608" alt="image" src="https://github.com/user-attachments/assets/65aec123-a8f8-4e47-8af2-d7ecb34d4c60" />
<img width="1918" height="1072" alt="image" src="https://github.com/user-attachments/assets/9fc129b1-4c53-48e2-adda-0e78836e328d" />
<img width="1919" height="876" alt="image" src="https://github.com/user-attachments/assets/c0fcb472-af72-4aed-820c-0c23c6878ab3" />
<img width="1910" height="1072" alt="image" src="https://github.com/user-attachments/assets/cdf1e381-cd74-4164-bfe7-db4e4004fe98" />
<img width="1134" height="988" alt="image" src="https://github.com/user-attachments/assets/56fdc35d-2f7f-471a-9012-679e3e4680c4" />
<img width="692" height="698" alt="image" src="https://github.com/user-attachments/assets/da5f6d60-0a0b-45e2-b975-47d471e12578" />
<img width="891" height="631" alt="image" src="https://github.com/user-attachments/assets/09d178dc-83cb-49e6-a55e-9e369ab9ae46" />
<img width="887" height="672" alt="image" src="https://github.com/user-attachments/assets/7b697202-d2c9-4f21-a74c-c17fe6c2fdc5" />
<img width="912" height="631" alt="image" src="https://github.com/user-attachments/assets/72085e97-70fc-4417-becc-589a5648782a" />
<img width="1460" height="950" alt="image" src="https://github.com/user-attachments/assets/0487c44b-f23b-42ff-a756-56be26371f9b" />
<img width="1143" height="1048" alt="image" src="https://github.com/user-attachments/assets/1b2be222-b2fd-4c5e-9406-0da17241be2c" />

-----
## 👤 User Module

<img width="1912" height="1068" alt="image" src="https://github.com/user-attachments/assets/fe31d6f7-67e9-48f0-84eb-a77bd5d6ff81" />
<img width="1904" height="1021" alt="image" src="https://github.com/user-attachments/assets/929b050f-dbee-4dc4-ae7e-3c5a3f52ba76" />
<img width="1908" height="1049" alt="image" src="https://github.com/user-attachments/assets/b5c1d254-1f88-47c7-bb4a-72616ee6c1f6" />
<img width="1910" height="1035" alt="image" src="https://github.com/user-attachments/assets/7cd6777d-3fe6-495c-9752-dc843f2c6fef" />
<img width="1903" height="1082" alt="image" src="https://github.com/user-attachments/assets/345add37-2da1-4c52-ba55-345b2ed0ae4a" />

------
## 👤User Pricing(🆓 Free, ⚡Basic, 💎Premium,🏢Enterprise) 
<img width="1919" height="944" alt="image" src="https://github.com/user-attachments/assets/cc5c106f-2069-4822-b645-85ffea39c974" />

**👤User-🆓Free**
<img width="1280" height="680" alt="image" src="https://github.com/user-attachments/assets/fe65624e-2e99-448b-bb60-8b7363fc90c4" />
<img width="1280" height="682" alt="image" src="https://github.com/user-attachments/assets/c8550fcb-7bf8-4adb-a4a6-a02e4654c6ba" />

**👤User-⚡Basic**
<img width="1280" height="681" alt="image" src="https://github.com/user-attachments/assets/e6187af5-e470-488b-b7bc-cf3fa7de4152" />
<img width="1280" height="688" alt="image" src="https://github.com/user-attachments/assets/3f014a45-e785-49b7-8751-5ea1e1859a59" />
<img width="1280" height="700" alt="image" src="https://github.com/user-attachments/assets/38cf83d3-fce6-4d6b-8c53-d3ad1e014817" />
<img width="1280" height="608" alt="image" src="https://github.com/user-attachments/assets/d4afb596-28e3-46db-b13d-9c40218037a7" />
<img width="1280" height="599" alt="image" src="https://github.com/user-attachments/assets/4ad21974-9b54-421a-a35a-e1e9e00076c8" />
<img width="1280" height="657" alt="image" src="https://github.com/user-attachments/assets/bf2d253c-e078-4942-b08d-140f80b09ef1" />

**👤User-💎Premium**
<img width="1280" height="533" alt="image" src="https://github.com/user-attachments/assets/8eba416e-5219-4927-a0ad-331db650e005" />
<img width="1280" height="605" alt="image" src="https://github.com/user-attachments/assets/311872d4-c7e5-4c66-889c-40839ad8dc03" />
<img width="1280" height="631" alt="image" src="https://github.com/user-attachments/assets/0638351f-ddd4-49fa-a744-6f59c825abae" />
<img width="1280" height="649" alt="image" src="https://github.com/user-attachments/assets/a2b644d1-e211-4325-b781-504b7f48d77c" />

**👤User-🏢Enterprise**
<img width="1280" height="620" alt="image" src="https://github.com/user-attachments/assets/69308629-c8ba-4633-8b8c-d68cbcef54cf" />
<img width="1280" height="678" alt="image" src="https://github.com/user-attachments/assets/b045b784-cd7a-4896-a6a3-ea012c3ba85d" />
<img width="1280" height="692" alt="image" src="https://github.com/user-attachments/assets/098a1536-e5fe-4e3e-95dc-6e5e223903e8" />
<img width="1280" height="683" alt="image" src="https://github.com/user-attachments/assets/b684fdd0-b0d6-40c3-a9cb-9cc947344288" />
<img width="1280" height="694" alt="image" src="https://github.com/user-attachments/assets/0b765912-f6a6-4e32-b86e-34d8e5ba6c4e" />

------
## 📜 License

📝 This project is licensed under the **MIT License** — allowing open use, modification, and distribution for personal or commercial purposes.
💡 If you use or build upon this project, giving credit is appreciated.

---

🔧 **Designed & Developed with dedication by KAZA SRAVANI**
