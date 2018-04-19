import math
import pyexcel as pe
from pyexcel.ext import xlsx
from sklearn import datasets, linear_model
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.neural_network import MLPRegressor
from sklearn.datasets import make_regression

import numpy as np

#----------------import training set---------------#
a = pe.get_array(file_name = "updatedtraindata.xlsx")
training= np.array(a)

y_train = training[0:1000, 4]
y_train = np.array(y_train, dtype=float)

x_train = training[0:1000, 0:4]
x_train = np.array(x_train, dtype=float)


#----------------import test set--------------------#
b = pe.get_array(file_name = "updatedtestdatamlp.xlsx")
test = np.array(b)

y_test = test[0:50, 4]
y_test = np.array(y_test, dtype=float)

x_test = test[0:50, 0:4]
x_test = np.array(x_test, dtype=float)

mlp = MLPRegressor(hidden_layer_sizes=50, activation='tanh', max_iter=500, learning_rate_init=0.1, random_state=1, solver='lbfgs', tol=0.001 )


#regr is used for OP_1 and regr1 is used for OP_2

#regr = RandomForestRegressor(max_depth=5, random_state = 0)



#FOR OP_1

# Train the model using the training sets
mlp.fit(x_train, y_train)


# Make predictions using the testing set
y_test_pred = mlp.predict(x_test)
#rounded_y_test_pred = np.array(y_test_pred)
#rounded_y_test_pred = rounded_y_test_pred.rint(rounded_y_test_pred)

rounded_y_test_pred=[]
for n in y_test_pred:
    rounded_y_test_pred.append(int(round(n)))
    
# Make predictions using the training set

print (rounded_y_test_pred)


print
print

print
print('OP_1 Rsq train ', r2_score(y_test, rounded_y_test_pred))
print
print ("Y TEST Below")
print (y_test)

print ("PREDICTION BELOW");
print (rounded_y_test_pred)


