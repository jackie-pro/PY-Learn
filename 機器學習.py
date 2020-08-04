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

XTrain, XTest, yTrain, yTest = train_test_split(X,y,test_size = 0.2, random_state=100)

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



#ex4:
from sklearn import datasets
import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split


bc= datasets.load_breast_cancer()

# 1. 全資料集建立邏輯迴歸模型====================================================

x=pd.DataFrame(bc.data, columns=bc.feature_names)
target=pd.DataFrame(bc.target, columns=["cured"])
y=target["cured"]

logistic=linear_model.LogisticRegression(max_iter=3000)
logistic.fit(x,y)

pred= logistic.predict(x)

print(pd.crosstab(target["cured"], pred))
print("全資料集正確率:",logistic.score(x,y))
allscore=logistic.score(x,y)
# 2. 選擇5個指標製作模型=======================================================

print("coef of all dataset:", logistic.coef_)
coef=pd.DataFrame(logistic.coef_, columns=bc.feature_names).T
coef_abs=abs(coef)

# 選擇以下五個指標
print(coef_abs.sort_values(0, ascending=False).index[0:5])
print()

# 篩選資料

index5=coef_abs.sort_values(0, ascending=False).index[0:5]
x1=x[index5]
target=pd.DataFrame(bc.target, columns=["cured"])
y=target["cured"]

# 製作模型
logistic=linear_model.LogisticRegression()
logistic.fit(x1,y)

pred= logistic.predict(x1)

print(pd.crosstab(target["cured"], pred))
print("5個指標資料集正確率:",logistic.score(x1,y))
index5score=logistic.score(x1,y)
# 3.  製作訓練測試資料集=======================================================

x=pd.DataFrame(bc.data, columns=bc.feature_names)
target=pd.DataFrame(bc.target, columns=["cured"])
y=target["cured"]

xtrain, xtest, ytrain, ytest=train_test_split(x,y, test_size=0.3,
                                              random_state=10)

logistic=linear_model.LogisticRegression(max_iter=3000)
logistic.fit(xtrain,ytrain)
pred_test= logistic.predict(x)

print(pd.crosstab(target["cured"], pred_test))
print("測式資料集正確率:",logistic.score(x,y))
testscore=logistic.score(x,y)
# 4.  決定測試何者較佳========================================================

x=pd.DataFrame(bc.data, columns=bc.feature_names)
target=pd.DataFrame(bc.target, columns=["cured"])
y=target["cured"]

def testsize(ts):
    
    xtrain, xtest, ytrain, ytest=train_test_split(x,y, test_size=ts,
                                                  random_state=10)
    
    logistic=linear_model.LogisticRegression(max_iter=5000, dual=False)
    logistic.fit(xtrain,ytrain)
    pred_test= logistic.predict(x)
    pd.crosstab(target["cured"], pred_test)
    
    testscore=logistic.score(x,y)
    return testscore

maxscore=0
bestsize=0
for i in range(99, 1,-1):
    testscore=testsize(i/100)
    if testscore>maxscore:
        maxscore=testscore
        bestsize=i/100
print("準確率最高為 %f, 測試集比率為 %f" % (maxscore, bestsize))

