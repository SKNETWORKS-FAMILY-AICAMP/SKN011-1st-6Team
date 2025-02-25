import streamlit as st
from streamlit_app import chart_df
import plotly.express as px


chart_df['density_ratio'] = chart_df['density'] / chart_df['car_amount']


fig = px.pie(chart_df, names='city_name', values='density_ratio', title="전국 인구 밀도 대비 자동차 등록 현황")

fig.update_layout(
    width=800,  
    height=800,  
)

st.plotly_chart(fig)
