# Enter your code here. Read input from STDIN. Print output to STDOUT

import numpy as np
from sklearn import linear_model as lm
from sklearn import preprocessing as pp

F, N = map(int, input().split())
train = np.array([input().split() for _ in range(N)], float)
T = int(input())
test = np.array([input().split() for _ in range(T)], float)

model = lm.LinearRegression()
XtoP = pp.PolynomialFeatures(3)

model.fit(XtoP.fit_transform(X = train[:, :-1]), y = train[:, -1])

yHat = model.predict(XtoP.fit_transform(test))

print(*yHat, sep = '\n')
