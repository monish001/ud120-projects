#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""

import sys
from time import time

sys.path.append("../tools/")
from email_preprocess import preprocess

### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

#########################################################
### your code goes here ###

# features_train = features_train[:len(features_train)/100]
# labels_train = labels_train[:len(labels_train)/100]

from sklearn import svm

# clf = svm.SVC(kernel="linear")
# clf = svm.SVC(kernel="rbf")
C = 10000.
clf = svm.SVC(kernel="rbf", C=C)

t0 = time()
print "Training the model"
clf.fit(features_train, labels_train)
print "Fit time: ", time() - t0

t1 = time()
pred = clf.predict(features_test)
print "Predict time: ", time() - t1

from sklearn.metrics import accuracy_score

accuracy = accuracy_score(labels_test, pred)
print 'Accuracy ', accuracy

print 'Predictions ', pred[10], pred[26], pred[50]

count = 0
for val in pred:
    if val == 1:
        count = count + 1
print "Chris count in test data ", count
#########################################################
