import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

# 假设有三个特征
x = np.array([1.5, -2.0, 3.0])   # 输入向量 (3,)
w = np.array([0.5, -1.2, 0.8])   # 权重向量 (3,)
b = 0.5                           # 偏置标量

# 直接计算（标量循环）
z_direct = 0
for i in range(len(x)):
    z_direct += w[i] * x[i]
z_direct += b
a_direct = sigmoid(z_direct)
print(f"直接计算: z = {z_direct:.4f}, a = {a_direct:.4f}")

# 矩阵方式（向量化）
z_matrix = np.dot(w, x) + b
a_matrix = sigmoid(z_matrix)
print(f"矩阵方式: z = {z_matrix:.4f}, a = {a_matrix:.4f}")
