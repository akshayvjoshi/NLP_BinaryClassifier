from sklearn.svm import SVC
import numpy as np
import matplotlib as plt
import pylab as pl

from sklearn.svm import SVC
clf = SVC()

fh_train = open("/home/avj/Documents/NLP/NLP_BinaryClassifier/training1.csv", 'r')
fh_test = open("/home/avj/Documents/NLP/NLP_BinaryClassifier/test1.csv", 'r')
X_train = list()
Y_train = list()
X_test = list()
Y_test = list()
while True:
	line = fh_train.readline()
	vect = list()
	
	if not line:
		break
	vect = line.split(",")
	Y_train.append(vect[0:1])	
	vect = map(int, vect[1:])
	X_train.append(vect[0:])
	#print vect[1:]
#print X_train
#print Y_train
		
while True:
	line = fh_test.readline()
	vect = list()
	
	if not line:
		break
	vect = line.split(",")
	
	Y_test.append(vect[0:1])	
	vect = map(int, vect[1:])
	X_test.append(vect[0:])
#print fh_train.readline()

clf.fit(X_train, Y_train) 
print(clf.predict(X_test))

