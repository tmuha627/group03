import string 
import nltk
import os

path = "C:\\Users\\Bryan's Laptop\\hello\\group03"
os.chdir(path)

def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())

for file in os.listdir():
    if file.endswith(".txt"):
        file_path = os.path.join(path, file)

        read_text_file(file_path)          