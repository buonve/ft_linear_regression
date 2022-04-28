import csv
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


if __name__ == '__main__':
    # read the data from the csv file
    data = pd.read_csv('data.csv')
    X = data.iloc[:, 0]
    Y = data.iloc[:, 1]

    
    #building the model
    m = 0
    c = 0
    learning_rate = 0.0001
    epochs = 1000
    n = float(len(X))
    print(X)
    for i in range(epochs):
        Y_pred = m * X + c
        D_m = -(2/n) * sum(X * (Y - Y_pred))
        D_c = -(2/n) * sum(Y - Y_pred)
        m = m - learning_rate * D_m
        c = c - learning_rate * D_c
    
    print('m: ', m, 'c: ', c)

    #make predictions
    Y_pred = m * X + c
    plt.scatter(X, Y)
    plt.plot(X, Y_pred, color='red')
    plt.show()








    