# Machine_Learning
Discrimination of Reflected Sound Signals using MLP Classifier

The surface of an object reflects a sound signal. Recording the reflected signal provides a time signal. This time signal results from the convolution of the incident acoustic wave with the surface properties of the reflecting object. Knowing the incident acoustic signal one can conclude on the reflecting object by analyzing the reflected signal.
We use reflected time signals to conclude on the reflecting object. As the number of objects is limited in our experimental setup, solving the task means discriminating the time signals.
# Model:
![mlp](https://user-images.githubusercontent.com/84661500/120302693-6f392680-c2ce-11eb-9f8e-0a78de7c21d3.png)

The actual concept of neural network model which is specifically known as Multi-layer Perceptron classifier, is to obtain linear combinations of the given inputs as derived features and then model the target as a nonlinear function of these features. We used the MLPClassifier function in the sklearn Python library for MLP. We selected stochastic gradient-based optimizer proposed by Kingma, Diederik, and Jimmy Ba as the solver forweight optimization (ie, solver = “adam”) because of large dataset. We considered hyperparameters, including different hidden layer sizes and activation functions.

# Tasks:
1) Creating a GUI,
2) Reading time signals from given Excel files, one time signal per row, starting column and signal length (number of scan points) adjustable,
3) To distinguish between three classes, namely “Object #1”, “Object #2” and “Object #3”,
4) Using data labels given in the Excel file or to create new labels and complete the data files,
5) Creating a classifier (discriminator) by machine learning using a MLP (multilayer perceptron) and labeled data,
6) Using the trained MLP classifier for discriminating new data,
7) Assess the classifier (at least all of the following measures: TP, TN, FP, FN, FDR, NPV, TPR, TNR, F1, ROC),

The GUI looks as follows with three tabs:
1. Train, 2. Output Measures and 3. Test

Train tab fetches all the the time signals from each row within specified columns, trains the MLP Classifier model and produces the Accuracy.
Model was build using sklearn.

<img width="1263" alt="Screenshot 2021-06-26 at 12 22 36" src="https://user-images.githubusercontent.com/56874374/123510201-7c9dc280-d67a-11eb-9558-551ee2463ba6.png">

Output Measures tab displayes all the outputs acquired while validating 20% of whole data.                                                                 
Measures inculde: TruePositive(TP), TrueNegative(TN), FalsePositive(FP), FalseNegative(FN), False Discovery Rate(FDR), Negative Preductive Value(NPV), True Positive Rate(TPR), True Negative Rate(TNR), F1 Score, ROC Score, Confusion Matrix and ROC Graph.

<img width="1270" alt="Screenshot 2021-06-26 at 12 22 49" src="https://user-images.githubusercontent.com/56874374/123510206-81fb0d00-d67a-11eb-9bff-eb7ddeb28281.png">

Test tab browses the test file and also the folder to store the test result in Output.xlsx file.                                                             
In addition we can get the output of particular time signal using precise output.

<img width="1269" alt="Screenshot 2021-06-26 at 12 23 07" src="https://user-images.githubusercontent.com/56874374/123510208-858e9400-d67a-11eb-98af-4d63dcd8e3c4.png">

# Installation Guide:
Below are the following steps to test the project.
1.	Install Python from the below link. This project is implemented in Python 3.9.
https://www.python.org/downloads/
2.	Download and Install any IDE (integrated development environment) such as ‘PyCharm’ or ‘Visual Studio’ Code.
3.	Now open the python file(.py) in the IDE.
4.	Open the Terminal and import the packages using the following commands. Do it one after another.

    i.	pip install pandas
    
    ii.	pip install numpy
    
    iii.pip install sklearn
    
    iv.	pip install seaborn
    
    v.	pip install matplotlib
    
5.  After installing the required packages, run the program. Now a gui window will be opened and follow the instructions.
