import warnings
warnings.filterwarnings("ignore")

import pandas as pd

tfidf_vectors = pd.read_excel("./hw4/output table/tfidf_table.xlsx", index_col=0)

# shape vector
tfidf_vectors.shape

#reindex
tfidf_vectors = tfidf_vectors.reindex(sorted(tfidf_vectors.columns), axis=1)

#6 clusters, one for each topic created here
tfidf_vectors['sports_centroid'] = tfidf_vectors['cleaned_9901_sports_tokens_tfidf']
tfidf_vectors['food_centroid'] = tfidf_vectors['cleaned_9902_food_tokens_tfidf']
tfidf_vectors['tech_centroid'] = tfidf_vectors['cleaned_9903_tech_tokens_tfidf']
tfidf_vectors['science_centroid'] = tfidf_vectors['cleaned_9904_science_tokens_tfidf']
tfidf_vectors['business_centroid'] = tfidf_vectors['cleaned_9905_business_tokens_tfidf']
tfidf_vectors['politics_centroid'] = tfidf_vectors['cleaned_9906_politics_tokens_tfidf']

#ITERATION 1
from scipy.spatial.distance import cosine

#creating the distance matrix -- get distance of each vector to each centroid
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

#ITERATION 2 (same thing as iteration 1)
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

# adjusting data to fit into dataFrame
len_s, len_f, len_t, len_sc, len_b, len_p = len(sports_cluster), len(food_cluster), len(tech_cluster), len(science_cluster), len(business_cluster), len(politics_cluster)
max_len = max(len_s, len_f, len_t, len_sc, len_b, len_p)

if not max_len == len_s:
    sports_cluster.extend(['']*(max_len-len_s))
if not max_len == len_f:
    food_cluster.extend(['']*(max_len-len_f))
if not max_len == len_t:
    tech_cluster.extend(['']*(max_len-len_t))
if not max_len == len_sc:
    science_cluster.extend(['']*(max_len-len_sc))
if not max_len == len_b:
    business_cluster.extend(['']*(max_len-len_b))
if not max_len == len_p:
    politics_cluster.extend(['']*(max_len-len_p))

excel = pd.DataFrame.from_dict({'sports_cluster'  :sports_cluster,
            'food_cluster'    :food_cluster,
            'tech_cluster'    :tech_cluster,
            'science_cluster' :food_cluster,
            'business_cluster':business_cluster,
            'politics_cluster':politics_cluster
            }).to_excel("cluster_group_3.xlsx", header=True, index=False)

tfid = pd.DataFrame(tfidf_vectors).to_excel("centroid_group_3.xlsx", header=True, index=True)
