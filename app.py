import streamlit as st
import streamlit_ext as ste

from datetime import time, datetime, date

option = ste.selectbox(
    "How would you like to be contacted?",
    range(100),
    key="selectbox",
)

st.write("You selected:", option)

d = ste.date_input("When's your birthday", date(2019, 7, 6), key="date_input")
st.write("Your birthday is:", d)

t = ste.time_input("Set an alarm for", time(8, 45), key="time_input")
st.write("Alarm is set for", t)
