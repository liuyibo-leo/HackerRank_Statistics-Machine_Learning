#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
from sklearn import linear_model as lm
import pandas as pd


dataset = pd.read_csv('trainingdata.txt', header=None)

dataset = dataset.loc[dataset[0] <= 4]

X = np.array(dataset[0]).reshape(-1,1)
y = np.array(dataset[1]).reshape(-1,1)

model = lm.LinearRegression()
model.fit(X = X, y = y)


if __name__ == '__main__':
    timeCharged = float(input().strip())

predict = model.predict(np.array(timeCharged).reshape(-1,1))
predict = float(predict[0].round(2)) # for getting the standard output format

if predict > 8:
    print(8.0)
else:
    print(predict)

    
########################
#for my own practice
#!/bin/python3

import math
import os
import random
import re
import sys
import numpy as np
from sklearn import linear_model as lm
import pandas as pd



dataset = pd.read_csv('Laptop Battery Life  Training Data.txt', header=None)

dataset = dataset.loc[dataset[0] <= 4]

X = np.array(dataset[0]).reshape(-1,1)
y = np.array(dataset[1]).reshape(-1,1)

model = lm.LinearRegression()
model.fit(X = X, y = y)


if __name__ == '__main__':
    timeCharged = float(input().strip())

predict = model.predict(np.array(timeCharged).reshape(-1,1))
predict = float(predict[0].round(2)) # for getting the standard output format

if predict > 8:
    print(8.0)
else:
    print(predict)
