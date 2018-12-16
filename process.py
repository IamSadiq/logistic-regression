import numpy as np 
import pandas as pd

def getData():
    df = pd.read_csv('./data/ecommerce_data.csv')
    data = df.as_matrix()

    X = data[:, :-1]
    Y = data[:, -1]

    X[:, 1] = (X[:, 1] - X[:, 1].mean()) / X[:, 1].std()
    X[:, 2] = (X[:, 2] - X[:, 2].mean()) / X[:, 2].std()

    N, D = X.shape

    X2 = np.zeros((N, D+3))
    X2[:, 0:(D-1)] = X[:, 0:(D-1)]

    print(X)
    print(Y)
    print(X2)


# getData()