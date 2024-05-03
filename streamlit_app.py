import streamlit as st
import subprocess

def google_chrome():
    try:
        # Execute the PowerShell command to upgrade the application as admin
        subprocess.run(["cmd","winget", "upgrade", "Chrome", "--disable-interactivity"], check=True)
        st.success("Application updated successfully.")
    except subprocess.CalledProcessError as e:
        st.error(f"No New Updates Available")

def microsoft_edge():
    try:
        # Execute the PowerShell command to upgrade the application as admin
        subprocess.run(["winget", "upgrade", "Edge", "--disable-interactivity"], check=True)
        st.success("Application updated successfully.")
    except subprocess.CalledProcessError as e:
        st.error(f"No New Updates Available")
def microsoft_teams():
    try:
        # Execute the PowerShell command to upgrade the application as admin
        subprocess.run(["winget", "upgrade", "Teams", "--disable-interactivity"], check=True)
        st.success("Application updated successfully.")
    except subprocess.CalledProcessError as e:
        st.error(f"No New Updates Available")

# Streamlit app setup
st.title("Applicaiton Update Manager")
st.write("Click on the below buttons to update your application")

if st.button("Google Chrome"):
    google_chrome()
if st.button("Microsoft Edge"):
    microsoft_edge()
if st.button("Microsoft Teams"):
    microsoft_teams()

