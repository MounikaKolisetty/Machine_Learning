import os
import re
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import classification_report
from sklearn.metrics import accuracy_score
from sklearn.metrics import plot_confusion_matrix
import matplotlib.pyplot as plt

path = r'/Users/mouni.kolisetty/Documents/Sem 3/machine learning/Files for task 5'

object1_data = pd.DataFrame()
object2_data = pd.DataFrame()
object3_data = pd.DataFrame()  
training_set = pd.DataFrame()  
validation_set = pd.DataFrame()  
for subdir, dirs, files in os.walk(path):
    for dir in dirs:
        subdir_path = os.path.join(subdir, dir)
        for subdir1, dirs1, files1 in os.walk(subdir_path):
            if dir == "Object 1":
                for f in files1:
                        df = pd.read_excel(os.path.join(subdir1,f), header = None, usecols = "G:DZZ")
                        df.insert(0, "Object Type", "Object 1")
                        object1_data = object1_data.append(df,ignore_index=True)
                training_set1, validation_set1 = train_test_split(object1_data, test_size = 0.2, random_state = 21)
                
            elif dir == "Object 2":
                for f in files1:
                        df = pd.read_excel(os.path.join(subdir1,f), header = None, usecols = "G:DZZ")
                        df.insert(0, "Object Type", "Object 2")
                        object2_data = object2_data.append(df,ignore_index=True)
                training_set2, validation_set2 = train_test_split(object2_data, test_size = 0.2, random_state = 21)
               
            elif dir == "Object 3":
                for f in files1:
                        df = pd.read_excel(os.path.join(subdir1,f), header = None, usecols = "G:DZZ")
                        df.insert(0, "Object Type", "Object 3")
                        object3_data = object3_data.append(df,ignore_index=True)
                training_set3, validation_set3 = train_test_split(object3_data, test_size = 0.2, random_state = 21)

#Appending training data from all the object types        
training_set = training_set.append(training_set1,ignore_index = True)
training_set = training_set.append(training_set2,ignore_index = True)
training_set = training_set.append(training_set3,ignore_index = True)

#Appending validation data from all the object types  
validation_set = validation_set.append(validation_set1,ignore_index = True)
validation_set = validation_set.append(validation_set2,ignore_index = True)
validation_set = validation_set.append(validation_set3,ignore_index = True)


X_train = training_set.iloc[:, 1:-1].values
Y_train = training_set.iloc[:, 0].values
X_val = validation_set.iloc[:, 1:-1].values
y_val = validation_set.iloc[:, 0].values

#Initializing the MLPClassifier
classifier = MLPClassifier(hidden_layer_sizes=(100,50,50), max_iter=300,activation = 'relu',solver='adam',random_state=1)

#Fitting the training data to the network
classifier.fit(X_train, Y_train)

#Predicting y for X_val
y_pred = classifier.predict(X_val)

#Comparing the predictions against the actual observations in y_val
cm = confusion_matrix(y_pred, y_val)
print(cm, "\n")

#Ploting confusion matrix
disp = plot_confusion_matrix(classifier, X_val, y_val,
                                 cmap=plt.cm.Blues)
plt.show()

#Printing the accuracy
accuracy = accuracy_score(y_pred, y_val)
print("Accuracy of MLPClassifier : ", accuracy, "\n")

#Printing F1
print(classification_report(y_pred,y_val), "\n")

FP = cm.sum(axis=0) - np.diag(cm) 
FN = cm.sum(axis=1) - np.diag(cm)
TP = np.diag(cm)
TN = cm.sum() - (FP + FN + TP)
FP = FP.astype(float)
FN = FN.astype(float)
TP = TP.astype(float)
TN = TN.astype(float)

print("TruePostive(TP) : ", TP, "\n")
print("TrueNegative(TN) : ", TN, "\n")
print("FalsePostive(FP) : ", FP, "\n")
print("False Negative(FN) : ", FN, "\n")

# False discovery rate
FDR = FP/(TP+FP)
print("False Discovery Rate(FDR) : ", FDR, "\n")

# Negative predictive value
NPV = TN/(TN+FN)
print("Negative Preductive Value(NPV) : ", NPV, "\n")

# Sensitivity, hit rate, recall, or true positive rate
TPR = TP/(TP+FN)
print("True Positive Rate(TPR) : ", TPR, "\n")

# Specificity, selectivity or true negative rate
TNR = TN/(TN+FP) 
print("True Negative Rate(TNR) : ", TNR, "\n")