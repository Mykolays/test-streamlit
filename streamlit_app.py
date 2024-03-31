import streamlit as st 
import pandas as pd
import plotly.express as px
from get_data import df, all_cycles_daily, all_cycles_monthly
    

st.set_page_config(layout="centered")
st.markdown("# Solar flare analysis")
st.markdown("Lets plot N-S daily flare index to show south - north asymmetry ")
# Create a container for each row
with st.container():
    # Row 1
    with st.container():
        f = px.line(
            df[4], 
            x="Data",
            y=['N-day', 'S minus'],
            title="21 Cycle N-S daily"
        )
        st.plotly_chart(f)

    # Row 2
    with st.container():
        f = px.line(
            df[3], 
            x="Data",
            y=['N-day', 'S minus'],
            title="22 Cycle N-S daily"
        )
        st.plotly_chart(f)

    # Row 3
    with st.container():
        f = px.line(
            df[2], 
            x="Data",
            y=['N-day', 'S minus'],
            title="23 Cycle N-S daily"
        )
        st.plotly_chart(f)

    # Row 4
    with st.container():
        f = px.line(
            df[1], 
            x="Data",
            y=['N-day', 'S minus'],
            title="24 Cycle N-S daily"
        )
        st.plotly_chart(f)

    # Row 5
    with st.container():
        f = px.line(
            df[0].dropna(), 
            x="Data",
            y=['N-day', 'S minus'],
            title="25 Cycle N-S daily"
        )
        st.plotly_chart(f)

f = px.line(
    all_cycles_monthly, 
    x=all_cycles_monthly.index,
    y="T-day",
    title="All Cycle N-S monthly"
)
st.plotly_chart(f)