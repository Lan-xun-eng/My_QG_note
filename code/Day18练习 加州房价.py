import numpy as np
from sklearn.datasets import fetch_california_housing
import time
import matplotlib.pyplot as plt

'''
由于波士顿你房价数据集存在伦理问题，现已经被sklearn官方删除，同时加州房价数据集效果上与前者无明显差异，
故改用加州数据集
'''

# 数据加载与预处理
def load_and_preprocess():
    data = fetch_california_housing()
    X = data.data
    y = data.target

    # 划分训练集和测试集（80%训练，20%测试）
    np.random.seed(42)
    indices = np.random.permutation(len(X))
    split = int(0.8 * len(X))
    train_idx, test_idx = indices[:split], indices[split:]
    X_train, X_test = X[train_idx], X[test_idx]
    y_train, y_test = y[train_idx], y[test_idx]

    # 特征标准化
    mean = X_train.mean(axis=0)
    std = X_train.std(axis=0)
    std[std == 0] = 1.0
    X_train_std = (X_train - mean) / std
    X_test_std = (X_test - mean) / std

    # 添加偏置列（全1）
    X_train_b = np.c_[X_train_std, np.ones(X_train_std.shape[0])]
    X_test_b = np.c_[X_test_std, np.ones(X_test_std.shape[0])]

    return X_train_b, X_test_b, y_train, y_test, mean, std

# 多元线性回归类
class LinearRegression:
    def __init__(self, method='closed_form', learning_rate=0.01, epochs=1000, fit_intercept=True):
        self.method = method
        self.lr = learning_rate
        self.epochs = epochs
        self.fit_intercept = fit_intercept
        self.theta = None
        self.loss_history = []

    def fit(self, X, y):
        X = np.asarray(X)
        y = np.asarray(y).reshape(-1, 1)

        if self.fit_intercept and X.shape[1] == X.shape[1] and not np.allclose(X[:, -1], 1):
            X = np.c_[X, np.ones(X.shape[0])]

        if self.method == 'closed_form':
            self._closed_form(X, y)
        elif self.method == 'gradient_descent':
            self._gradient_descent(X, y)
        else:
            raise ValueError("method must be 'closed_form' or 'gradient_descent'")

    def _closed_form(self, X, y):
        XTX = X.T @ X
        if np.linalg.det(XTX) == 0:
            self.theta = np.linalg.pinv(XTX) @ X.T @ y
        else:
            self.theta = np.linalg.inv(XTX) @ X.T @ y

    def _gradient_descent(self, X, y):
        N = X.shape[0]
        self.theta = np.random.randn(X.shape[1], 1) * 0.01
        self.loss_history = []

        for epoch in range(self.epochs):
            y_pred = X @ self.theta
            loss = np.mean((y_pred - y) ** 2) / 2
            self.loss_history.append(loss)

            grad = (X.T @ (y_pred - y)) / N
            self.theta -= self.lr * grad

            if epoch % 100 == 0:
                print(f"Epoch {epoch}, loss = {loss:.4f}")

    def predict(self, X):
        X = np.asarray(X)
        if self.fit_intercept and X.shape[1] == X.shape[1] and not np.allclose(X[:, -1], 1):
            X = np.c_[X, np.ones(X.shape[0])]
        return (X @ self.theta).flatten()

    def score(self, X, y):
        y_pred = self.predict(X)
        y = np.asarray(y).flatten()
        ss_res = np.sum((y - y_pred) ** 2)
        ss_tot = np.sum((y - np.mean(y)) ** 2)
        return 1 - ss_res / ss_tot

# 训练与评估
if __name__ == "__main__":
    # 加载数据
    X_train, X_test, y_train, y_test, mean, std = load_and_preprocess()

    # 1.解析解
    print("=" * 50)
    print("解析解 (正规方程)")
    start = time.time()
    lr_closed = LinearRegression(method='closed_form')
    lr_closed.fit(X_train, y_train)
    time_closed = time.time() - start
    train_score_closed = lr_closed.score(X_train, y_train)
    test_score_closed = lr_closed.score(X_test, y_test)
    print(f"训练时间: {time_closed:.4f} 秒")
    print(f"训练集 R^2: {train_score_closed:.4f}")
    print(f"测试集 R^2: {test_score_closed:.4f}")

    # 2.梯度下降
    print("\n" + "=" * 50)
    print("梯度下降 (学习率=0.1, epoch=2000)")
    lr_gd = LinearRegression(method='gradient_descent', learning_rate=0.1, epochs=2000)
    start = time.time()
    lr_gd.fit(X_train, y_train)
    time_gd = time.time() - start
    train_score_gd = lr_gd.score(X_train, y_train)
    test_score_gd = lr_gd.score(X_test, y_test)
    print(f"训练时间: {time_gd:.4f} 秒")
    print(f"训练集 R^2: {train_score_gd:.4f}")
    print(f"测试集 R^2: {test_score_gd:.4f}")

    # 3.绘制损失下降曲线
    plt.figure(figsize=(8, 5))
    plt.plot(lr_gd.loss_history)
    plt.xlabel('Epoch')
    plt.ylabel('Loss (MSE/2)')
    plt.title('Gradient Descent Loss Curve')
    plt.grid(True)
    plt.show()

    # 4.比较系数
    print("\n" + "=" * 50)
    print("解析解系数（前5个）:", lr_closed.theta.flatten()[:5])
    print("梯度下降系数（前5个）:", lr_gd.theta.flatten()[:5])