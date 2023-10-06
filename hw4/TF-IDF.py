import os
import nltk
import pandas as pd
from nltk.tokenize import word_tokenize
from sklearn.feature_extraction.text import CountVectorizer
nltk.download('punkt')
import math
import numpy

# All Directories
input_directory = "C:/TextMiningProject-Shared/group03/cleaned-articles"
output_directory = "C:/TextMiningProject-Shared/group03/hw4/output directory"
unique_tokens_directory = 'C:/TextMiningProject-Shared/group03/hw4/unique tokens'  # New directory for unique tokens
output_table_directory = 'C:/TextMiningProject-Shared/group03/hw4/output table'  # New directory for the output table


# Function to tokenize a text file
def tokenize_file(input_file_path, output_file_path):
    with open(input_file_path, 'r', encoding='utf-8') as input_file:
        text = input_file.read()
        tokens = word_tokenize(text)
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(' '.join(tokens))

# Create a set to store unique tokens across all files
unique_tokens_set = set()

# Create a list to store the paths of tokenized files
tokenized_file_paths = []

# Create a dictionary to store token frequency across articles
token_frequency = {}

# Create a dictionary to store corpus-specific term frequency for each token
corpus_term_frequency = {}

# Loop through all text files in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.txt'):
        input_file_path = os.path.join(input_directory, filename)
        output_file_path = os.path.join(output_directory, filename.replace('.txt', '_tokens.txt'))
        tokenize_file(input_file_path, output_file_path)
        tokenized_file_paths.append(output_file_path)  # Store the path of the tokenized file
        
        # Update the set of unique tokens with tokens from the current file
        with open(output_file_path, 'r', encoding='utf-8') as token_file:
            tokens = token_file.read().split()
            unique_tokens_set.update(tokens)
            
            # Update token frequency for each token
            for token in tokens:
                if token in token_frequency:
                    token_frequency[token] += 1
                else:
                    token_frequency[token] = 1

# Sort unique tokens alphabetically
sorted_unique_tokens = sorted(unique_tokens_set)

# Save all unique tokens to a single output file in the "unique_tokens" directory
output_file_path = os.path.join(unique_tokens_directory, 'all_unique_tokens.txt')
with open(output_file_path, 'w', encoding='utf-8') as output_file:
    output_file.write(' '.join(sorted_unique_tokens))

# Initialize CountVectorizer
count_vectorizer = CountVectorizer(vocabulary=sorted_unique_tokens)

# Create a list to store data for the table
table_data = []

# Process each text file using CountVectorizer
for file_path in tokenized_file_paths:
    filename = os.path.basename(file_path)
    article_id = os.path.splitext(filename)[0]
    
    with open(file_path, 'r', encoding='utf-8') as input_file:
        text = input_file.read()
        
        # Transform the text into a document-term matrix
        document_term_matrix = count_vectorizer.transform([text])
        
        # Convert the document-term matrix into a dictionary
        word_counts = dict(zip(sorted_unique_tokens, document_term_matrix.toarray()[0]))
        
        # Append the data for the table, including corpus-specific term frequency
        table_data.append([article_id] + [word_counts[token] for token in sorted_unique_tokens])

# Create a DataFrame for the table
column_names = ['Article ID'] + sorted_unique_tokens

table_df = pd.DataFrame(data=table_data, columns=column_names)

# Calculate corpus-specific term frequency and add a new row
corpus_term_freq = [token_frequency[token] for token in sorted_unique_tokens]
table_df.loc[len(table_df)] = ['corpus_term_freq'] + corpus_term_freq

# Calculate IDF values and add a new row
num_documents = len(tokenized_file_paths)
idf_values = [math.log(num_documents / (1 + token_frequency[token])) for token in sorted_unique_tokens]
table_df.loc[len(table_df)] = ['idf'] + idf_values

# Save the DataFrame to a CSV file in the "output_table" directory
output_table_path = os.path.join(output_table_directory, 'token_count_table.csv')
table_df.to_csv(output_table_path, index=False)

print("Tokenization, extraction of unique tokens, token frequency calculation, table creation, corpus term frequency, and IDF added completed.")
