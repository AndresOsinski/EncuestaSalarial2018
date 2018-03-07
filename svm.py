import math
import sys
import pandas as pd
import numpy as np
from sklearn import svm

data = pd.read_csv(sys.stdin)

columns = data.axes[1][:-1]
y = data.salary.values
X = data.drop(['salary'], axis=1).values
clf = svm.SVR(kernel='rbf', C=75000, gamma=3)
clf.fit(X, y)

errs = []
for x, d in enumerate(X):
    expected = clf.predict([d])[0]
    value = y[x]
    err2 = (expected - value) * (expected - value)
    errs.append((err2, x))

errs.sort(key=lambda x: x[0], reverse=True)
for (_, x) in errs[:10]:
    d = X[x]
    expected = clf.predict([d])[0]
    print('expected: {}, value: {}'.format(round(expected), round(y[x])))
    print(' '.join('{}: {}'.format(col, d[i]) for i, col in enumerate(columns)))

print(math.log(sum(e[0] for e in errs)))
