import streamlit as st
import pandas as pd
import numpy as np

st.title('My first cloud app')
st.write('A simple Datafram')

df=pd.DataFrame(np.random.randn(10,2),columns=['a','b'])
st.dataframe(df)