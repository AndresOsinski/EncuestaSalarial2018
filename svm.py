import csv
import math
import random
from sklearn import svm
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
x = [[int(y * 100) for y in x] for x in data[:num_sample]]
y = [int(x) for x in salary[:num_sample]]
clf = svm.SVC()
clf.fit(x, y)

errs = []
for x, d in enumerate(data):
    expected = clf.predict([d])[0]
    value = salary[x]
    err2 = (expected - value) * (expected - value)
    errs.append((err2, x))

errs.sort(key=lambda x: x[0], reverse=True)
for (_, x) in errs[:5]:
    d = data[x]
    expected = clf.predict([d])[0]
    print('expected: {}, value: {}'.format(round(expected), round(salary[x])))
    print(' '.join('{}: {}'.format(col, d[i]) for i, col in enumerate(columns)))

print(math.log(sum(e[0] for e in errs)))
