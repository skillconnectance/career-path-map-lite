import streamlit as st
import pandas as pd

# Load O*NET data
@st.cache_data
def load_data():
    occupation_df = pd.read_csv("data/Occupation Data.csv", sep="\t")
    related_df = pd.read_csv("data/Related Occupations.csv", sep="\t")
    knowledge_df = pd.read_csv("data/Knowledge.csv", sep="\t")
    skills_df = pd.read_csv("data/Skills.csv", sep="\t")
    return occupation_df, related_df, knowledge_df, skills_df

occupation_df, related_df, knowledge_df, skills_df = load_data()

st.title("O*NET Explorer")
st.write("Explore occupations, their related skills, and knowledge areas.")

# Let user select an occupation
occupation = st.selectbox("Select an Occupation:", occupation_df["Title"].unique())

# Get Occupation Code
code = occupation_df[occupation_df["Title"] == occupation]["O*NET-SOC Code"].values[0]

st.subheader("Related Occupations")
related = related_df[related_df["O*NET-SOC Code"] == code]
st.dataframe(related[["Related Occupation"]])

st.subheader("Key Knowledge Areas")
know = knowledge_df[knowledge_df["O*NET-SOC Code"] == code].sort_values("Importance", ascending=False)
st.dataframe(know[["Element Name", "Scale", "Importance"]])

st.subheader("Key Skills")
skills = skills_df[skills_df["O*NET-SOC Code"] == code].sort_values("Importance", ascending=False)
st.dataframe(skills[["Element Name", "Scale", "Importance"]])
