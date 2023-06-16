import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Données de recommandation de profils Linkedin", layout = "wide")

st.title('Présentation des données')

def show_table(subtitle: str, data: list, data_columns: list):
  st.subheader(subtitle)
  df = pd.DataFrame(data, columns = data_columns)
  st.table(df)

data_columns = ['Colonnes', 'Significations']

data_employee = [
  ["ageEstimate", "Age"], ["connectionsCount", "Nombre de connexions Linkedin"], ["country", "Pays"],
  ["followable", "Présence sur les réseaux sociaux"], ["followersCount", "Nombre de followers"], ["genderEstimate", "Genre"],
  ["hasPicture", "Présence d'une photo de profil"], ["isPremium", "Présence d'un compte premium Linkedin"],
  ["mbrLocation", "Adresse de résidence de l'employé"], ["mbrLocationCode", "Code postal de l'employé"],
  ["mbrTitle", "Intitulé du job de l'employé"], ["memberUrn", "URN Linkedin de l'employé"],
]

data_company = [
  ["companyFollowerCount", "Nombre de followers"], ["companyHasLogo", "Présence d'un logo"], ["companyName", "Nom"],
  ["companyStaffCount", "Nombre d'employés"], ["companyUrl", "URL de leur site web"], ["companyUrn", "URN Linkedin"]
]

data_contract = [
  ["startDate", "Date de début"], ["endDate", "Date de fin"], ["posLocation", "Adresse de résidence de l'entreprise"],
  ["posLocationCode", "Code postal de l'entreprise"], ["posTitle", "Intitulé du job recherché"], ["positionId", "Identifiant du contrat"],
  ["avgMemberPosDuration", "Durée moyenne du contrat de l'employé en années"], ["avgCompanyPosDuration", "Durée moyenne du contrat de l'entreprise en années"]
]

show_table("Données de l'employé", data_employee, data_columns)
show_table("Données de l'entreprise", data_company, data_columns)
show_table("Données du contrat", data_contract, data_columns)
