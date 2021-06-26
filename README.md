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
