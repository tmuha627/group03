import warnings
warnings.filterwarnings("ignore")

import pandas as pd

tfidf_vectors = pd.read_excel("./hw4/output table/tfidf_table.xlsx", index_col=0)

# shape vector
tfidf_vectors.shape

#setting up clustering
tfidf_vectors = tfidf_vectors[['cleaned_9901_sports_tokens_tfidf','cleaned_0101_sports_tokens_tfidf','cleaned_0102_sports_tokens_tfidf','cleaned_0103_sports_tokens_tfidf',
                               'cleaned_9902_food_tokens_tfidf', 'cleaned_0204_food_tokens_tfidf', 'cleaned_0206_food_tokens_tfidf', 'cleaned_0207_food_tokens_tfidf',
                               'cleaned_9903_tech_tokens_tfidf', 'cleaned_0307_tech_tokens_tfidf', 'cleaned_0301_tech_tokens_tfidf', 'cleaned_0309_tech_tokens_tfidf',
                               'cleaned_9904_science_tokens_tfidf', 'cleaned_science_0409_tokens_tfidf', 'cleaned_science_0412_tokens_tfidf', 'cleaned_science_0403_tokens_tfidf',
                               'cleaned_9905_business_tokens_tfidf', 'cleaned_0501_business_tokens_tfidf', 'cleaned_0514_business_tokens_tfidf', 'cleaned_0516_business_tokens_tfidf',
                               'cleaned_9906_politics_tokens_tfidf', 'cleaned_0520_politics_tokens_tfidf', 'cleaned_0515_politics_tokens_tfidf', 'cleaned_0510_politics_tokens_tfidf']]

tfidf_vectors['sports_centroid'] = tfidf_vectors['cleaned_9901_sports_tokens_tfidf']
tfidf_vectors['food_centroid'] = tfidf_vectors['cleaned_9902_food_tokens_tfidf']
tfidf_vectors['tech_centroid'] = tfidf_vectors['cleaned_9903_tech_tokens_tfidf']
tfidf_vectors['science_centroid'] = tfidf_vectors['cleaned_9904_science_tokens_tfidf']
tfidf_vectors['business_centroid'] = tfidf_vectors['cleaned_9905_business_tokens_tfidf']
tfidf_vectors['politics_centroid'] = tfidf_vectors['cleaned_9906_politics_tokens_tfidf']

tfidf_vectors = tfidf_vectors.reindex(sorted(tfidf_vectors.columns), axis=1)

# show vectors
tfidf_vectors

#ITERATION 1
from scipy.spatial.distance import cosine

#creating the distance matrix
distance_matrix = pd.DataFrame(columns=['sports_centroid','food_centroid','tech_centroid','science_centroid','business_centroid','politics_centroid'])

for col in tfidf_vectors.columns:
    if 'tfidf' in str(col):
        idx = str(col)
        sports_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['sports_centroid']),10)
        food_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['food_centroid']),10)
        tech_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['tech_centroid']),10)
        science_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['science_centroid']),10)
        business_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['business_centroid']),10)
        politics_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['politics_centroid']),10)
        
        distance_matrix.loc[idx] = [sports_dist, food_dist, tech_dist, science_dist, business_dist, politics_dist]


#adding documents in the clusters
sports_cluster = []
food_cluster = []
tech_cluster = []
science_cluster = []
business_cluster = []
politics_cluster = []

for doc in distance_matrix.index:
    
    centroid = distance_matrix.loc[doc].idxmin()

    if 'sports' in str(centroid):
        sports_cluster.append(str(doc))
    
    if 'food' in str(centroid):
        food_cluster.append(str(doc))
        
    if 'tech' in str(centroid):
        tech_cluster.append(str(doc))
        
    if 'science' in str(centroid):
        science_cluster.append(str(doc))
        
    if 'business' in str(centroid):
        business_cluster.append(str(doc))
        
    if 'politics' in str(centroid):
        politics_cluster.append(str(doc))
        
#recalculating the centroids
tfidf_vectors['sports_centroid'] = tfidf_vectors[sports_cluster].sum(axis=1)
tfidf_vectors['food_centroid'] = tfidf_vectors[food_cluster].sum(axis=1)
tfidf_vectors['tech_centroid'] = tfidf_vectors[tech_cluster].sum(axis=1)
tfidf_vectors['science_centroid'] = tfidf_vectors[science_cluster].sum(axis=1)
tfidf_vectors['business_centroid'] = tfidf_vectors[business_cluster].sum(axis=1)
tfidf_vectors['politics_centroid'] = tfidf_vectors[politics_cluster].sum(axis=1)

#ITERATION 2
distance_matrix = pd.DataFrame(columns=['sports_centroid','food_centroid','tech_centroid','science_centroid','business_centroid','politics_centroid'])

for col in tfidf_vectors.columns:
    if 'tfidf' in str(col):
        idx = str(col)
        sports_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['sports_centroid']),10)
        food_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['food_centroid']),10)
        tech_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['tech_centroid']),10)
        science_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['science_centroid']),10)
        business_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['business_centroid']),10)
        politics_dist = round(cosine(tfidf_vectors[col], tfidf_vectors['politics_centroid']),10)
        
        distance_matrix.loc[idx] = [sports_dist, food_dist, tech_dist, science_dist, business_dist, politics_dist]
        
sports_cluster = []
food_cluster = []
tech_cluster = []
science_cluster = []
business_cluster = []
politics_cluster = []

for doc in distance_matrix.index:
    
    centroid = distance_matrix.loc[doc].idxmin()
    
    if 'sports' in str(centroid):
        sports_cluster.append(str(doc))
    
    if 'food' in str(centroid):
        food_cluster.append(str(doc))
        
    if 'tech' in str(centroid):
        tech_cluster.append(str(doc))
        
    if 'science' in str(centroid):
        science_cluster.append(str(doc))
        
    if 'business' in str(centroid):
        business_cluster.append(str(doc))
        
    if 'politics' in str(centroid):
        politics_cluster.append(str(doc))

print(politics_cluster)




