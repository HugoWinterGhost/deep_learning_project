import streamlit as st

st.set_page_config(page_title = "Données de recommandation de profils Linkedin", layout = "wide")

st.title('Préparation des données')

# companyFollowerCount remplacer les vlauers nulles par des 0 et supprimer les vlaeurs égales à 0 - done
# companyHasLogo remplacer les valeurs null par True ou False si y a une image ou pas - done
# companyName virer les 2 lignes nulles - done
# companyStaffCount remplacer les nulles par la médiane 50% qui est de 1269 et supprimer les vlaeurs égales à 0 - done
# genderEstimate faire un random de 66 % de H et 34% de F avec numpy - done
# jobStartDate virer les 16 lignes nulles - done
# avgEmployeeJobDuration virer les valeurs nulles et virer aussi celle qui sont en dessous ou égale de 0 - done
# avgCompanyJobDuration virer les valeurs nulles et virer aussi celle qui sont en dessous ou égale de 0 - done
# renommage et supression des colonnes - done
# supression des lignes dupliqués
# Encodage des labels
# Fusion de pluisuers mots en une seul mot

@st.cache_data
def load_Infos(subtitle, description):
  st.subheader(subtitle)
  st.text(description)

titles = [
  'Suppression des valeurs nulles',
  'Remplacement de certaines valeurs',
  'Renomage des colonnes',
  'Uniformisation de Location',
  'Suppression des colonnes inutiles',
  'Supression des lignes dupliqués',
  'Transformation des données',
]
description = [
  'Colonnes concernées : companyFollowerCount, companyName, jobStartDate, avgEmployeeJobDuration, avgCompanyJobDuration',
  'Remplacement : \nDes valeurs null dans la colonne companyHasLogo, par True ou False, si une image est présente ou non, au lieu d\'avoir le lien de l\'image. \nDans companyStaffCount remplacer les valeurs null par la mediane qui est de 1269 et supprimer la lignes contenant un 0. \nRemplacer les valeurs non renseignée par un random entre Male et Female, en respectant le pourcentage des deux deja présent qui est de 66% et 33%. \n',
  'Renomage des colonnes pour qu\'elles soient plus simples a comprendre exemple de avgMemberPosDuration qui deviens avgEmployeeJobDuration',
  'Puisque les données sont toutes en Australie on a enlever le pays et la region des colonnes EmployeeLocation et CompanyLocation',
  'Colonnes concernées : Year_Birth, Dt_Customer, Z_CostContact, Z_Revenue, ID, Complain',
  'Supprimer les lignes qui étaient exactement les mêmes',
  'Normalisation des données numérique grace a la fonction minMaxScaler',
]

for x in range(len(titles)):
  load_Infos(titles[x], description[x])
