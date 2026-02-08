'''
numpy
创建一个形状为 (3,4) 的二维数组，元素为 0-11 的连续整数
查看数组的 shape 、 dtype 、 ndim 属性
将数组变形为 (4,3)，并展平为一维数组
文档查阅：搜索 NumPy 官方文档「np.reshape」，确认 reshape 中 -1 的用法（如
arr.reshape(4,-1) 是什么含义）
'''
import numpy as np

# 1. 创建（3， 4）数组
arr = np.arange(0, 12).reshape(3, 4)
print(arr)
print()

# 2. 查看数组的相关属性
print(f"arr shape: {arr.shape}")
print(f"arr dtype: {arr.dtype}")
print(f"arr ndim: {arr.ndim}")
print()

# 3. 转换数组的形状
reshaped_arr = arr.reshape(4, 3)
print(f"变形后的数组：\n {reshaped_arr}")
print()

# 4. 展开数组
unfolded_arr = reshaped_arr.reshape(-1)
print(f"展开后的数组：\n {unfolded_arr}")
print()
