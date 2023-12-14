import os
import numpy as np
import pandas as pd
import time
import re
from sklearn.feature_extraction.text import CountVectorizer
from nltk.corpus import stopwords

# preprocess the articles
def preprocess(text):
    #define stopwords
    stop_words = set(stopwords.words('english'))

    #remove punctuation and numbers
    text = re.sub(r'[^a-zA-Z\s%]|(?<!\d)\d{1,3}(?!\d)|\b\d{4}\b', '', text)

    #remove stopwords
    words = [word for word in text.split() if word.lower() not in stop_words]
    return ' '.join(words)



# create the document term matrix
def create_doc_term_matrix(folder_path):
    subdirectory_path = os.path.join(folder_path, 'cleaned articles')
    file_list = os.listdir(subdirectory_path)

    vectorizer = CountVectorizer()

    document_content_list = []
    doc_name = []

    for file in file_list:
        file_path = os.path.join(subdirectory_path, file)
        with open(file_path, 'r', encoding='utf-8') as file:
            doc = file.read()
            preprocessed_doc = preprocess(doc)
            document_content_list.append(preprocessed_doc)
            file_name = os.path.basename(file_path)
            file_name = os.path.splitext(file_name)[0]
            doc_name.append(file_name)

    dtm = vectorizer.fit_transform(document_content_list)

    terms = vectorizer.get_feature_names_out()
    matrix = dtm.toarray()
    matrix = np.array(matrix)

    dt_dataframe = pd.DataFrame(data=matrix,
                                columns=terms,
                                index=doc_name)

    print("Terms:", terms)
    print("Doc-Term Matrix: ")
    print(matrix)
    dt_dataframe.to_csv('output.csv', index=True)
    
    #create the U,D,VT
    U, D, VT = np.linalg.svd(matrix, full_matrices=False)

    print('Here is original matrix:\nMatrix =\n',matrix, "\n")
    print('Here is matrix U:\nU =\n',np.round(U, decimals=2),"\n")
    print('Here is matrix Σ:\nΣ =\n',np.round(np.diag(D), decimals=2),"\n")
    print('Here is the diagonal of matrix Σ:\nΣ =\n',np.round(D, decimals=2),"\n")
    print('Here is matrix VT:\nVT =\n',np.round(VT, decimals=2),"\n")

    #check if we can remake the original matrix using U,Σ,VT
    remake = (U @ np.diag(D) @ VT)
    print('original matrix remade:\nremade = \n', np.round(remake, decimals=2))
    time.sleep(.5)

    # get number of topics
    k = 5

    topic_names=["Tech", "Sports", "Business/Politics", "Food", "Science"]

    U_k = U[:, :k]
    D_k = np.diag(D[:k])
    VT_k = VT[:k, :]

    # Topic model
    topic_model = U_k @ D_k @ VT_k

    print(np.round(topic_model, decimals=2))

    topic_data = {topic_name: [] for topic_name in topic_names}
    topic_doc_data = {topic_name: [] for topic_name in topic_names}

    # Show the top terms for each topic
    for i, topic in enumerate(VT_k):
        index = topic.argsort()[-20:][::-1]
        top_terms = [terms[idx] for idx in index]
        topic_name = topic_names[i]
        topic_data[topic_name].extend(top_terms)

    df = pd.DataFrame(topic_data)
    df.to_excel('LSA_group_3.xlsx', index=False)

    for i, preprocessed_doc in enumerate(doc_name):
        doc_vector = U_k[i, :]
        doc_topic = np.argmax(doc_vector)
        topic_name = topic_names[doc_topic]
        topic_doc_data[topic_name].append(preprocessed_doc)
    
    doc_topic_matrix = pd.DataFrame.from_dict(topic_doc_data, orient='index').transpose()
    doc_topic_matrix.to_excel('articles_topicized_group_3.xlsx', index=False)

folder_path = 'hw4'

create_doc_term_matrix(folder_path)



