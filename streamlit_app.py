import streamlit
import requests
import snowflake.connector

import pandas as pd

my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_REGION()")
my_data_row = my_cur.fetchone()
streamlit.text("Hello from Snowflake:")
streamlit.text(my_data_row)

fruityvice_response = requests.get('https://fruityvice.com/api/fruit/watermelon')

streamlit.text(fruityvice_response.json())

streamlit.dataframe(pd.json_normalize(fruityvice_response.json()))
fruit_choice=streamlit.text_input('what fruit would you like information about?','Kiwi')
streamlit.write(fruit_choice)

streamlit.title('snowflake badge2 course')
streamlit.header('🥗 Breakfast Menu')
streamlit.text('Dosa chutney')
streamlit.text('Idly chutney')
streamlit.text('Poori curry')


df=pd.read_csv('https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt')
df.set_index('Fruit',inplace=True)

fruits_selected = streamlit.multiselect("pick some fruits : ", list(df.index),['Apple','Banana'])
df_to_show = df.loc[fruits_selected]

streamlit.dataframe(df_to_show)
