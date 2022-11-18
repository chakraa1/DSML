"""
====================
Problem Statement
====================

Given the train, test data, max_depth, n_trees, and ratio, implement bagging. Print the predictions for the observations
in the test data.
subsample(dataset, ratio) is already implemented but hidden, it returns a 2d-list consisting of sampled observations from the dataset.

====================
Input Format:
====================
There will be two lists and three numerical values.

====================
Output Format:
====================
a list is printed

====================
Sample Input:
====================
train = [[-0.049754741299329164, 1.7545324153602802, -2.015451904277496, -0.6655946053274271, 1.7654623717757776, 0.0], [-0.870176558754425, -0.8632506160200222, 1.0363347961933609, -0.9921482916137182, -1.1832955643653762, 1.0], [-0.5129465077761397, -1.2734979390270784, 1.0392261463425687, 0.5032338839619092, -0.27021541668479643, 1.0], [-1.1259555456220574, -1.3824926465371696, -2.4659947360738013, -1.0063448217690898, 0.5301098720856643, 0.0], [1.3355396455376942, 0.4767704351913865, -0.30995179013581164, 0.47754374871627314, 1.0282482787129177, 0.0], [-0.7941311111136664, -0.888479087765921, -0.9250860232848708, 1.7103333917320582, -0.006363196215441307, 0.0], [0.9640563948034004, 1.4206857618787228, -1.6719701692403608, -0.3025879352391404, -0.3062031013690185, 0.0], [2.1330018022897006, -0.2530885153742814, 0.14824433392167236, -1.5377998003498103, 1.491748723938095, 0.0], [0.8568323473193591, 1.454906042604595, 1.0226070656111748, 1.4208697842258664, -0.27155848114641123, 1.0], [-1.1103222963405424, -0.13362863845048603, 0.5522979973275985, 0.42165872702810914, 0.4884106152343072, 0.0]]
test = [[0.17633958605089237, 0.35362499501406774, 1.0412089882932318, -0.7965536407430361, 0.9519863722017938], [0.620158792718217, 1.7453802356037476, 0.2816748822184669, -0.9782700792376439, -0.7872827938664166], [-1.306157556172553, -0.36060622411280663, 0.9397657677158866, -0.1262661498810779, -0.458138342833524], [-1.3391549838490366, 0.9327917466845197, 1.1026267285716564, 0.23785062696034148, -0.4146697234931255], [0.08239261344402903, 0.6390284651763855, 0.9943395785869232, -1.5238363086071611, -0.5068234330383359], [1.2456200894224607, -1.2782333788330993, -0.9217918528513316, 1.6251354644171232, -0.6064346799018023], [-0.2632339135609847, -1.086878071181507, -1.7763680131285988, 0.4366870243082978, 1.7860028809138975], [-0.9190320708567004, 0.6107324610184034, 0.9930674674619598, 1.353023555031771, -1.800699232148709], [0.9540368382685985, -1.227571715875412, -0.18990171035397174, -0.5446964612387463, 0.3511497213610034], [1.8860175589060588, -0.036958602806592036, -1.2247513223969646, 0.7340332381471137, 1.1319547973555735]]
max_depth = 1
n_trees = 3
ratio = 0.1

====================
Sample Output: ==>
====================
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
"""
import numpy as np
from sklearn.tree import DecisionTreeClassifier

np.random.seed(0)

train = np.asarray(eval(input()))
test = np.asarray(eval(input()))
max_depth = int(input())  # maximum depth of trees
n_trees = int(input())  # number of trees
ratio = float(input())  # ratio of length of dataset to be generated while sampling


# Construct a tree model with max_depth = "max_depth", train it on the sample and return the model
def build_tree(sample, max_depth):
    tree = DecisionTreeClassifier(max_depth=max_depth)
    tree.fit(np.asarray(sample)[:, :-1], np.asarray(sample, dtype='int')[:, -1])
    return tree


def bagging_predict(trees, row):
    # predictions is the list of labels predicted by all the trees
    predictions = [tree.predict(row.reshape(1, -1))[0] for tree in trees]

    # return the prediction according to procedure used in bagging in classification
    return max(set(predictions), key=predictions.count)


# bagging
def bagging(train, test, max_depth, n_trees, ratio):
    trees = list()
    for i in range(n_trees):
        sample = subsample(train, ratio)  # A sample created from dataset of size round(len(dataset) * ratio)
        tree = build_tree(sample, max_depth)
        trees.append(tree)

    # store the predictions for each observation in the test data
    predictions = [bagging_predict(trees, row) for row in test]
    return (predictions)

