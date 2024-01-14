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


st.header("World Clocks")
#markdown('<h1> <center>World Clocks</h1>', unsafe_allow_html=True)

current_time = datetime.now().strftime("%H:%M:%S")
col1, col2, col3 = st.columns(3)

with col1:
    st.header("Delhi")
    strprint = utc_dt.astimezone(IND).strftime('%A %d. %B %Y')
    st.markdown(f'***:blue[{strprint}]***.')
    strprint = utc_dt.astimezone(IND).strftime('%H:%M:%S')
    st.markdown(f'**:red[{strprint}]**')
    st.header("RUS")
    strprint = utc_dt.astimezone(RUS).strftime('%A %d. %B %Y')
    st.markdown(f'***:blue[{strprint}]***.')
    strprint = utc_dt.astimezone(RUS).strftime('%H:%M:%S')
    st.markdown(f'**:red[{strprint}]**')
with col2:
    st.header("France")
    strprint = utc_dt.astimezone(FRA).strftime('%A %d. %B %Y')
    st.markdown(f'***:blue[{strprint}]***.')
    strprint = utc_dt.astimezone(FRA).strftime('%H:%M:%S')
    st.markdown(f'**:red[{strprint}]**')
    st.header("SGP")
    strprint = utc_dt.astimezone(SGP).strftime('%A %d. %B %Y')
    st.markdown(f'***:blue[{strprint}]***.')
    strprint = utc_dt.astimezone(SGP).strftime('%H:%M:%S')
    st.markdown(f'**:red[{strprint}]**')
with col3:
    st.header("USA")
    strprint = utc_dt.astimezone(USA).strftime('%A %d. %B %Y')
    st.markdown(f'***:blue[{strprint}]***.')
    strprint = utc_dt.astimezone(USA).strftime('%H:%M:%S')
    st.markdown(f'**:red[{strprint}]**')
    st.header("AUS")
    strprint = utc_dt.astimezone(AUS).strftime('%A %d. %B %Y')
    st.markdown(f'***:blue[{strprint}]***.')
    strprint = utc_dt.astimezone(AUS).strftime('%H:%M:%S')
    st.markdown(f'**:red[{strprint}]**')

# Sleep for 5 seconds before rerunning
time.sleep(1)
st.rerun()
