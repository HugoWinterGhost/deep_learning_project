import streamlit as st

st.set_page_config(page_title = "Description du projet", layout = "wide")

st.title('Description du projet')

@st.cache_data
def load_Infos(subtitle, description):
  st.subheader(subtitle)
  st.text(description)

titles = [
  'Type de projet',
  'Technos utilisés',
  'Méthodologie de travail',
  'Source de donnée utilisée',
  'Objectifs',
]
description = [
  'Système de recommandation d\'offres d\'emplois en fonction de profils Linkedin',
  '- Langage : Python \n- Outil : Github \n- Modèle de classification : Apprentissage Non supervisé, Clustering car on n\'avait pas de Label',
  '- Daily Meeting \n- Répartitions des taches : on avançait ensemble tâche par tâche',
  'Kaggle : https://www.kaggle.com/datasets/killbot/linkedin-profiles-and-jobs-data (pas besoin de scrapping)',
  'Le but du projet était de donner des recommendations de postes à pourvoir, pour certains profils Linkedin',
]

for x in range(len(titles)):
  load_Infos(titles[x], description[x])