import streamlit as st
import pandas as pd
import random
from datetime import datetime, timedelta
import uuid
import plotly.express as px
import time
import os
from PIL import Image

st.set_page_config(page_title="Real-Time Crisis Dashboard", layout="wide")

st.title("🌐 Real-Time Crisis Management Dashboard")
st.markdown("Displaying synthetic real-time data for emergency monitoring.")

refresh_rate = st.sidebar.slider("🔄 Refresh Rate (seconds)", min_value=5, max_value=60, value=10)
st.sidebar.markdown("---")
st.sidebar.write("Live updating data every few seconds.")

# Filters
selected_type = st.sidebar.selectbox("🔍 Filter by Disaster Type", ["All"] + [
    "Forest Fire Hotspot", "Earthquake", "Flood", "Cyclone", "Avalanche", 
    "Cloud Burst", "Coastal Currents", "Swell Surge", "High Wave", 
    "Nowcast Warning", "Temperature Alert", "News", "Watch", "Alert", "Warning"
])

# Pre-defined lists
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

disaster_types = [
    "Forest Fire Hotspot", "Earthquake", "Flood", "Cyclone", "Avalanche", 
    "Cloud Burst", "Coastal Currents", "Swell Surge", "High Wave", 
    "Nowcast Warning", "Temperature Alert", "News", "Watch", "Alert", "Warning"
]
severity_levels = ["Low", "Moderate", "High", "Severe"]
alert_levels = ["None", "Watch", "Alert", "Warning"]
locations = ["Mumbai", "Delhi", "Chennai", "Kolkata", "Hyderabad", "Bangalore", 
             "Ahmedabad", "Pune", "Jaipur", "Lucknow", "Bhopal", "Nagpur", "Patna"]
sources = ["IMD", "INCOIS", "CWC", "FSI", "NDMA", "ISRO", "News Agency", "Citizen Report"]

def generate_data(n=5500):
    records = []
    for _ in range(n):
        event_type = random.choice(disaster_types)
        record = {
            "Event_ID": str(uuid.uuid4()),
            "Event_Type": event_type,
            "Severity_Level": random.choice(severity_levels),
            "Latitude": round(random.uniform(8.0, 37.0), 4),
            "Longitude": round(random.uniform(68.0, 97.0), 4),
            "Location": random.choice(locations),
            "Timestamp": (datetime.now() - timedelta(hours=random.randint(0, 24))).strftime("%Y-%m-%d %H:%M:%S"),
            "Source": random.choice(sources),
            "Alert_Level": random.choice(alert_levels),
            "Description": f"{event_type} reported with {random.choice(severity_levels)} severity."
        }
        records.append(record)
    return pd.DataFrame(records)

placeholder = st.empty()
image_index = 0

while True:
    df = generate_data()
    if selected_type != "All":
        df = df[df["Event_Type"] == selected_type]

    with placeholder.container():
        st.markdown("### 📊 Key Metrics")
        col1, col2, col3 = st.columns(3)
        col1.metric("🔴 Total Alerts", len(df))
        col2.metric("⚠ High Severity Events", str(len(df[df["Severity_Level"] == "Severe"])))
        col3.metric("📍 Unique Locations", df["Location"].nunique())

        st.markdown("---")

        # Slideshow Image Viewer
        st.image(image_paths[image_index % len(image_paths)], use_container_width=True, caption="Disaster Snapshot")
        image_index += 1

        st.markdown("### 📈 Live Event Type Distribution")
        fig1 = px.bar(df.groupby("Event_Type").size().reset_index(name="Count"),
                      x="Event_Type", y="Count",
                      color="Count", color_continuous_scale="Reds")
        fig1.update_layout(height=350, transition_duration=500, xaxis_tickangle=-45)
        st.plotly_chart(fig1, use_container_width=True)

        st.markdown("### 🧭 Event Source Contribution")
        fig_source = px.pie(df, names="Source", title="Alert Distribution by Source")
        fig_source.update_layout(height=350)
        st.plotly_chart(fig_source, use_container_width=True)

        st.markdown("### 🏙 Top Affected Locations")
        top_locations = df["Location"].value_counts().nlargest(10).reset_index()
        top_locations.columns = ["Location", "Count"]
        fig_location = px.bar(top_locations, x="Location", y="Count", color="Count", color_continuous_scale="Viridis")
        fig_location.update_layout(height=350)
        st.plotly_chart(fig_location, use_container_width=True)

        st.markdown("### 🌍 Live Alert Distribution by Location")
        fig2 = px.scatter_geo(df, lat="Latitude", lon="Longitude", color="Severity_Level",
                              hover_name="Location", size_max=15, opacity=0.7,
                              color_discrete_map={"Low": "green", "Moderate": "orange", "High": "red", "Severe": "darkred"})
        fig2.update_layout(geo_scope="asia", transition_duration=500, height=350)
        st.plotly_chart(fig2, use_container_width=True)

        st.markdown("### 📈 Severity Level Over Time")
        df_sorted = df.sort_values("Timestamp")
        severity_time = df_sorted.groupby("Timestamp")["Severity_Level"].value_counts().unstack().fillna(0)
        severity_time = severity_time.reset_index().melt(id_vars=["Timestamp"], var_name="Severity", value_name="Count")
        fig3 = px.line(severity_time, x="Timestamp", y="Count", color="Severity", markers=True)
        fig3.update_layout(height=350, xaxis_title="Time", yaxis_title="Count")
        st.plotly_chart(fig3, use_container_width=True)

        st.markdown("### ⏳ Recent Alerts Table")
        st.dataframe(df.sort_values("Timestamp", ascending=False).head(20), use_container_width=True)

    time.sleep(refresh_rate)