import math
import pyexcel as pe
from pyexcel.ext import xlsx
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np

#----------------import training set---------------#
a = pe.get_array(file_name = "updatedtraindata.xlsx")
training= np.array(a)

y_train = training[0:1000, 4]
y_train = np.array(y_train, dtype=float)

x_train = training[0:1000, 0:4]
x_train = np.array(x_train, dtype=float)


#----------------import test set--------------------#
b = pe.get_array(file_name = "updatedtestdatalinreg.xlsx")
test = np.array(b)

y_test = test[0:50, 4]
y_test = np.array(y_test, dtype=float)

x_test = test[0:50, 0:4]
x_test = np.array(x_test, dtype=float)


#regr is used for OP_1 and regr1 is used for OP_2

regr = linear_model.LinearRegression()



#FOR OP_1

# Train the model using the training sets
regr.fit(x_train, y_train)


# Make predictions using the testing set
y_test_pred = regr.predict(x_test)
#rounded_y_test_pred = np.array(y_test_pred)
#rounded_y_test_pred = rounded_y_test_pred.rint(rounded_y_test_pred)

rounded_y_test_pred=[]
for n in y_test_pred:
    rounded_y_test_pred.append(int(round(n)))
    
# Make predictions using the training set




print
print
#Print the coefficients
print('Coefficients for OP_1: ', regr.coef_)
print
print('OP_1 Rsq train ', r2_score(y_test, rounded_y_test_pred))
print

print ("Y TEST ARRAY BELOW")
print (y_test)

print

print ("PREDICTION BELOW")
print (rounded_y_test_pred)


