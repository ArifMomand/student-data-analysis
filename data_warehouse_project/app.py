import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Data Warehouse Dashboard", layout="wide")

# ======================
# 📥 LOAD DATA
# ======================
df = pd.read_csv("data/data_warehouse.csv")

# ======================
# 🎓 TITLE
# ======================
st.title("🎓 Data Warehouse Dashboard")

st.divider()

# ======================
# 📌 KPI SECTION
# ======================
st.subheader("📌 Key Metrics")

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Students", len(df))
col2.metric("Average Marks", round(df["marks"].mean(), 2))
col3.metric("Highest Mark", df["marks"].max())
col4.metric("Lowest Mark", df["marks"].min())

st.divider()

# ======================
# 🔍 FILTER SECTION
# ======================
st.subheader("🔍 Filter by Department")

dept = st.selectbox("Choose Department", df["department"].unique())
filtered = df[df["department"] == dept]

st.write(filtered)

st.divider()

# ======================
# 📊 BAR CHART (ALL DATA)
# ======================
st.subheader("📊 Average Marks by Department")

avg_all = df.groupby("department")["marks"].mean()

col1, col2, col3 = st.columns([1,2,1])

with col2:
    fig1, ax1 = plt.subplots(figsize=(5, 3))
    avg_all.plot(kind="bar", ax=ax1)
    st.pyplot(fig1)

st.divider()

# ======================
# 📊 BAR CHART (FILTERED)
# ======================
st.subheader(f"📊 Average Marks in {dept}")

avg_filtered = filtered.groupby("department")["marks"].mean()

col1, col2, col3 = st.columns([1,2,1])

with col2:
    fig2, ax2 = plt.subplots(figsize=(5, 3))
    avg_filtered.plot(kind="bar", ax=ax2)
    st.pyplot(fig2)

st.divider()

# ======================
# 🥧 PIE CHART
# ======================
st.subheader("🥧 Student Distribution")

count_dep = df["department"].value_counts()

col1, col2, col3 = st.columns([1,2,1])

with col2:
    fig3, ax3 = plt.subplots(figsize=(4, 4))
    ax3.pie(count_dep, labels=count_dep.index, autopct="%1.1f%%")
    ax3.axis("equal")
    st.pyplot(fig3)

st.divider()

# ======================
# 🏆 TOP STUDENTS
# ======================
st.subheader("🏆 Top Students")

top_students = df.sort_values("marks", ascending=False).head(5)
st.dataframe(top_students)

st.divider()

# ======================
# 📋 FULL DATA
# ======================
st.subheader("📋 Full Dataset")

st.dataframe(df)