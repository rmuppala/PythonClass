# Import the libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA
import pandas as pd
from sklearn import datasets, metrics
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


dataset = pd.read_csv('admission2.csv')
x = dataset.iloc[:, 0:2].values
y = dataset.iloc[:, 2].values

for i in range(0,5):
    x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)

    #LDA
    lda = LDA(n_components = 2)
    lda.fit_transform(x_train, y_train)
    y_pred = lda.predict(x_test)
    print(i , "LDA accuracy                 = " ,lda.score(x_test,y_test))


    #LogisticRegression
    model=LogisticRegression()
    model.fit(x_train,y_train)
    y_pred = model.predict(x_test)
    print(i , "Logistic Regression accuracy = " ,model.score(x_test,y_test))
