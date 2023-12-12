import os
import numpy as np
import pandas as pd
import time
from sklearn.feature_extraction.text import CountVectorizer

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
            document_content_list.append(doc)
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
    k = 6

    topic_names=["Politics", "Sports", "Tech", "Food", "Science", "Business"]

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

folder_path = 'hw4'

create_doc_term_matrix(folder_path)



