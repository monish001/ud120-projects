#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
from numpy import NaN, number
from math import isnan

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))


print "Sample feature data for METTS MARK: ", enron_data["METTS MARK"]
print "Feature count per person: ", len(enron_data["METTS MARK"])
chairman = "LAY KENNETH L" # chairman
cfo = "FASTOW ANDREW S" # cfo
person = ceo = "SKILLING JEFFREY K" # ceo
print "Features of ", person, ":"
for feature in enron_data[person]:
    print "    ", feature, enron_data[person][feature]

poi_count = 0
print "List of POI people:"
for person in enron_data:
    #print person
    #print enron_data[person]["poi"]
    if(enron_data[person]["poi"]):
        poi_count = poi_count + 1
        print "    ", poi_count, person

print "Total_count: ", len(enron_data)
print "Poi_count: ", poi_count
    
print "Total_stock_value of James Prentice:", enron_data["PRENTICE JAMES"]["total_stock_value"]
print "From_this_person_to_poi of Wesley Colwell:", enron_data["COLWELL WESLEY"]["from_this_person_to_poi"]
print "Exercised_stock_options of Jeffrey Skilling:", enron_data["SKILLING JEFFREY K"]["exercised_stock_options"]

import math

print enron_data[ceo]["total_payments"]
print enron_data[cfo]["total_payments"]
print enron_data[chairman]["total_payments"]

salaried_count = 0
for person in enron_data:
    #print person
    #print enron_data[person]["poi"]
    
    if(not enron_data[person]["salary"]=="NaN"):
        salaried_count = salaried_count + 1
        #print "    ", salaried_count, person, enron_data[person]["salary"]
print "Total_count of salaried people: ", salaried_count


email_count = 0
for person in enron_data:
    #print person
    #print enron_data[person]["poi"]
    if(not enron_data[person]["email_address"]=="NaN"):
        email_count = email_count + 1
        #print "    ", email_count, person, enron_data[person]["email_address"]
print "Total_count of people with email: ", email_count


total_payment_zero_count = 0
for person in enron_data:
    #print person
    #print enron_data[person]["poi"]
    if(enron_data[person]["total_payments"]=="NaN" or enron_data[person]["total_payments"] == 0):
        total_payment_zero_count = total_payment_zero_count + 1
        #print "    ", total_payment_zero_count, person, enron_data[person]["total_payments"]
print "Total_count of people with zero payments: ", total_payment_zero_count



total_payment_zero_count = 0
for person in enron_data:
    #print person
    #print enron_data[person]["poi"]
    if(enron_data[person]["total_payments"]=="NaN" or enron_data[person]["total_payments"] == 0):
        if(enron_data[person]["poi"]):
            total_payment_zero_count = total_payment_zero_count + 1
            #print "    ", total_payment_zero_count, person, enron_data[person]["total_payments"]
print "Total_count of POI with zero payments: ", total_payment_zero_count



count = 0
for person in enron_data:
    #print person
    #print enron_data[person]["poi"]
    if(enron_data[person]["total_stock_value"]=="NaN" or enron_data[person]["total_stock_value"] == 0):
        if(enron_data[person]["poi"]):
            count = count + 1
            #print "    ", count, person, enron_data[person]["total_payments"]
print "Total_count of POI with zero total stock value: ", count
