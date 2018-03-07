from sklearn.linear_model import LogisticRegression
from sklearn import datasets
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from sklearn import svm, datasets

irisdatasets=datasets.load_iris()
x=irisdatasets.data
y=irisdatasets.target



#split the data for training and testing
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2)


svcl = svm.SVC(kernel='linear')
svcl.fit(x_train, y_train)
print("SVC Accuracy Linear Kernal  = ", svcl.score(x_test,y_test))

svcr = svm.SVC(kernel='rbf')
svcr.fit(x_train, y_train)

print("SVC Accuracy RBF Kernal    = ",svcr.score(x_test,y_test))