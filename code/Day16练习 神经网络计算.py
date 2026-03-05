import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def ReLU(z):
    return np.maximum(0, z)

# 单个样本
# 输入层 一个神经元
x = np.array([1.0, -0.5])

# 隐藏层 一层 三个神经元
w1 = np.array([[0.2, -0.3],
              [0.5, 0.1],
              [-0.4, 0.6]]
              )
b1 = np.array([0.1, -0.2, 0.3])

# 输出层 一个神经元
w2 = np.array([[0.7, -0.5, 0.2]])
b2 = np.array([0.4])


'''
一定要具备分装的思想，一开始我还只是想着分别计算隐藏层和输出层的结果，但是前向传播作为一个独立整体的过程，
还是要分装成专门的函数更为妥当，所以以后要注意对于一个独立的过程最好分装成函数，反向传播也一样
'''
# 前向传播
def forward_propagation(x, w1, b1, w2, b2):
    # 隐藏层
    z1 = np.dot(w1, x) + b1
    a1 = ReLU(z1)
    # 输出层
    z2 = np.dot(w2, a1) + b2
    a2 = sigmoid(z2)
    return a2, a1

# 输出结果
pred_a, hidden_a = forward_propagation(x, w1, b1, w2, b2)
print(f"预测概率:{pred_a[0]}")

# 多个样本
X = np.array([[1.0, 0.5, -0.2],
               [-0.5, 0.8, 0.3]]
              )
def forward_propagation_plus(X, w1, b1, w2, b2):
    # 隐藏层
    z1 = np.dot(w1, X) + b1.reshape(-1, 1)
    A1 = ReLU(z1)
    # 输出层
    z2 = np.dot(w2, A1) + b2.reshape(-1, 1)
    A2 = sigmoid(z2)
    return A2, A1

pred_A, hidden_A = forward_propagation_plus(X, w1, b1, w2, b2)
print(f"预测概率:{pred_A[0]}")


