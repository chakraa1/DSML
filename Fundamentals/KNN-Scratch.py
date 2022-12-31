def distance(x1,x2):
    return np.sqrt(np.sum(x1-x2)**2)
def KNN_Scratch(X,Y, x_query,K):
    distances =[]
    n = X.shape[0]

    for i in range(n):
        distance = distance(x_query,X[i])
        distances.append((distance,Y[i]))

    distances = sorted(distances)
    distances = distances[:K]
    distances = np.array(distances)

    # class count
    class_counts = np.unique(distances[:, 1], return_count=True)
    index = class_counts[1].argmax()
    pred = class_counts[0][index]

    return pred


