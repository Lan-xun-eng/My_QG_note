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


def silhouette_score(X, labels):
    n_samples = X.shape[0]
    unique_labels = np.unique(labels)
    n_clusters = len(unique_labels)

    if n_clusters == 1:
        return 0.0

    diff = X[:, np.newaxis, :] - X[np.newaxis, :, :]
    dist_matrix = np.sqrt(np.sum(diff ** 2, axis=2))  # (n_samples, n_samples)

    s = np.zeros(n_samples)
    for i in range(n_samples):
        same_cluster = (labels == labels[i])
        same_cluster[i] = False
        if np.sum(same_cluster) == 0:
            a_i = 0
        else:
            a_i = np.mean(dist_matrix[i, same_cluster])

        b_i = np.inf
        for label in unique_labels:
            if label == labels[i]:
                continue
            other_cluster = (labels == label)
            mean_dist = np.mean(dist_matrix[i, other_cluster])
            if mean_dist < b_i:
                b_i = mean_dist

        if a_i == 0 and b_i == np.inf:
            s[i] = 0
        else:
            s[i] = (b_i - a_i) / max(a_i, b_i)

    return np.mean(s)

def purity_score(y_true, y_pred):
    contingency = np.zeros((len(np.unique(y_true)), len(np.unique(y_pred))))
    for i in range(len(y_true)):
        contingency[y_true[i], y_pred[i]] += 1

    return np.sum(np.max(contingency, axis=0)) / len(y_true)


# 这次的代码借鉴了ai，因为感觉对机器学习部分的内容掌握还不熟练，后续熟练后可能会修改
# 获取数据
iris = load_iris()
X = iris.data
y_true = iris.target

# 设置随机种子保证可复现
kmeans = KMeans(n_clusters=3, max_iter=300, tol=1e-4, random_state=42)
kmeans.fit(X)

# 预测标签
y_pred = kmeans.labels_

# 计算轮廓系数
sil_score = silhouette_score(X, y_pred)
print(f"轮廓系数: {sil_score:.4f}")

# 计算纯度
purity = purity_score(y_true, y_pred)
print(f"纯度: {purity:.4f}")

# 输出 inertia
print(f"簇内平方和: {kmeans.inertia_:.2f}")
print(f"迭代次数: {kmeans.n_iter_}")
print("簇中心:\n", kmeans.cluster_centers_)