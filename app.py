import streamlit as st
import pandas as pd

# ---- PAGE CONFIG ----
st.set_page_config(page_title="O*NET Explorer", layout="wide")

# ---- LOAD DATA ----
@st.cache_data
def load_data():
    occupation_df = pd.read_excel("data/Occupation Data.xlsx")
    related_df = pd.read_excel("data/Related Occupations.xlsx")
    knowledge_df = pd.read_excel("data/Knowledge.xlsx")
    skills_df = pd.read_excel("data/Skills.xlsx")
    return occupation_df, related_df, knowledge_df, skills_df

occupation_df, related_df, knowledge_df, skills_df = load_data()

# ---- UI ----
st.title("🔍 O*NET Skill Explorer")

# ---- Select an Occupation ----
selected_title = st.selectbox(
    "Select an Occupation:",
    sorted(occupation_df["Title"].unique())
)

# ---- Show Related Info ----
if selected_title:
    st.subheader(f"📌 Selected Occupation: {selected_title}")

    # Get the code
    selected_code = occupation_df[occupation_df["Title"] == selected_title]["O*NET-SOC Code"].values[0]

    # Skills
    st.markdown("### 🧠 Skills")
    skill_rows = skills_df[skills_df["O*NET-SOC Code"] == selected_code]
    st.dataframe(skill_rows[["Element Name", "Scale Name", "Data Value"]])

    # Knowledge
    st.markdown("### 📘 Knowledge Areas")
    knowledge_rows = knowledge_df[knowledge_df["O*NET-SOC Code"] == selected_code]
    st.dataframe(knowledge_rows[["Element Name", "Scale Name", "Data Value"]])

    # Related Occupations
    st.markdown("### 🤝 Related Occupations")
    related_rows = related_df[related_df["O*NET-SOC Code"] == selected_code]
    st.dataframe(related_rows[["Related O*NET-SOC Code", "Title", "Relation Type"]])
