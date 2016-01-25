#!/usr/bin/python

from time import time
import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture

features_train, labels_train, features_test, labels_test = makeTerrainData()

print 'num of features: ', len(features_train[0])

### the training data (features_train, labels_train) have both "fast" and "slow"
### points mixed together--separate them so we can give them different colors
### in the scatterplot and identify them visually
grade_fast = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==0]
bumpy_fast = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==0]
grade_slow = [features_train[ii][0] for ii in range(0, len(features_train)) if labels_train[ii]==1]
bumpy_slow = [features_train[ii][1] for ii in range(0, len(features_train)) if labels_train[ii]==1]


#### initial visualization
plt.xlim(0.0, 1.0)
plt.ylim(0.0, 1.0)
plt.scatter(bumpy_fast, grade_fast, color = "b", label="fast")
plt.scatter(grade_slow, bumpy_slow, color = "r", label="slow")
plt.legend()
plt.xlabel("bumpiness")
plt.ylabel("grade")
#plt.show()
################################################################################

# Your algorithm choices are the following:
# k nearest neighbors
# random forest
# adaboost (sometimes also called boosted decision tree)


### your code here!  name your classifier object clf if you want the 
### visualization code (prettyPicture) to show you the decision boundary

# k nearest neighbors
from sklearn import neighbors
n_neighbors = 25
algorithm = 'ball_tree'
weights = 'distance'
p=3
leaf_size = 100
clf = neighbors.KNeighborsClassifier(n_neighbors=n_neighbors, weights=weights, p=p, leaf_size=leaf_size, algorithm=algorithm)
print 'With k=', n_neighbors
print 'algorithm=', algorithm
print 'weight=', weights
print 'p=', p
print 'leaf_size=', leaf_size
clfName = 'KNN'

#Random forest
# from sklearn import ensemble
# criterion = 'gini'
# n_estimators = 55
# clf = ensemble.RandomForestClassifier(criterion=criterion, n_estimators=n_estimators)
# print 'criterion: ', criterion
# print 'n_estimators: ', n_estimators
# clfName = 'Random forest'

#AdaBoost
# from sklearn import ensemble
# algo = 'SAMME'
# clf = ensemble.AdaBoostClassifier(algorithm=algo)
# print 'Algo=', algo
# clfName = 'AdaBoost'

t0 = time()
print "Training the model"
clf.fit(features_train, labels_train)
print "Fit time: ", time() - t0

t1 = time()
labels_pred = clf.predict(features_test)
print "Predict time: ", time() - t1

from sklearn import metrics
accuracy = metrics.accuracy_score(labels_test, labels_pred)
print 'accuracy: ', accuracy, '. Classifier: ', clfName, clf





#try:
#    prettyPicture(clf, features_test, labels_test)
#except NameError:
#    pass
