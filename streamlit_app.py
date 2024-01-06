import streamlit as st
import time


# NOTE: This must be the first command in your app, and must be set only once
st.set_page_config(layout="wide")


# Function to get the current time
user_count = 0


def get_current_time():
    return time.strftime("%H:%M:%S")

# UI elements
# user_count+1


user_count = user_count+1

# Streamlit app

st.title(" Real clock Demo 1")
st.divider()
st.write("Delhi time Now : ")
time_container = st.empty()

while True:
    current_time = get_current_time()
    time_container.write(f"Current Time: {current_time}")
    time.sleep(1)
