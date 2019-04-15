# scipy

> ## 简介



> ##要点





# numpy

> ## 简介
>
> NumPy系统是Python的一种开源的数值计算扩展。这种工具可用来存储和处理大型矩阵，比Python自身的嵌套列表（nested list structure)结构要高效的多（该结构也可以用来表示矩阵（matrix））。
>
> [Numpy中文文档]('<https://www.numpy.org.cn/>')





> ## 要点

+ **Numpy底层使用C语言编写，内部解除了GIL（全局解释器锁），其对数组的操作速度不受Python解释器的限制，效率远高于纯Python代码。**



> ## note

### 数组(array)

My_array = np.array([1,2,3])

创建零数组：np.zero（（N*M））

创建随机数组:np.random.random((N*M)) //随机值在0~1之间

创建1数组:np.ones((N*M))

多维数组的提取：array[row1:row2:step,col1:col2:step]



---------

> 数组操作

使用NumPy，你可以轻松地在数组上执行数学运算。例如，你可以添加NumPy数组，你可以减去它们，你可以将它们相乘，甚至可以将它们分开。 以下是一些例子：

```python
import numpy as np 
a = np.array([[1.0, 2.0], [3.0, 4.0]]) 
b = np.array([[5.0, 6.0], [7.0, 8.0]]) 
sum = a + b 
difference = a - b 
product = a * b 
quotient = a / b 
print "Sum = \n", sum 
print "Difference = \n", difference 
print "Product = \n", product 
print "Quotient = \n", quotient 

# The output will be as follows: 

Sum = [[ 6. 8.] [10. 12.]]
Difference = [[-4. -4.] [-4. -4.]]
Product = [[ 5. 12.] [21. 32.]]
Quotient = [[0.2 0.33333333] [0.42857143 0.5 ]]
```

如你所见，乘法运算符执行逐元素乘法而不是矩阵乘法。 要执行矩阵乘法，你可以执行以下操作：

```python
matrix_product = a.dot(b) 
print "Matrix Product = ", matrix_product
```

输出将是：

```
[[19. 22.]

[43. 50.]]
```

> 数组属性

```python
 Array properties
a = np.array([[11, 12, 13, 14, 15],
              [16, 17, 18, 19, 20],
              [21, 22, 23, 24, 25],
              [26, 27, 28 ,29, 30],
              [31, 32, 33, 34, 35]])

print(type(a)) # >>><class 'numpy.ndarray'>
print(a.dtype) # >>>int64
print(a.size) # >>>25
print(a.shape) # >>>(5, 5)
print(a.itemsize) # >>>8
print(a.ndim) # >>>2#维度
print(a.nbytes) # >>>200
```

`itemsize`属性是每个项占用的字节数。这个数组的数据类型是int 64，一个int 64中有64位，一个字节中有8位，除以64除以8，你就可以得到它占用了多少字节，在本例中是8。

`nbytes` 属性是数组中的所有数据消耗掉的字节数。你应该注意到，这并不计算数组的开销，因此数组占用的实际空间将稍微大一点。



### 数组特殊运算符

NumPy还提供了一些别的用于处理数组的好用的运算符。

```python
# dot, sum, min, max, cumsum
a = np.arange(10)

print(a.sum()) # >>>45
print(a.min()) # >>>0
print(a.max()) # >>>9
print(a.cumsum()) # >>>[ 0  1  3  6 10 15 21 28 36 45]
```

sum()、min()和max()函数的作用非常明显。将所有元素相加，找出最小和最大元素。

然而，cumsum()函数就不那么明显了。它将像sum()这样的每个元素相加，但是它首先将第一个元素和第二个元素相加，并将计算结果存储在一个列表中，然后将该结果添加到第三个元素中，然后再将该结果存储在一个列表中。这将对数组中的所有元素执行此操作，并返回作为列表的数组之和的运行总数。

> 索引进阶
>
> 花式索引

`花式索引` 是获取数组中我们想要的特定元素的有效方法。

```python
# Fancy indexing
a = np.arange(0, 100, 10)
indices = [1, 5, -1]
b = a[indices]
print(a) # >>>[ 0 10 20 30 40 50 60 70 80 90]
print(b) # >>>[10 50 90]
```

正如你在上面的示例中所看到的，我们使用我们想要检索的特定索引序列对数组进行索引。这反过来返回我们索引的元素的列表。

> 布尔屏蔽

布尔屏蔽是一个有用的功能，它允许我们根据我们指定的条件检索数组中的元素。

```python
# Boolean masking
import matplotlib.pyplot as plt

a = np.linspace(0, 2 * np.pi, 50)
b = np.sin(a)
plt.plot(a,b)
mask = b >= 0
plt.plot(a[mask], b[mask], 'bo')
mask = (b >= 0) & (a <= np.pi / 2)
plt.plot(a[mask], b[mask], 'go')
plt.show()
```

上面的示例显示了如何进行布尔屏蔽。你所要做的就是将数组传递给涉及数组的条件，它将为你提供一个值的数组，为该条件返回true。

该示例生成以下图：

![布尔掩码结果图](https://www.numpy.org.cn/static/images/article/numpy_masking-1.png)

我们利用这些条件来选择图上的不同点。蓝色点(在图中还包括绿点，但绿点掩盖了蓝色点)，显示值大于0的所有点。绿色点表示值大于0且小于一半π的所有点。

> 缺省索引

不完全索引是从多维数组的第一个维度获取索引或切片的一种方便方法。例如，如果数组a=[1，2，3，4，5]，[6，7，8，9，10]，那么[3]将在数组的第一个维度中给出索引为3的元素，这里是值4。

```python
# Incomplete Indexing
a = np.arange(0, 100, 10)
b = a[:5]
c = a[a >= 50]
print(b) # >>>[ 0 10 20 30 40]
print(c) # >>>[50 60 70 80 90]
```

> Where 函数

where() 函数是另外一个根据条件返回数组中的值的有效方法。只需要把条件传递给它，它就会返回一个使得条件为真的元素的列表。

```python
# Where
a = np.arange(0, 100, 10)
b = np.where(a < 50) 
c = np.where(a >= 50)[0]
print(b) # >>>(array([0, 1, 2, 3, 4]),)
print(c) # >>>[5 6 7 8 9]
```





