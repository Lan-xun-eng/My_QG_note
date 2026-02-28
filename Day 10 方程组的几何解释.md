由于线代中有相当大的一部分笔记需要各种公式，而截图公式的话比较费时费力，所以小编特意在github上找到了相关笔记，可以直接引用，所以我将直接采取github笔记并加入自己的理解，这样方便理解的同时，也有我自己的感悟

# 一、方程组的几何解释基础

### 1. 行图像

- 所谓 **行图像**，就是：
  在系数矩阵上，**一次取一行** 构成方程。和我们在初等数学中学习的作图求解方程的过程无异

我们首先通过一个例子了解二维方程组（2个未知数，2个方程），如下：

[![2个未知数2个方程](https://github.com/Gre111/math/raw/master/images/01/LA_1_1.png)

我们首先按 **row (行)** 将方程组写成矩阵形式：

[![按行写成矩阵形式](https://github.com/Gre111/math/raw/master/images/01/LA_1_2.png)](https://github.com/Gre111/math/blob/master/images/01/LA_1_2.png)

```
系数矩阵(A): 将方程组系数按行提取出来，构造完成的一个矩阵
未知向量(x): 将方程组的未知数提取出来，按列构成一个向量
向量(b): 将等号右侧结果按列提取，构成一个向量
```

构造完成相应的矩阵形式了，我们将对应的 **行图像** 画出来

[![行图像求解方程组](https://github.com/Gre111/math/raw/master/images/01/LA_1_3.jpg)](https://github.com/Gre111/math/blob/master/images/01/LA_1_3.jpg)

### 2. 列图像

从列图像的角度，我们再次求解上面的方程：

[![2个未知数2个方程](https://github.com/Gre111/math/raw/master/images/01/LA_1_1.png)](https://github.com/Gre111/math/blob/master/images/01/LA_1_1.png)

在这一次的求解过程中，我们将方程按列提取，使用的矩阵为：

[![按列提取矩阵](https://github.com/Gre111/math/raw/master/images/01/LA_1_4.png)](https://github.com/Gre111/math/blob/master/images/01/LA_1_4.png)
如上所示，我们使用 列向量 构成系数矩阵，将问题转化为: 将向量 [![向量1](https://github.com/Gre111/math/raw/master/images/01/LA_1_5.png)](https://github.com/Gre111/math/blob/master/images/01/LA_1_5.png) 与向量 [![向量2](https://github.com/Gre111/math/raw/master/images/01/LA_1_6.png)](https://github.com/Gre111/math/blob/master/images/01/LA_1_6.png) 正确组合，使得其结果构成 [![向量3](https://github.com/Gre111/math/raw/master/images/01/LA_1_7.png)](https://github.com/Gre111/math/blob/master/images/01/LA_1_7.png) 。

接下来我们使用 **列图像** 将方程组展现出来，并求解：

[![列图像](https://github.com/Gre111/math/raw/master/images/01/LA_1_5.jpg)](https://github.com/Gre111/math/blob/master/images/01/LA_1_5.jpg)

即寻找合适的 **x，y** 使得 **x** 倍的 **(2,-1)** + **y** 倍的 **(-1,2)**得到最终的向量 **(0,3)**。很明显能看出来，**1** 倍 **(2,-1)** + **2** 倍 **(-1,2)** 即满足条件。

反映在图像上，明显结果正确。

我们再想一下，仅仅对 [![按列提取矩阵](https://github.com/Gre111/math/raw/master/images/01/LA_1_4.png)](https://github.com/Gre111/math/blob/master/images/01/LA_1_4.png) 这个方程，如果我们任意取 x 和 y ，那么我们得到的是什么呢？很明显，能得到任意方向的向量，这些向量能够布满整个平面。这里我们先不做展开，稍微有一些印象就好。

# 二、方程组的几何解释推广

### 1. 高维行图像

我们将方程组的维数进行推广，从三维开始，[![三维方程](https://github.com/Gre111/math/raw/master/images/01/LA_1_8.png)](https://github.com/Gre111/math/blob/master/images/01/LA_1_8.png) ，如果我们继续使用上面介绍的 做出行图像 来求解问题，那么会得到一个很复杂的图像。

矩阵如下：

[![矩阵](https://github.com/Gre111/math/raw/master/images/01/LA_1_9.png)](https://github.com/Gre111/math/blob/master/images/01/LA_1_9.png)

对应方程： Ax = b

[![三维矩阵](https://github.com/Gre111/math/raw/master/images/01/LA_1_10.png)](https://github.com/Gre111/math/blob/master/images/01/LA_1_10.png)

如果绘制行图像，很明显这是一个三个平面相交得到一点，我们想直接看出这个点的性质可谓是难上加难

比较靠谱的思路是先联立其中两个平面，使其相交于一条直线，再研究这条直线与平面相交于哪个点，最后得到点坐标即为方程的解

这个求解过程对于三维来说或许还算合理，那四维呢？五维甚至更高维数呢？直观上**很难直接绘制更高维数的图像，这种行图像受到的限制也越来越多** 

### 2. 高维列图像

我们使用上面同样的例子，[![三维方程](https://github.com/Gre111/math/raw/master/images/01/LA_1_8.png)](https://github.com/Gre111/math/blob/master/images/01/LA_1_8.png) ，如果我们使用列图像的思路进行计算，那矩阵形式就变为：

[![三维方程的列形式](https://github.com/Gre111/math/raw/master/images/01/LA_1_11.png)](https://github.com/Gre111/math/blob/master/images/01/LA_1_11.png)

左侧是线性组合，右侧是合适的线性组合组成的结果，这样一来思路就清晰多了，“寻找线性组合”成为了解题关键。

[![三维方程的列图像](https://github.com/Gre111/math/raw/master/images/01/LA_1_10.jpg)](https://github.com/Gre111/math/blob/master/images/01/LA_1_10.jpg)

很明显这道题是一个特例，我们只需要取 **x = 0, y = 0, z = 1** 就得到了结果，这在**行图像**之中并不明显。

当然，之所以我们更推荐使用 **列图像** 求解方程， 是因为这是一种更系统的求解方法，即 **寻找线性组合**，而不用绘制每个行方程的图像之后寻找那个很难看出来的点。

另外一个优势在于，如果我们改变最后的结果 **b**，例如本题中，

[![改变列向量方程](https://github.com/Gre111/math/raw/master/images/01/LA_1_11.jpg)](https://github.com/Gre111/math/blob/master/images/01/LA_1_11.jpg)

那么我们 2 −1 1 0 −3 4 −3 就重新寻找一个线性组合就够了，但是如果我们使用的是行图像呢？那意味着我 们要完全重画三个平面图像，就简便性来讲，两种方法高下立判。

另外，还要注意的一点是对任意的 **b** 是不是都能求解 **Ax = b** 这个矩阵方程呢？ 也就是对 **3*3** 的系数矩阵 **A**，其列的线性组合是不是都可以覆盖整个三维空间呢？

对于我们举的这个例子来说，一定可以，还有我们上面 **2*2** 的那个例子，也可以覆盖整个平面，但是有一些矩阵就是不行的。

比如三个列向量本身就构成了一个 平面，那么这样的三个向量组合成的向量只能活动在这个平面上，肯定无法覆盖 **2 −1 1** 一个三维空间，

[![三个列向量](https://github.com/Gre111/math/raw/master/images/01/LA_1_12.jpg)](https://github.com/Gre111/math/blob/master/images/01/LA_1_12.jpg)

这三个向量就构成了一个平面。

[![Ax=b](https://github.com/Gre111/math/raw/master/images/01/LA_1_13.jpg)](https://github.com/Gre111/math/blob/master/images/01/LA_1_13.jpg)

### 3.3、矩阵乘法
![[Pasted image 20260226213929.jpg]]