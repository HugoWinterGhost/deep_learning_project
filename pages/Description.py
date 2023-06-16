import streamlit as st

st.set_page_config(page_title = "Description du projet", layout = "wide")

st.title('Description du projet')

@st.cache_data
def load_Infos(subtitle, description):
  st.subheader(subtitle)
  st.text(description)

titles = [
  'Technos utilisés',
  'Source de donnée utilisé',
]
description = [
  'Python, Apprentissage non supervisé, Clustering',
  'Kaggle (https://www.kaggle.com/datasets/killbot/linkedin-profiles-and-jobs-data)',
]

for x in range(len(titles)):
  load_Infos(titles[x], description[x])