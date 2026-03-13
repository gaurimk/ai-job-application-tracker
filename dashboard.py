import streamlit as st
import pandas as pd
from tools import (
    add_job_application,
    list_applications,
    update_status,
    delete_application,
    summarize_applications
)

st.title("AI Job Application Tracker")

st.header("Add New Job Application")

company = st.text_input("Company")
role = st.text_input("Role")
status = st.selectbox("Status", ["Applied", "Interview", "Rejected", "Offer"])
date = st.date_input("Application Date")

if st.button("Add Application"):
    add_job_application(company, role, status, str(date))
    st.success("Application added!")

st.header("Job Applications")

jobs = list_applications()

if jobs:
    df = pd.DataFrame(jobs, columns=["ID", "Company", "Role", "Status", "Date"])
    st.dataframe(df, use_container_width=True)
else:
    st.info("No job applications added yet.")

st.header("Update Status")

job_id = st.number_input("Job ID", step=1)
new_status = st.selectbox(
    "New Status", ["Applied", "Interview", "Rejected", "Offer"]
)

if st.button("Update Status"):
    update_status(job_id, new_status)
    st.success("Status updated!")

st.header("Delete Application")

delete_id = st.number_input("Application ID to Delete", step=1)

if st.button("Delete"):
    delete_application(delete_id)
    st.success("Application deleted!")

st.header("Application Summary")

summary = summarize_applications()

if summary:
    summary_df = pd.DataFrame(summary, columns=["Status", "Count"])
    st.bar_chart(summary_df.set_index("Status"))