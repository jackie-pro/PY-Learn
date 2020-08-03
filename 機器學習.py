# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 11:47:39 2020

@author: Jackie
"""

#ex1:
import numpy as np
import pandas as pd 
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

heights = np.array([147.9,163.5,159.8,155.1,163.3,158.7,172.0,161.2,153.9,161.6])
weights = np.array([41.7,60.2,47.0,53.2,48.3,55.2,58.5,49.0,46.7,52.5])

x = pd.DataFrame(heights, columns=["Heights"])
y = pd.DataFrame(weights, columns=["Weights"])


lm = LinearRegression()
lm.fit(x,y)
print("迴歸係數",lm.coef_)
print("截距",lm.intercept_)

#預測身高 155、165、180的體重
new_heights = pd.DataFrame(np.array([155,165,180]))
predicted_weights = lm.predict(new_heights)
print(predicted_weights)

#圖示
plt.scatter(heights,weights)
regression_weights = lm.predict(x)
plt.plot(heights,regression_weights,color='blue')
plt.plot(new_heights,predicted_weights,color='red',marker='o',markersize=10)
plt.show()

#ex2:
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

diabetes = datasets.load_diabetes()

print(diabetes.keys())
X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
print(X)
target = pd.DataFrame(diabetes.target, columns=['MEDV'])
print(target.head())

y = target['MEDV']
print(y)
lm = LinearRegression()
lm.fit(X,y)
print("迴歸係數",lm.coef_)
print("截距",lm.intercept_ )
predicted_target = lm.predict(X)
print(predicted_target[0:5])

plt.scatter(y , predicted_target)
plt.xlabel('Target')
plt.ylabel('Predicted_target')
plt.show()


df = X[['age','sex','bmi','bp']]
print(df)
lm = LinearRegression()
lm.fit(df,y)
print("迴歸係數",lm.coef_)
print("截距",lm.intercept_ )
predicted_target = lm.predict(df)
print(predicted_target[0:5])

plt.scatter(y , predicted_target)
plt.xlabel('Target(Age,Sex,Bmi,Bp)')
plt.ylabel('Predicted_target(Age,Sex,Bmi,Bp)')
plt.show()




#ex3:
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np

diabetes = datasets.load_diabetes()
print(diabetes.keys())

X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
print(X)

target = pd.DataFrame(diabetes.target, columns=['MEDV'])
print(target.head())

y = target['MEDV']
print(y)


lm = LinearRegression()
lm.fit(X,y)

print("迴歸係數",lm.coef_)
print("截距",lm.intercept_ )
predicted_target = lm.predict(X)
print(predicted_target[0:5])

MSE = np.mean((y-predicted_target)**2)
print('MSE',MSE)
print('R-squared:',lm.score(X,y))
#===============
plt.scatter(y , predicted_target)
plt.xlabel('Target')
plt.ylabel('Predicted_target')
plt.show()
#=====================
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

diabetes = datasets.load_diabetes()
#print(diabetes.keys())

X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
#print(X)
y = pd.DataFrame(diabetes.target, columns=['MEDV'])
#print(y)

XTrain, XTest, yTrain, yTest = train_test_split(X,y,test_size = 0.33, random_state=100)

lm = LinearRegression()
lm.fit(XTrain,yTrain)

pred_train = lm.predict(XTrain)
pred_test = lm.predict(XTest)

MSE_train = np.mean((yTrain-pred_train)**2)
MSE_test = np.mean((yTest-pred_test)**2)
#print('訓練資料的MSE:', MSE_train)
print('測試資料的MSE:', MSE_test)

#print('訓練資料的R-squared:', lm.score(XTrain,yTrain))
print('測試資料的R-squared:', lm.score(XTest,yTest))

#=====================
import pandas as pd
from sklearn import datasets
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
import numpy as np

diabetes = datasets.load_diabetes()
#print(diabetes.keys())

X = pd.DataFrame(diabetes.data, columns=diabetes.feature_names)
#print(X)
y = pd.DataFrame(diabetes.target, columns=['MEDV'])
#print(y)

XTrain, XTest, yTrain, yTest = train_test_split(X,y,test_size = 0.25, random_state=100)

lm = LinearRegression()
lm.fit(XTrain,yTrain)

pred_train = lm.predict(XTrain)
pred_test = lm.predict(XTest)

MSE_train = np.mean((yTrain-pred_train)**2)
MSE_test = np.mean((yTest-pred_test)**2)
#print('訓練資料的MSE:', MSE_train)
print('測試資料的MSE:', MSE_test)

#print('訓練資料的R-squared:', lm.score(XTrain,yTrain))
print('測試資料的R-squared:', lm.score(XTest,yTest))





