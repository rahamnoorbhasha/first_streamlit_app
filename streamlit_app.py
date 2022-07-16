import streamlit
streamlit.title('snowflake badge2 course')
streamlit.header('🥗 Breakfast Menu')
streamlit.text('Dosa chutney')
streamlit.text('Idly chutney')
streamlit.text('Poori curry')

import pandas as pd

df=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
df.set_index('Fruit',inplace=True)

streamlit.multiselect("pick some fruits : ", list(df.index),['Apple','Banana'])
streamlit.dataframe(df)
