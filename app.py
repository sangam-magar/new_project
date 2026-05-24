import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st
df =sns.load_dataset("penguins")
dtspecies =df.groupby(["species", "sex"])["bill_length_mm"].count().reset_index()
st.title("seaborn dataset analysis")
st.header("penguins  table")
st.write("displaying male and female numberr of penguins with their species")
st.dataframe(dtspecies)
st.table(dtspecies)

#analyzing through chart
st.header("penguin bar graph")
st.write("displaying the male and female numbers with species")
fig, ax=plt.subplots()
sns.barplot(data =dtspecies, x ="species", y="bill_length_mm",  hue ="sex", ax =ax)
st.pyplot(fig)
