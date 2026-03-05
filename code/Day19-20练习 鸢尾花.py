import numpy as np
from sklearn.datasets import load_iris

class KMeans:
    def __init__(self, n_clusters=3, max_iter=300, tol=1e-4, init='random', random_state=None):
        self.n_clusters = n_clusters
        self.max_iter = max_iter
        self.tol = tol
        self.init = init
        self.random_state = random_state
        self.cluster_centers_ = None   # 簇中心，形状 (n_clusters, n_features)
        self.inertia_ = None           # 样本到最近簇中心的距离平方和
        self.labels_ = None            # 训练后每个样本的标签
        self.n_iter_ = 0               # 实际迭代次数

    def _init_centroids(self, X):
        n_samples = X.shape[0]
        rng = np.random.default_rng(self.random_state)
        indices = rng.choice(n_samples, size=self.n_clusters, replace=False)
        self.cluster_centers_ = X[indices].copy()

    def _assign_clusters(self, X):
        distances = np.linalg.norm(X[:, np.newaxis, :] - self.cluster_centers_[np.newaxis, :, :], axis=2)
        labels = np.argmin(distances, axis=1)

        inertia = np.sum(np.min(distances, axis=1) ** 2)
        return labels, inertia

    def _update_centroids(self, X, labels):
        new_centers = []
        for i in range(self.n_clusters):
            mask = (labels == i)
            if np.sum(mask) == 0:
                new_centers.append(self.cluster_centers_[i])
            else:
                new_centers.append(np.mean(X[mask], axis=0))
        return np.array(new_centers)

    def fit(self, X):
        X = np.asarray(X)
        if self.random_state is not None:
            np.random.seed(self.random_state)

        self._init_centroids(X)
        prev_inertia = np.inf

        for i in range(self.max_iter):
            labels, inertia = self._assign_clusters(X)
            new_centers = self._update_centroids(X, labels)

            center_shift = np.linalg.norm(new_centers - self.cluster_centers_)
            self.cluster_centers_ = new_centers

            if center_shift < self.tol:
                self.n_iter_ = i + 1
                break

            prev_inertia = inertia
        else:
            self.n_iter_ = self.max_iter

        # 最终分配
        self.labels_, self.inertia_ = self._assign_clusters(X)
        return self

    def predict(self, X):
        X = np.asarray(X)
        distances = np.linalg.norm(X[:, np.newaxis, :] - self.cluster_centers_[np.newaxis, :, :], axis=2)
        return np.argmin(distances, axis=1)

    def fit_predict(self, X):
        self.fit(X)
        return self.labels_

iris = load_iris()
X = iris.data
y_true = iris.target