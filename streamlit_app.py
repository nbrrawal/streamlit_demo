import streamlit as st
import time
import pytz
from datetime import datetime, timezone

utc_dt = datetime.now(timezone.utc)
nl = '\n'

IND = pytz.timezone("Asia/Kolkata")
FRA = pytz.timezone("Europe/Paris")
USA = pytz.timezone("US/Pacific")   # Las Vegas
RUS = pytz.timezone("Europe/Moscow")
SGP = pytz.timezone("Asia/Singapore")
AUS = pytz.timezone("Australia/Sydney")

# Display the current time
st.title('World Clocks ')
current_time = datetime.now().strftime("%H:%M:%S")
col1, col2, col3 = st.columns(3)

with col1:
    st.title("Delhi")
    st.write(utc_dt.astimezone(IND).strftime('%A %d. %B %Y'))
    st.write(utc_dt.astimezone(IND).strftime('%H:%M:%S'))
    st.title("RUS")
    st.write(utc_dt.astimezone(RUS).strftime('%A %d. %B %Y'))
    st.write(utc_dt.astimezone(RUS).strftime('%H:%M:%S'))
with col2:
    st.title("France")
    st.write(utc_dt.astimezone(FRA).strftime('%A %d. %B %Y'))
    st.write(utc_dt.astimezone(FRA).strftime('%H:%M:%S'))
    st.title("SGP")
    st.write(utc_dt.astimezone(SGP).strftime('%A %d. %B %Y'))
    st.write(utc_dt.astimezone(SGP).strftime('%H:%M:%S'))
with col3:
    st.title("USA")
    st.write(utc_dt.astimezone(USA).strftime('%A %d. %B %Y'))
    st.write(utc_dt.astimezone(USA).strftime('%H:%M:%S'))
    st.title("AUS")
    st.write(utc_dt.astimezone(AUS).strftime('%A %d. %B %Y'))
    st.write(utc_dt.astimezone(AUS).strftime('%H:%M:%S'))

# Sleep for 5 seconds before rerunning
time.sleep(1)
st.experimental_rerun()
