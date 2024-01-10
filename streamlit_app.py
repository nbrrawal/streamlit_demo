import streamlit as st
import time
import pytz
from datetime import datetime, timezone
# from tzlocal import get_localzone


def get_current_time():
    return time.strftime("%H:%M:%S")

# UI elements
# user_count+1

# user_count = user_count+1

# Streamlit app


st.title(" Real Time clock Demo 1")
st.divider()
st.write("Delhi Time Now : ")
time_container = st.empty()

while True:
    utc_dt = datetime.now(timezone.utc)
    IND = pytz.timezone("Asia/Kolkata")
    time_container.write(f" {utc_dt.astimezone(IND).strftime('%A %d. %B %Y %H:%M:%S')}")
    time.sleep(1)

#    current_time = time.strftime("%H:%M:%S")
