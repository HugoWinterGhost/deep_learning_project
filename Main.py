import streamlit as st
import pandas as pd

st.set_page_config(page_title = "Système de recommandation de profils Linkedin", layout = "wide")

st.title('Jeu de donnée utilisé')

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

st.markdown("""
  <style>
    .st-cr {
      cursor: pointer !important;
    }
    .st-cb {
      background-color: #005A9C !important;
      border: none !important;
    }
    .st-bz, .st-c0, .st-c1, .st-c2 {
      border: none !important;
    }
  </style>
""", unsafe_allow_html = True)

st.checkbox("Utiliser la largeur du conteneur", value = True, key = "use_container_width")
with st.spinner('Chargement des données en cours...'):
  initial_df = load_dataset('./data/linkedin_data.csv')
  updated_df = load_dataset('./data/updated_linkedin_data.csv')

st.subheader("Dataset Original")
showDataset(initial_df, 1)
st.markdown(f"Le dataset original contient {len(initial_df)} lignes et {len(initial_df.columns)} colonnes. ")

st.subheader("Dataset Nettoyé")
showDataset(updated_df, 2)
st.markdown(f"Après avoir nettoyé les données, on obtient un dataset de {len(updated_df)} lignes et {len(updated_df.columns)} colonnes.")
