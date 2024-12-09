import streamlit as st
import pandas as pd

st.title("Effective Baking Test")
st.write("Hello User!")


data = {
    'Column1': [1, 2, 3, 4],
    'Column2': ['A', 'B', 'C', 'D']
}
 
df = pd.DataFrame(data)
 
st.write(data)

df.to_csv("data.csv")
         
data = pd.read_csv("data.csv")
