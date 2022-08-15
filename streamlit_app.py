import streamlit
import requests
fruityvice_response = requests.get('https://fruityvice.com/api/fruit/watermelon')

streamlit.text(fruityvice_response.json())

streamlit.dataframe(pandas.json_normalize(fruityvice_response.json()))

streamlit.title('snowflake badge2 course')
streamlit.header('🥗 Breakfast Menu')
streamlit.text('Dosa chutney')
streamlit.text('Idly chutney')
streamlit.text('Poori curry')

import pandas as pd

df=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
df.set_index('Fruit',inplace=True)

fruits_selected = streamlit.multiselect("pick some fruits : ", list(df.index),['Apple','Banana'])
df_to_show = df.loc[fruits_selected]

streamlit.dataframe(df_to_show)
