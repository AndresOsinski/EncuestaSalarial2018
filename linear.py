import csv
import math
import numpy as np
import random
import sys

columns = None
data = []
salary = []
reader = csv.reader(sys.stdin)
for row in reader:
    if columns is None:
        columns = row[:-1]
    else:
        data.append([float(x) for x in row[:-1]])
        salary.append(float(row[-1]))

num_sample = 1000
x = np.asarray([
    [x[i] for x in data[:num_sample]]
    for i in range(0, len(columns))
]).T
y = np.asarray(salary[:num_sample]).T
coefs = np.linalg.pinv((x.T).dot(x)).dot(x.T.dot(y))
print(', '.join('{}: {}'.format(col, round(coefs[i])) for i, col in enumerate(columns)))

errs = []
for x, d in enumerate(data):
    expected = sum(coefs[i] * d[i] for i in range(0, len(columns)))
    value = salary[x]
    err2 = (expected - value) * (expected - value)
    errs.append((err2, x))

errs.sort(key=lambda x: x[0], reverse=True)
for (_, x) in errs[:5]:
    d = data[x]
    expected = sum(coefs[i] * d[i] for i in range(0, len(columns)))
    print('expected: {}, value: {}'.format(round(expected), round(salary[x])))
    print(' '.join('{}: {}'.format(col, d[i]) for i, col in enumerate(columns)))

print(math.log(sum(e[0] for e in errs)))
