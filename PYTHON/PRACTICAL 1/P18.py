# Import required libraries
from sklearn.datasets import load_digits
from sklearn.decomposition import PCA

# Load Digits dataset
digits = load_digits()
X = digits.data   # features

# Apply PCA to reduce dimensions to 2
pca = PCA(n_components=2)
X_reduced = pca.fit_transform(X)

# Print explained variance ratio
print("Explained Variance Ratio:", pca.explained_variance_ratio_)