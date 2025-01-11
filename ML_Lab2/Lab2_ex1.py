import time
import numpy as np
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.datasets import fetch_california_housing
from sklearn.metrics import r2_score

def load_data():
    [X,y]=fetch_california_housing(return_X_y=True)
    return X,y

def main():
    [X,y]=load_data()
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30, random_state=999)

    ##scale the data
    scaler = StandardScaler()
    scaler= scaler.fit(X_train)
    X_train_scaled = scaler.transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    #train a model
    print("---Training under progress---")
    print ("N =%d" %(len(X)))
    model = LinearRegression()
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    r2= r2_score(y_test, y_pred)
    print ("R2 =", r2)

if __name__ == '__main__':
    main()
