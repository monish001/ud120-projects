#!/usr/bin/python

import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "r") )
data_dict.pop("TOTAL", 0)
#data_dict.pop("LAVORATO JOHN J", 0)
#data_dict.pop("FREVERT MARK A", 0)
#data_dict.pop("LAY KENNETH L", 0) # OUTLIER (FREAK POINT)
#data_dict.pop("SKILLING JEFFREY K", 0) # OUTLIER (FREAK POINT)

print "data_dict", data_dict
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
for point in data:
    print "point:", point
    salary = point[0]
    bonus = point[1]
    if(salary > 10000000):
        matplotlib.pyplot.scatter(salary, bonus, color="r")
        print "salary:", salary
        print "bonus:", bonus
    else:
        matplotlib.pyplot.scatter(salary, bonus, color="b")
    
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()



