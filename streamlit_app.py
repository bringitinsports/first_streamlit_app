import streamlit

streamlit.title('My Parents New Healthy Diner')

streamlit.header('Breakfast Favorites')
streamlit.text('😜Omega 3 & Blueberry Oatmeal')
streamlit.text('🎉Kale, Spinach & Rocket Smoothie')
streamlit.text('🙌Hard-Boiled Free-Range Egg')
streamlit.text('💋🌹 Avocado Toast')

streamlit.header('🎂🤳 Build Your Own Fruit Smoothie 🤦‍♀️🤷‍♀️')

import pandas
my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

# Let's put as pick list here so they can pick the fruit they want to include
fruits_selected = streamlit.multiselect("Pick some fruits:", list(my_fruit_list.index), ['Avocado','Strawberries'])
fruits_to_show = my_fruit_list.loc[fruits_selected]

#display the table on the pages
streamlit.dataframe(fruits_to_show)

#New Section to display fruityvice api response
streamlit.header('🎂🤳 Fruity Fruit Advice! 🤦‍♀️🤷‍♀️')

import requests
fruityvice_response = requests.get("https://fruityvice.com/api/fruit/watermelon")
streamlit.text(fruityvice_response.json())

# take the json versin of the response and normalize it
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
#output it to the screen as a table
streamlit.dataframe(fruityvice_normalized)
