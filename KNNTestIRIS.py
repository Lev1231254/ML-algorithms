import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import sklearn
import KNNFromScratch


def scatter2features(i, j, feature_names):
    plt.scatter(setosas[:, i], setosas[:, j],
                color='skyblue',
                label='Setosas')
    plt.scatter(versicolors[:, i], versicolors[:, j],
                color='lightcoral',
                label='Versicolors')
    plt.scatter(virginicas[:, i], virginicas[:, j],
                color='lawngreen',
                label='Virginicas')
    plt.xlabel(feature_names[i])
    plt.ylabel(feature_names[j])
    plt.legend()


def plot_neighbours(point, k_neighbours, axes):
    # --- axes are sepal length and width ---
    xAxis, yAxis = axes
    # divide into groups
    k_neighbour_cords_setosa = np.array([neighbour[0] for neighbour in k_neighbours if neighbour[2] == 0])
    k_neighbour_cords_versicolor = np.array([neighbour[0] for neighbour in k_neighbours if neighbour[2] == 1])
    k_neighbour_cords_virginica = np.array([neighbour[0] for neighbour in k_neighbours if neighbour[2] == 2])
    
    predicted_group = KNNFromScratch.intToGroup(KNNFromScratch.knn_predict(k, point, features, labels))
    
    scatter2features(xAxis, yAxis, feature_names)
    if k_neighbour_cords_setosa.size != 0:
        plt.scatter(k_neighbour_cords_setosa[:, xAxis], k_neighbour_cords_setosa[:, yAxis],
                    label = 'Setosa neighbours',
                    color = 'darkblue')
    if k_neighbour_cords_versicolor.size != 0:
        plt.scatter(k_neighbour_cords_versicolor[:, xAxis], k_neighbour_cords_versicolor[:, yAxis],
                    label = 'Versicolor neighbours',
                    color = 'darkred')
    if k_neighbour_cords_virginica.size != 0:
        plt.scatter(k_neighbour_cords_virginica[:, xAxis], k_neighbour_cords_virginica[:, yAxis],
                    label = 'Virginica neighbours',
                    color = 'darkgreen')
    
    plt.scatter(point[xAxis], point[yAxis],
                label = 'Prediction: ' + predicted_group,
                color = 'magenta',
                )
    plt.legend()
    plt.title("KNN using Iris-Dataset")
    plt.show()


dataset = sklearn.datasets.load_iris()

feature_names = dataset.feature_names
label_names = dataset.target_names

features = dataset.data
labels = dataset.target


setosas = np.array([features[i] for i in range(features.shape[0]) if labels[i] == 0])
versicolors = np.array([features[i] for i in range(features.shape[0]) if labels[i] == 1])
virginicas = np.array([features[i] for i in range(features.shape[0]) if labels[i] == 2])

#---- 5 nearest neighbours from point (5.5, 3.5, 2.5, 1) -----
k = 10
point = np.array([5.5, 3.5, 2.5, 1])

k_neighbours = KNNFromScratch.find_k_nearest_neighbours(k, point, features, labels)



plot_neighbours(point, k_neighbours, (0, 1))
plt.figure()