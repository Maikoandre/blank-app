import streamlit as st
import pandas as pd
import numpy as np

st.title("🎈 My streamlit new app")
st.write(
    "Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/)."
)

df = pd.DataFrame({
    'first-column': [1,2,3,4],
    'second-column': [10,20,30,40]
})

st.write(df)

dataframe = np.random.randn(10,20)
st.dataframe(dataframe)

dataframe02 = pd.DataFrame(
    np.random.randn(10,20),
    columns=('col %d' % i for i in range(20))
)

st.dataframe(dataframe02.style.highlight_max(axis=0))

st.table(dataframe02)

char_data = pd.DataFrame(
    np.random.randn(20,3),
    columns=['a','b','c']
)

st.line_chart(char_data)

map_data = pd.DataFrame(
    np.random.randn(1000,2)/[50,50]+[37.76, -122.4],
    columns=['lat', 'lon']
)

st.map(map_data)

x = st.slider('x')
st.write(x, 'squared is', x * x)

st.text_input("Your name", key="name")
st.session_state.name