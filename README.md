# Machine_Learning
Discrimination of Reflected Sound Signals
The surface of an object reflects a sound signal. Recording the reflected signal provides a time signal. This time signal results from the convolution of the incident acoustic wave with the surface properties of the reflecting object. Knowing the incident acoustic signal one can conclude on the reflecting object by analyzing the reflected signal.
We use reflected time signals to conclude on the reflecting object. As the number of objects is limited in our experimental setup, solving the task means discriminating the time signals.
# Tasks:
1) Creating a GUI,
2) Reading time signals from given Excel files, one time signal per row, starting column and signal length (number of scan points) adjustable,
3) To distinguish between three classes, namely “Object #1”, “Object #2” and “Object #3”,
4) Using data labels given in the Excel file or to create new labels and complete the data files,
5) Creating a classifier (discriminator) by machine learning using a MLP (multilayer perceptron) and labeled data,
6) Using the trained MLP classifier for discriminating new data,
7) Assess the classifier (at least all of the following measures: TP, TN, FP, FN, FDR, NPV, TPR, TNR, F1, ROC),
