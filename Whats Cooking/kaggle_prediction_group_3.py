from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import LabelEncoder
import json
import warnings
from sklearn import metrics
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
import matplotlib.pyplot as plt
import itertools
from sklearn.metrics import confusion_matrix
import numpy as np


print ("Read Dataset ... ")
def read_dataset(path):
    return json.load(open(path)) 


Data = read_dataset('Whats Cooking/trainfile2.json')

#Convert everything to lowercase.  Probably could clean up a little more
def generate_text(data):
    text_data = [" ".join(doc['ingredients']).lower() for doc in data]
    return text_data 

X = generate_text(Data)
Y = [doc['cuisine'] for doc in Data]

for i in range(5):
    print(Y[i],'|',X[i],'\n')

print ("Divide into training and validation sets")
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size=0.20, random_state=42)

print(len(X_train),len(y_train),len(X_test),len(y_test))

#build a tfidf transformer on training set.  use it on testing set.
tfidf = TfidfVectorizer(binary=True)
def tfidf_features(txt, flag):
    if flag == "train":
        x = tfidf.fit_transform(txt)
    else:
        x = tfidf.transform(txt)
    x = x.astype('float32')
    return x 


XX = tfidf_features(X_train, flag="train")
XX_test = tfidf_features(X_test, flag="test")


lb = LabelEncoder()
yy = lb.fit_transform(y_train)

warnings.filterwarnings("ignore") 

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(XX, yy)

yy_test = knn.predict(XX_test)
yy_pred = lb.inverse_transform(yy_test)

# model accuracy, how often is the classifier correct
print("Accuracy:",metrics.accuracy_score(y_test, yy_pred))

class_names =[]
for i in range(len(y_test)):
    if y_test[i] not in class_names:
        class_names.append(y_test[i])


def plot_confusion_matrix(cm, classes,
                          normalize=False,
                          title='Confusion matrix',
                          cmap=plt.cm.Blues):
    if normalize:
        cm = cm.astype('float') / cm.sum(axis=1)[:, np.newaxis]

    plt.imshow(cm, interpolation='nearest', cmap=cmap)
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(len(classes))
    plt.xticks(tick_marks, classes, rotation=45)
    plt.yticks(tick_marks, classes)

    fmt = '.2f' if normalize else 'd'
    thresh = cm.max() / 2.
    for i, j in itertools.product(range(cm.shape[0]), range(cm.shape[1])):
        plt.text(j, i, format(cm[i, j], fmt),
                 horizontalalignment="center",
                 color="white" if cm[i, j] > thresh else "black")

    plt.ylabel('True label')
    plt.xlabel('Predicted label')
    plt.tight_layout()

# run confusion matrix
cnf_matrix = confusion_matrix(y_test, yy_pred)
np.set_printoptions(precision=2)

# plot non-normalized confusion matrix
plt.figure(figsize=(12, 10))
plot_confusion_matrix(cnf_matrix, classes=class_names,
                      title='Confusion matrix, without normalization')

plt.savefig("figure1.pdf", dpi="figure")
# plot normalized confusion matrix
plt.figure(figsize=(12, 10))
plot_confusion_matrix(cnf_matrix, classes=class_names, normalize=True,
                      title='Normalized confusion matrix')

plt.savefig("figure2.pdf", dpi="figure")
plt.show()