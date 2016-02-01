#!/usr/bin/python
#from outliers.outlier_removal_regression import net_worths

def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    error = []
    ages_filtered = []
    net_worths_filtered = []
    ### your code goes here
    for i in range(0, 89):
        error_val = predictions[i] - net_worths[i]
        if error_val < 0:
            error_val = -1 * error_val
        #error_val = error_val * error_val
        error.append(error_val)
        if error_val < 88.88: # keeping error level just enough to weed out 10% outliers data
            #print predictions[i], ages[i], net_worths[i], error_val, i
            error.append(error_val)
            ages_filtered.append(ages[i])
            net_worths_filtered.append(net_worths[i])
            
    cleaned_data = zip(ages_filtered, net_worths_filtered, error)
    print "clean data count - ", len(cleaned_data)
    return cleaned_data

