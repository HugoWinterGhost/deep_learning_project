import spacy
import pandas as pd
import numpy as np

from sklearn.preprocessing import MinMaxScaler
from sklearn.cluster import KMeans

numeric_cols = ['ageEstimate', 'companyFollowerCount', 'companyStaffCount', 'connectionsCount', 'followersCount', 'avgEmployeeJobDuration', 'avgCompanyJobDuration']
text_cols = ['companyName', 'employeeLocation', 'employeeTitle', 'jobLocation', 'jobTitle']

def concat_vectors(row):
  num_vector = np.array(row[numeric_cols].values, dtype = np.float64)
  text_vector = np.concatenate([row[col] for col in text_cols])
  return np.concatenate((num_vector, text_vector))

def init_config(linkedin_simple):
  n_clusters = 4
  feature_matrix = np.stack(linkedin_simple['feature_vector'].values)

  kmeans = KMeans(n_clusters = n_clusters, n_init = 4, random_state = 42)
  kmeans.fit(feature_matrix)

  scaler = MinMaxScaler()
  nlp = spacy.load('en_core_web_sm')
  return (scaler, nlp, kmeans)

def recommend_profiles(linkedin_simple, job, nb_recommendations):
  init_config(linkedin_simple)

  (scaler, nlp, kmeans) = job_df = pd.DataFrame([job])

  for col in linkedin_simple.columns:
    if col not in job_df.columns:
      job_df[col] = np.nan

  job_df[numeric_cols] = scaler.transform(job_df[numeric_cols])
      
  for col in text_cols:
    job_df[col] = job_df[col].astype(str).apply(lambda x: nlp(x).vector)

  job_df['feature_vector'] = job_df.apply(concat_vectors, axis = 1)
  job_vector = np.stack(job_df['feature_vector'].values)

  job_cluster = kmeans.predict(job_vector)

  profiles_cluster = np.where(kmeans.labels_ == job_cluster)[0]
  recommended_profiles = np.random.choice(profiles_cluster, size = nb_recommendations)

  return linkedin_simple.iloc[recommended_profiles]
