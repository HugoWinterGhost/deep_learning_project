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

st.checkbox("Utiliser la largeur du conteneur", value = True, key = "use_container_width")
initial_df = load_dataset('./data/linkedin_data.csv')
updated_df = load_dataset('./data/updated_linkedin_data.csv')

st.subheader("Dataset Original")
showDataset(initial_df, 1)
st.markdown(f"Le dataset original contient {len(initial_df)} lignes et {len(initial_df.columns)} colonnes. ")

st.subheader("Dataset Nettoyé")
showDataset(updated_df, 2)
st.markdown(f"Après avoir nettoyé les données, on obtient un dataset de {len(updated_df)} lignes et {len(updated_df.columns)} colonnes.")


st.write(list(initial_df.columns))