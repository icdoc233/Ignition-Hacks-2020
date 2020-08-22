import pandas as pd
import numpy as np
import sklearn
from sklearn import linear_model
from sklearn.preprocessing import PolynomialFeatures
from sklearn import metrics
import pickle
from sys import exit

data = pd.read_csv("student-mat.csv", sep=";")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

stored = None
predict = "G3"


def changepredict():
    global predict, X, y, X_train, X_test, y_train, y_test, stored
    predict = input(
        "Enter the attribute you want to predict (\"G1\", \"G2\", \"G3\", \"studytime\", \"failures\", "
        "or \"absences\"). \nCurrently predicting " + predict + ", enter \"quit\" to exit.\n")
    if predict == "quit":
        exit()
    X = np.array(data.drop(predict, 1))
    y = np.array(data[predict])
    X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

    if predict != stored:
        print ("Training models...")
        retrain_models(-100)
        stored = predict


def retrain_models(minimum):
    for i in range(1, 6):
        train_polyreg(100, i, minimum)


def train_polyreg(k, degree, atleast):
    global X, y, PolyReg, polynom
    score = atleast

    for _ in range(k):
        X_train, X_test, y_train, y_test = sklearn.model_selection.train_test_split(X, y, test_size=0.1)

        LinReg = linear_model.LinearRegression()
        LinReg.fit(X_train, y_train)

        polynom = PolynomialFeatures(degree=degree)
        X_polynom = polynom.fit_transform(X_train)

        PolyReg = linear_model.LinearRegression()
        PolyReg.fit(X_polynom, y_train)

        predicted = PolyReg.predict(polynom.fit_transform(X_test))
        r_square = metrics.r2_score(y_test, predicted)
        if r_square > score:
            score = r_square
            with open("student_degree" + str(degree) + "_model.pickle", "wb") as f:
                pickle.dump(PolyReg, f)


lst = ["G1", "G2", "G3", "studytime", "failures", "absences"]
while True:
    changepredict()
    temp = lst.copy()
    temp.remove(predict)
    arr = (list(map(int, input("Please enter the " + ', '.join(temp) + " of the student, separated by space:\n").split())))
    for i in range(1, 6):
        pickle_in = open("student_degree" + str(i) + "_model.pickle", "rb")
        PolyReg = pickle.load(pickle_in)
        polynom = PolynomialFeatures(degree=i)
        predictions = PolyReg.predict(polynom.fit_transform(X_test))
        r_square = metrics.r2_score(y_test, predictions)
        print("Estimated result with degree " + str(i) + " regression:", PolyReg.predict(polynom.fit_transform([arr])))
        print("R-Square Error for reference:", r_square, "\n")
    print("***\n")