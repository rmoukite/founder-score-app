import streamlit as st
import pandas as pd

st.title("Founder Score Calculator")

st.markdown("""
This app helps you evaluate startup founders using a weighted score out of 100.  
Fill in the traits and get an instant credibility score for LP and internal use.
""")

# Input fields
founder_name = st.text_input("Founder Name", "Jane Doe")
previous_startups = st.slider("Number of Previous Startups", 0, 5, 1)
exited_startup = st.selectbox("Exited a Startup?", ["No", "Yes"]) == "Yes"
accelerator_alum = st.selectbox("Top Accelerator Alum (YC, Techstars...)?", ["No", "Yes"]) == "Yes"
industry_fit = st.selectbox("Industry Background Match?", ["No", "Yes"]) == "Yes"
roles_gt_2 = st.selectbox("Held >2 Startup Roles?", ["No", "Yes"]) == "Yes"
thought_leadership = st.selectbox("Public Thought Leadership (Talks, Articles)?", ["No", "Yes"]) == "Yes"
hiring_start = st.selectbox("Strong Team Hired Early?", ["No", "Yes"]) == "Yes"
vc_affiliation = st.selectbox("VC or MNC Network Affiliation?", ["No", "Yes"]) == "Yes"

# Scoring logic
score = (
    15 * previous_startups +
    20 * int(exited_startup) +
    10 * int(accelerator_alum) +
    10 * int(industry_fit) +
    10 * int(roles_gt_2) +
    10 * int(thought_leadership) +
    10 * int(hiring_start) +
    15 * int(vc_affiliation)
)
score = min(score, 100)

st.success(f"**Founder Score for {founder_name}: {score}/100**")

# Optional: Table Summary
if st.checkbox("Show Weighted Breakdown"):
    st.write(pd.DataFrame({
        "Category": [
            "Previous Startups", "Exited Startup", "Accelerator Alum", "Industry Fit",
            "Startup Roles > 2", "Thought Leadership", "Strong Hiring Start", "VC/MNC Affiliation"
        ],
        "Score Contribution": [
            15 * previous_startups,
            20 * int(exited_startup),
            10 * int(accelerator_alum),
            10 * int(industry_fit),
            10 * int(roles_gt_2),
            10 * int(thought_leadership),
            10 * int(hiring_start),
            15 * int(vc_affiliation)
        ]
    }))

