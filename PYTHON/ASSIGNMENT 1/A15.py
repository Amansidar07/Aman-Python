# Import required libraries
from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering

# Load Iris dataset
iris = load_iris()
X = iris.data   # features

# Apply Agglomerative Hierarchical Clustering
# Iris has 3 natural classes
model = AgglomerativeClustering(n_clusters=3)

# Fit the model and predict cluster labels
labels = model.fit_predict(X)

# Print cluster labels
print("Cluster Labels:")
print(labels)
