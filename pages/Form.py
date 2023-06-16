import streamlit as st
import pandas as pd

from processing.Model import recommend_profiles

st.set_page_config(page_title = "Formulaire de recommandation de profils Linkedin", layout = "wide")

st.title("Formulaire")

@st.cache_data
def load_dataset(dataset_path):
  return pd.read_csv(dataset_path)

def showDataset(dataset, index):
  cols = st.multiselect('Sélectionner les colonnes : ', dataset.columns, default = [], key = index)
  data_load_state = st.text('Chargement des données...')
  data_load_state.text("Données chargées!")

  if cols == []:
    st.dataframe(dataset, use_container_width = st.session_state.use_container_width)
  else:
    st.dataframe(dataset[cols], use_container_width = st.session_state.use_container_width)

updated_df_simple = load_dataset('./data/updated_linkedin_simple_data.csv')


st.markdown("""
  <style>
    .st-cr {
      cursor: pointer !important;
    }
    .css-1rtsdbg:hover, .css-1rtsdbg:active {
      background-color: #005A9C !important;
      color: #FFFFFF !important;
      border: none !important;
    }
    .css-1a5dplj:hover:enabled, .css-1a5dplj:focus:enabled {
      background-color: #005A9C !important;
    }
  </style>
""", unsafe_allow_html = True)

with st.form("my_form"):
  cols1 = st.columns(3)
  age_estimate = cols1[0].number_input("Age :", value = 32)
  company_follower_count = cols1[1].number_input("Nombre de followers de l'entreprise :", value = 1000)
  company_staff_count = cols1[2].number_input("Nombre d'employés de l\'entreprise :", value = 1200)
  
  st.write("\n")
  cols2 = st.columns(3)
  connections_count = cols2[0].number_input("Nombre de connections linkedin de l'employé :", value = 500)
  followers_count = cols2[1].number_input("Nombre de followers de l'employé :", value = 300)
  avg_employee_job_duration = cols2[2].number_input("Durée moyenne du contrat de l'employé en années :", value = 3)

  companies_name = {1: "Atlassian", 2: "IBM", 3: "Paypal", 4: "Nestlé", 5: "WiseTech Global", 6: "Canva"}
  employees_location = {1: "Sydney", 2: "Melbourne", 3: "Newtown", 4: "Oatlands", 5: "Wangaratta", 6: "Carlton"}
  employee_title = {1: "Data Scientist", 2: "Project Manager", 3: "arketing Manager", 4: "Software Engineer", 5: "Web Developer", 6: "Research Leader"}
   
  def format_companies_name(option):
    return companies_name[option]
   
  def format_employees_location(option):
    return employees_location[option]
  
  def format_employee_title(option):
    return employee_title[option]
   
  st.write("\n")
  cols3 = st.columns(3)
  avg_company_job_duration = cols3[0].number_input("Durée moyenne des contrats de l'entreprise en années :", value = 3)
  selected_companies_name = cols3[1].selectbox("Nom de l'entreprise :", options = companies_name.keys(), format_func = format_companies_name, index = 0)
  selected_job_location = cols3[2].selectbox("Adresse de résidence de l'entreprise :", options = employees_location.keys(), format_func = format_employees_location, index = 0)
  
  st.write("\n")
  cols4 = st.columns(3)
  selected_job_title = cols4[0].selectbox("Intitulé du job recherché :", options = employee_title.keys(), format_func = format_employee_title, index = 0)
  selected_employee_location = cols4[1].selectbox("Adresse de résidence de l'employé :", options = employees_location.keys(), format_func = format_employees_location, index = 0)
  selected_employee_title = cols4[2].selectbox("Intitulé du job de l'employé :", options = employee_title.keys(), format_func = format_employee_title, index = 0)

  st.write("\n")
  submitted = st.form_submit_button("Valider")

if submitted:
  new_job = {
    'ageEstimate': age_estimate, 'companyFollowerCount': company_follower_count, 'companyStaffCount': company_staff_count, 
    'connectionsCount': connections_count, 'followersCount': followers_count, 'avgEmployeeJobDuration': avg_employee_job_duration, 
    'avgCompanyJobDuration': avg_employee_job_duration, 'companyName': companies_name[selected_companies_name], 
    'employeeLocation': employees_location[selected_employee_location], 'employeeTitle': employee_title[selected_employee_title],
    'jobLocation': employees_location[selected_job_location], 'jobTitle': employee_title[selected_job_title]
  }

  with st.spinner('Calcul des recommandations en cours...'):
    recommended_profiles = recommend_profiles(updated_df_simple, new_job, 5)
  
  st.subheader("Profils Recommandés")
  st.checkbox("Utiliser la largeur du conteneur", value = True, key = "use_container_width")
  showDataset(recommended_profiles, 1)
  st.markdown(f"Le dataset contient {len(recommended_profiles)} lignes et {len(recommended_profiles.columns)} colonnes. ")
  st.balloons()
