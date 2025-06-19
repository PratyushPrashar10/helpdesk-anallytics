import streamlit as st
import pandas as pd

st.title("📊 Helpdesk Analytics Dashboard")

# Load dataset
@st.cache_data
def load_data():
    df = pd.read_csv("data/Updated_IT_Help_Desk_50k (2).csv")
    df.columns = df.columns.str.strip()  # Clean up any extra spaces
    df.rename(columns={"Max Day": "ResolutionTime"}, inplace=True)
    return df

df = load_data()

# Show dataset preview
st.subheader("🔍 Raw Data Preview")
st.dataframe(df.head())
import plotly.express as px

st.subheader("📌 Tickets by Priority")

priority_counts = df["Priority"].value_counts().reset_index()
priority_counts.columns = ["Priority", "Ticket Count"]

fig1 = px.bar(
    priority_counts,
    x="Priority",
    y="Ticket Count",
    color="Priority",
    title="Ticket Volume by Priority",
    labels={"Ticket Count": "Number of Tickets"},
)
st.plotly_chart(fig1, use_container_width=True)
st.subheader("⏱️ Average Resolution Time by Ticket Type")

avg_res_time = df.groupby("TicketType")["ResolutionTime"].mean().reset_index()
avg_res_time = avg_res_time.sort_values("ResolutionTime", ascending=False)

fig2 = px.bar(
    avg_res_time,
    x="TicketType",
    y="ResolutionTime",
    color="TicketType",
    title="Avg Resolution Time by Ticket Type (in Days)",
    labels={"ResolutionTime": "Avg Days to Resolve"},
)
st.plotly_chart(fig2, use_container_width=True)
