import streamlit as st
import pandas as pd

st.title("Volunteer Lifecycle & Retention Tracker")

df = pd.read_csv("volunteers.csv", parse_dates=["join_date", "last_active_date"])

total_volunteers = len(df)
active_volunteers = df[df["status"] == "Active"].shape[0]
inactive_volunteers = df[df["status"] == "Inactive"].shape[0]

st.metric("Total Volunteers", total_volunteers)
st.metric("Active Volunteers", active_volunteers)
st.metric("Inactive Volunteers", inactive_volunteers)

st.subheader("Volunteer Status Breakdown")
st.bar_chart(df["status"].value_counts())

st.subheader("Join Dates Over Time")
df_by_month = df.set_index("join_date").resample("M").count()["volunteer_id"]
st.line_chart(df_by_month)

st.subheader("Raw Volunteer Data")
st.dataframe(df)
