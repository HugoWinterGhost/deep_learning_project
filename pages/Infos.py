import streamlit as st

st.set_page_config(page_title = "Données de recommandation de profils Linkedin", layout = "wide")

st.title('Préparation des données')

# companyHasLogo remplacer les valeurs null par True ou False si y a une image ou pas - done
# companyStaffCount remplacer les nulles par la médiane 50% qui est de 1269 et supprimer les vlaeurs égales à 0 - done
# genderEstimate faire un random de 66 % de H et 34% de F avec numpy - done

@st.cache_data
def load_Infos(subtitle, description):
  st.subheader(subtitle)
  st.text(description)

titles = [
  'Suppression des valeurs nulles',
  'Remplacement de certaines valeurs',
  'Renomage des colonnes',
  'Uniformisation de données de localisation',
  'Suppression des colonnes peu pertinentes',
  'Supression des lignes dupliqués',
  'Transformation des données',
]


description = [
  'Colonnes concernées : companyFollowerCount, companyName, jobStartDate, avgEmployeeJobDuration, avgCompanyJobDuration',
  'Remplacement des valeurs nulles par des valeurs plus représentatives de notre DataFrame : \n- Les valeurs des colonnes companyHasLogo et hasPicture ont été remplacées par True ou False, en fonction de la présence ou non d\'une image \n- Les valeurs nulles de la colonne companyStaffCount ont été remplacé par la médiane qui est de 1269 \n- Les valeurs nulles de la colonne genderEstimate ont été remplacées par une valeur aléatoire entre Male et Female, \n  en respectant les proprotions du DataFrame, représentées par les probabilités suivantes H : 66%, F : 33%',
  'Renomage des colonnes suivantes pour qu\'elles soient plus simples a comprendre : \n- posLocation => jobLocation, posTitle => jobTitle, startDate => jobStartDate, endDate => jobEndDate \n- avgMemberPosDuration => avgEmployeeJobDuration, avgCompanyPosDuration => avgCompanyJobDuration \n- mbrLocation => employeeLocation, mbrTitle => employeeTitle',
  'Puisque les données sont toutes en Australie, on a enlever le pays, la région pour ne garder que la ville pour les colonnes suivantes : \n- EmployeeLocation et JobLocation',
  'Colonnes concernées : Unnamed, companyUrl, companyUrn, country, followable, isPremium, mbrLocationCode, memberUrn, posLocationCode, positionId',
  'Supression des lignes qui étaient exactement les mêmes',
  'Normalisation des données numérique grace a la fonction minMaxScaler lors de la vectorisation des données',
]

for x in range(len(titles)):
  load_Infos(titles[x], description[x])