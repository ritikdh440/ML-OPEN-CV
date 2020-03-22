# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 17:21:06 2020

@author: Ritik dhiman
"""
import sklearn 
import tree
#STEP 1 COLLECTING THE TRAINING DATA
feautres = [[140,1],[130,1],[150,0],[170,0]]
labels = [0,0,1,1]

"""features contains the data of [Weight , texture ] of the fruit
I used 1 for Smooth and 0 for Bumpy
abels variable contain the data of label given to fruit
I used 1 for Orange , 0 for Apple"""

#STEP 2 TRAIN THE CLASSIFIER , the type of classifier i used now is DECISION TREE
clf = tree.DecisionTreeClassifier()

"""To Train the classifier we need a learning alogrithim as the procedure that create.
It does that finding patterns in training data
for eg. it might noticed orange tend to weigh more, so it create a rule that heavier fruit is more likely to be Orange

In scikit , the training alogrithim is included in the classifier object and called as "fit" being used a syn. for "FIND PATTERNS" in the data"""

clf = clf.fit(features,labels)

#STEP 3 MAKE Prediction
print (clf.predict([[150,0]]))



