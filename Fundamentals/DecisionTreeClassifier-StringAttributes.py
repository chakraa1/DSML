"""
=======================
Problem Statement
=======================
Given the train and test data, predict the target labels for the observations in the test data using the
Decision Tree Classifier.
Decision Tree can't accept the string values for an attribute therefore complete the function str_column_to_int(dataset, var) to replace the string values of the 'var' column of the dataset with integers. The criteria for replacing the values is 'a' -> 0, 'b' -> 1, 'c' -> 2.

attr1 of the datasets contains binary values(0 or 1)
attr2 of the datasets is supposed to be consisting of string values.
The target variable also contains binary values(0 or 1)

=======================
Input Format:
=======================
5 lists are taken as input representing the attributes of train and test data and also target of train data.
First three lists are the attributes and target of the train data.
The next two lists are the attributes of the test data
=======================
Output Format:
=======================
Predictions for the observations in the test data in a NumPy array.
=======================
Sample Input:
=======================
attr1 for train data = [0, 0, 1, 1, 1, 1, 0, 0, 1, 1]
attr2 for train data = ['c', 'b', 'c', 'c', 'b', 'c', 'a', 'a', 'a', 'b']
tar for train data = [0, 0, 1, 1, 1, 1, 0, 1, 1, 0]
attr1 for test data = [1, 1, 0, 1, 1]
attr2 for test data = ['a', 'c', 'b', 'a', 'b']

=======================
Sample Output:
=======================
[1 1 0 1 0]
"""
# import Decision tree classifier
from sklearn.tree import DecisionTreeClassifier
import pandas as pd

a = eval(input())
b = eval(input())
c = eval(input())
d = eval(input())
e = eval(input())

train = pd.DataFrame({'attr1': a, 'attr2': b, 'tar': c})
test = pd.DataFrame({'attr1': d, 'attr2': e})


# returns a dataframe where the values in 'attr2' are replaced with 'l':0, 'm':1, 'h':2
def str_column_to_int(dataset, column):
    # all the unique values in the the attr2
    unique = sorted(pd.unique(dataset['attr2']))

    lookup = dict()
    for i, value in enumerate(unique):
        lookup[value] = i

    # replace the values in attr2


    dataset = dataset.replace({"attr2": {'a': 0, 'b': 1, 'c': 2}})
    return dataset

train = str_column_to_int(train, 'attr2')
test = str_column_to_int(test, 'attr2')

# initialize the classifier
tree = DecisionTreeClassifier()

# fit the model with the attributes and target of the training data
tree.fit(train[['attr1', 'attr2']], train[['tar']])

# predict the target for the observations in the test
pred = tree.predict(test[['attr1', 'attr2']])

print(pred)