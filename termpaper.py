import streamlit as st
import pandas as pd
import numpy as np
import time
import random
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, timedelta
from sklearn.ensemble import RandomForestRegressor
from PIL import Image
import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import uuid

# -------------------------------
# Login Authentication
# -------------------------------
def login_form():
    st.title("\U0001F510 Real-Time Crisis Detection Admin Login")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        if username == "sravani" and password == "admin":
            st.session_state.logged_in = True
            st.success("Login successful!")
            st.rerun()
        else:
            st.error("Invalid username or password.")

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if not st.session_state.logged_in:
    login_form()
    st.stop()

# -------------------------------
# Send Email Function
# -------------------------------
def send_email_alert(subject, message, recipient_email):
    sender_email = "sravani20499@gmail.com"
    sender_password = "admin"  # WARNING: Use environment variables or secrets in production

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = recipient_email
    msg["Subject"] = subject
    msg.attach(MIMEText(message, "plain"))

    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.quit()
        return True
    except Exception as e:
        st.error(f"Error sending email: {e}")
        return False

# -------------------------------
# Image Paths
# -------------------------------
image_paths = [
    r"C:\\Users\\Sravani\\OneDrive\\Analysis of Digital Marketing\\flood.jpg",
    r"C:\\Users\\Sravani\\OneDrive\\Analysis of Digital Marketing\\earthquake.jpg",
    r"C:\\Users\\Sravani\\OneDrive\\Analysis of Digital Marketing\\wildfire.webp",
    r"C:\\Users\\Sravani\\OneDrive\\Analysis of Digital Marketing\\hurricane.webp",
    r"C:\\Users\\Sravani\\OneDrive\\Analysis of Digital Marketing\\disaster.jpg",
    r"C:\\Users\\Sravani\\OneDrive\\Analysis of Digital Marketing\\storm.jpg",
    r"C:\\Users\\Sravani\\OneDrive\\Analysis of Digital Marketing\\rescue.jpg",
    r"C:\\Users\\Sravani\\OneDrive\\Analysis of Digital Marketing\\fire.jpg",
    r"C:\\Users\\Sravani\\OneDrive\\Analysis of Digital Marketing\\evacuation.jpg"
]

# -------------------------------
# Generate Synthetic Real-Time Crisis Data (5500 rows)
# -------------------------------
def generate_crisis_data():
    disaster_types = [
        "Forest Fire Hotspot", "Earthquake", "Flood", "Cyclone", "Avalanche",
        "Cloud Burst", "Coastal Currents", "Swell Surge", "High Wave",
        "Nowcast Warning", "Temperature Alert", "News", "Watch", "Alert", "Warning"
    ]
    severity_levels = [1, 2, 3, 4, 5]
    alert_levels = ["None", "Watch", "Alert", "Warning"]
    locations = ["Mumbai", "Delhi", "Chennai", "Kolkata", "Hyderabad", "Bangalore",
                 "Ahmedabad", "Pune", "Jaipur", "Lucknow", "Bhopal", "Nagpur", "Patna"]
    sources = ["IMD", "INCOIS", "CWC", "FSI", "NDMA", "ISRO", "News Agency", "Citizen Report"]
    sentiments = ["Positive", "Neutral", "Negative"]

    records = []
    for _ in range(5500):
        event_type = random.choice(disaster_types)
        severity = random.choice(severity_levels)
        record = {
            "Event_ID": str(uuid.uuid4()),
            "Crisis Type": event_type,
            "Severity": severity,
            "Latitude": round(random.uniform(8.0, 37.0), 4),
            "Longitude": round(random.uniform(68.0, 97.0), 4),
            "Location": random.choice(locations),
            "Time": (datetime.now() - timedelta(hours=random.randint(0, 24))).strftime("%Y-%m-%d %H:%M:%S"),
            "Source": random.choice(sources),
            "Alert_Level": random.choice(alert_levels),
            "Sentiment": random.choice(sentiments),
            "Description": f"{event_type} reported in the area with severity level {severity}."
        }
        records.append(record)

    df = pd.DataFrame(records)
    df.to_csv("RealTime_Crisis_24Hours_India.csv", index=False)
    panic_states = [loc for loc in df['Location'].unique() if df[df['Location'] == loc]['Severity'].mean() > 3.5]
    return df, panic_states

# -------------------------------
# Predict Severity
# -------------------------------
def predict_severity(df):
    df_encoded = pd.get_dummies(df[["Crisis Type", "Location", "Sentiment"]])
    X = df_encoded
    y = df["Severity"]
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X, y)
    df["Predicted Severity"] = model.predict(X).round()
    return df

# -------------------------------
# Streamlit Dashboard UI
# -------------------------------
st.set_page_config(page_title="\U0001F30D Real-Time Crisis Management", layout="wide")
st.title("\U0001F6A8 Real-Time Crisis Management Dashboard")
st.write("\U0001F4E2 Live social media monitoring for crisis detection and prediction")

df, panic_states = generate_crisis_data()
df = predict_severity(df)

# Alert Section
if "alert_triggered" not in st.session_state:
    st.session_state.alert_triggered = False
    st.session_state.alert_message = ""

def show_alert():
    st.session_state.alert_triggered = True
    st.session_state.alert_message = st.session_state.input_alert_message

st.subheader("\U0001F6A8 Real-Time Crisis Alerts")
st.session_state.input_alert_message = st.text_input("Enter custom alert message:")
recipient_email = st.text_input("Enter recipient email to send alert:")
if st.button("Check for Crisis Alerts"):
    show_alert()
    if "Negative" in df["Sentiment"].values and recipient_email:
        sent = send_email_alert("Crisis Alert \u26A0\uFE0F", st.session_state.alert_message, recipient_email)
        if sent:
            st.success(f"\u2705 Email sent to {recipient_email}!")

if st.session_state.alert_triggered and "Negative" in df["Sentiment"].values:
    st.warning(f"\u26A0\uFE0F Warning! {st.session_state.alert_message}")

# Panic States
st.subheader("\u26A0\uFE0F States in Panic Situation")
st.write(", ".join(panic_states))

# Weather Report
st.subheader("\u1F326 Live Weather Report")
st.write("Temperature: 28\u00B0C | Humidity: 70% | Wind Speed: 12 km/h")

# Data Table
st.subheader("\U0001F4DD Latest Crisis Reports")
st.dataframe(df, use_container_width=True)

# Image Gallery
st.subheader("\U0001F5BC\uFE0F Crisis Image Gallery")
cols = st.columns(3)
for idx, path in enumerate(image_paths):
    col = cols[idx % 3]
    try:
        with Image.open(path) as img:
            col.image(img, caption=os.path.basename(path), width=200)
    except:
        col.warning(f"Could not load image: {os.path.basename(path)}")

# Time Series
st.subheader("\U0001F4C8 Time Series: Severity over Time")
df['Time'] = pd.to_datetime(df['Time'])
df_sorted = df.sort_values(by="Time")
fig1, ax1 = plt.subplots()
ax1.plot(df_sorted["Time"], df_sorted["Severity"], marker='o', linestyle='-', color='#D7263D')
ax1.set_title("Severity Trend Over Time")
ax1.set_xlabel("Time")
ax1.set_ylabel("Severity Level")
plt.xticks(rotation=45)
st.pyplot(fig1)

# Bar Plot
st.subheader("\U0001F4CA Crisis Type Distribution")
crisis_counts = df["Crisis Type"].value_counts()
fig_bar, ax_bar = plt.subplots(figsize=(8, 5))
sns.barplot(x=crisis_counts.index, y=crisis_counts.values, palette="rocket", ax=ax_bar)
ax_bar.set_title("Crisis Type Frequency")
ax_bar.set_ylabel("Number of Reports")
ax_bar.set_xlabel("Crisis Type")
st.pyplot(fig_bar)

# Sentiment Pie Chart
st.subheader("\U0001F967 Sentiment Distribution")
sentiment_counts = df["Sentiment"].value_counts()
fig2, ax2 = plt.subplots()
ax2.pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%',
        colors=['#8BC34A', '#9E9E9E', '#F44336'])
ax2.set_title("Overall Sentiment Composition")
st.pyplot(fig2)

# Scatter Plot
st.subheader("\u26AA Scatter Plot: Severity vs Crisis Type")
df['Crisis Encoded'] = df['Crisis Type'].astype('category').cat.codes
fig3, ax3 = plt.subplots()
sns.scatterplot(data=df, x="Crisis Encoded", y="Severity", hue="Crisis Type", palette="husl", ax=ax3)
ax3.set_title("Scatter Plot of Severity by Crisis Type")
st.pyplot(fig3)

# Cumulative Plot
st.subheader("\U0001F4C9 Cumulative Severity Line Plot")
df_sorted["Cumulative Severity"] = df_sorted["Severity"].cumsum()
fig4, ax4 = plt.subplots()
ax4.plot(df_sorted["Time"], df_sorted["Cumulative Severity"], color='#2196F3')
ax4.set_title("Cumulative Severity Over Time")
plt.xticks(rotation=45)
st.pyplot(fig4)

# Dot Graph
st.subheader("\U0001F535 Dot Graph: Location vs Severity")
fig5, ax5 = plt.subplots()
sns.stripplot(data=df, x="Location", y="Severity", jitter=True, palette="deep", ax=ax5)
ax5.set_title("Severity vs Location")

st.pyplot(fig5)
