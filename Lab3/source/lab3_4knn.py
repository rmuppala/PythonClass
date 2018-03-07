from sklearn.neighbors import KNeighborsClassifier
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
import pandas as pd

dataset = pd.read_csv('admission.csv')
x = dataset.iloc[:, 0:2].values
y = dataset.iloc[:, 2].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


k_range=[1,10,20,30,40,50]
scores=[]

for k in k_range:
    knn=KNeighborsClassifier(n_neighbors=k)
    knn.fit(x_train,y_train)
    y_pred=knn.predict(x_test)
    scores.append(metrics.accuracy_score(y_test,y_pred))

import matplotlib.pyplot as plt
for i in range(0,len(k_range)):
    print('n_neighbors = ' , k_range[i] , ' accuracy = ' , scores[i])

plt.plot(k_range,scores)
plt.xlabel("value of k")
plt.ylabel("testing accuracy")
plt.show()