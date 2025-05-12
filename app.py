import streamlit as st
from utils.onet_loader import load_occupations, load_related, load_knowledge, load_skills

st.set_page_config(page_title="Career Path Map Lite", layout="wide")

st.title("🧭 Career Path Map (Lite)")

occupations_df = load_occupations()
related_df = load_related()
knowledge_df = load_knowledge()
skills_df = load_skills()

job_input = st.text_input("Enter a job title:", "Data Analyst")

match = occupations_df[occupations_df['Title'].str.contains(job_input, case=False, na=False)]

if not match.empty:
    job_row = match.iloc[0]
    onet_code = job_row["O*NET-SOC Code"]
    st.subheader(f"🎯 Career: {job_row['Title']}")
    st.markdown(f"**O*NET Code:** {onet_code}")

    st.subheader("🔄 Related Careers")
    related_jobs = related_df[related_df['O*NET-SOC Code'] == onet_code]
    st.write(related_jobs[['Related O*NET-SOC Code', 'Title']])

    st.subheader("📘 Knowledge Required")
    st.write(knowledge_df[knowledge_df['O*NET-SOC Code'] == onet_code][['Element Name', 'Scale Name', 'Data Value']])

    st.subheader("💡 Skills Required")
    st.write(skills_df[skills_df['O*NET-SOC Code'] == onet_code][['Element Name', 'Scale Name', 'Data Value']])
else:
    st.warning("No job found. Try a broader title like 'Analyst' or 'Manager'.")
