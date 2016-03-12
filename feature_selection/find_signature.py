#!/usr/bin/python

import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "r"))
authors = pickle.load( open(authors_file, "r") )



### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn import cross_validation
features_train, features_test, labels_train, labels_test = cross_validation.train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()

vectorizer_words = vectorizer.get_feature_names()
print 'len vectorizer_words', len(vectorizer_words)


### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
print 'total size of training data ', len(features_train.toarray()) # 15820
features_train = features_train[:150].toarray()
labels_train   = labels_train[:150]



### your code goes here
from time import time
from sklearn import tree
#min_samples_split = 40
#print "min_samples_split", min_samples_split
#criterion = 'entropy'
#print 'criterion', criterion
#clf = tree.DecisionTreeClassifier(min_samples_split=min_samples_split, criterion=criterion)
clf = tree.DecisionTreeClassifier()
t0 = time()
print "Training the model"
clf.fit(features_train, labels_train)
print "Fit time: ", time() - t0

t1 = time()
labels_pred = clf.predict(features_test)
print "Predict time: ", time() - t1

from sklearn import metrics
accuracy = metrics.accuracy_score(labels_test, labels_pred)

print 'Accuracy ', accuracy

print 'len fi ', len(clf.feature_importances_)
print 'feature_importances_'
for index in range(len(clf.feature_importances_)):
    fi = clf.feature_importances_[index]
    if fi>0.1:
        print index, fi, vectorizer_words[index]
    #else:
    #    print index, fi

