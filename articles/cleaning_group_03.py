import os
import string
import nltk
nltk.download('universal_tagset')
nltk.download('wordnet')
nltk.download('stopwords')
from nltk import word_tokenize, pos_tag
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet
from nltk.corpus import stopwords

#load in article
directory01 = "C:/Users/Tyler/Desktop/Web&Text/group03/articles/group_01_articles"
directory02 = "C:/Users/Tyler/Desktop/Web&Text/group03/articles/group_02_articles"
directory03 = "C:/Users/Tyler/Desktop/Web&Text/group03/articles/group_03_articles"
directory04 = "C:/Users/Tyler/Desktop/Web&Text/group03/articles/group_04_articles"
directory05 = "C:/Users/Tyler/Desktop/Web&Text/group03/articles/group_05_articles"
directory06 = "C:/Users/Tyler/Desktop/Web&Text/group03/articles/professor_articles_initial_centroids"

directoryList = [directory01, directory02, directory03, directory04, directory05, directory06]
for dir in directoryList:
    for files in os.listdir(dir):
        with open(os.path.join(dir, files), encoding="utf-8", errors="ignore") as f:
            ea = f.readlines()
        ea=ea[4:]

        updated_ea = []

        for i in range(len(ea)):
            if ea[i] != '\n':
                updated_ea.append(ea[i].replace('\n', ''))

        for i in range(len(updated_ea)):
            updated_ea[i] = updated_ea[i].lower()

        updated_ea = ' '.join(updated_ea)

        updated_ea = updated_ea.replace('not', 'not_')
        updated_ea = updated_ea.replace("wasn't", "wasn't_")

        updated_ea = ''.join([str(char) for char in updated_ea if char in string.printable])

        text = word_tokenize(updated_ea)

        tagged_article = pos_tag(text, tagset='universal')

        #init the wordnet lemmatizer
        lemmatizer = WordNetLemmatizer()

        lemmatized_sentence = []

        for word in tagged_article:
            mapped_tag = ''

            if word[1] in ['ADJ', 'NOUN', 'VERB', 'ADV']:

                if word[1]=='NOUN':
                    mapped_tag = wordnet.NOUN
                if word[1]=='VERB':
                    mapped_tag = wordnet.VERB
                if word[1]=='ADJ':
                    mapped_tag = wordnet.ADJ
                if word[1]=='ADV':
                    mapped_tag = wordnet.ADV
                
                lemmatized_sentence.append(lemmatizer.lemmatize(word[0], mapped_tag))
            else:
                lemmatized_sentence.append(word[0])

        stops = list(stopwords.words('english')) + ['!', '#', "'s", '(', ')', '5-foot-not_hing', '@']

        article_no_stopwords = []
        article_no_stopwords_2 = []

        for word in lemmatized_sentence:

            if word.casefold() not in stops:
                article_no_stopwords.append(word)

        for word in article_no_stopwords:
            if word.casefold() not in stops:
                article_no_stopwords_2.append(word)

        new_file = open("cleaned_" + files, "w")

        index = 15
        i = 0
        for line in article_no_stopwords_2:
            i += 1
            if(i == index):
                new_file.write("\n")
                i = 0
            new_file.write(line + " ")

        new_file.close()