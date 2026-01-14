# Import required libraries
from sklearn.datasets import load_iris
from sklearn.cluster import KMeans

# Load Iris dataset
iris = load_iris()
X = iris.data   # features

# Apply K-Means clustering (3 clusters for 3 flower types)
kmeans = KMeans(n_clusters=3, random_state=42)

# Fit the model
kmeans.fit(X)

# Get cluster labels
labels = kmeans.labels_

# Print cluster labels
print("Cluster Labels:")
print(labels)