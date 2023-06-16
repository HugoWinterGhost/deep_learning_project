import streamlit as st

st.set_page_config(page_title = "Données de recommandation de profils Linkedin", layout = "wide")

st.title('Préparation des données')

@st.cache_data
def load_Infos(subtitle, description):
  st.subheader(subtitle)
  st.text(description)

titles = [
  'Suppression des valeurs nulles',
  'Remplacement année de naissance',
  'Fusion des colonnes similaires',
  'Suppression des colonnes inutiles',
  'Filtre sur l\'age',
  'Transformation des données',
]
description = [
  'Colonnes concernées : Income',
  'Remplacement de l\'année de naissance par l\'age en se basant sur l\'année en cours',
  'Colonnes exemple : \nchildren = Kidhome + Teenhome \ntotalSpent = MntWines + MntFruits + MntMeatProducts + MntFishProducts + MntSweetProducts + MntGoldProds \nFusion de AcceptedCmp1, AcceptedCmp2, AcceptedCmp3, AcceptedCmp4, AcceptedCmp5 en Accepted',
  'Colonnes concernées : Year_Birth, Dt_Customer, Z_CostContact, Z_Revenue, ID, Complain',
  'Filtrer les personnes de plus de 100 ans',
  'Encodage des labels suivants : \nEducation : Graduation, Master, 2n Cycle \nMarital_Status : Married, Together, Single, Divorced, Widow, Alone',
]

for x in range(len(titles)):
  load_Infos(titles[x], description[x])
