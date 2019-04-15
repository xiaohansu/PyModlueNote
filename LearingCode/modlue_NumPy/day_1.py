import numpy as np 
import matplotlib.pyplot as plt 


array = np.array([[1,2,3],
                    [4,5,6],
                    [7,8,9]])

def c_zero():
    return np.zeros((3,3))

def c_ones():
    return np.ones((3,3))

def c_random():
    return np.random.random((3,3))

#简单的数组乘法*，只是逐项相乘，要实现矩阵相乘，要使用array.dot
def matrix_multiplication(arr1,arr2):
    return arr1.dot(arr2)

def drawLine():
    a = np.linspace(0,2*np.pi,50)
    b = np.sin(a)
    plt.plot(a,b)
    mask = b>=0
    plt.plot(a[mask],b[mask],'bo')
    mask = (b>=0) & (a<=np.pi/2)
    plt.plot(a[mask],b[mask],'go')
    plt.show()

#查找目标所在底标
def func_where():
    a = np.arange(0, 100, 10)
    b = np.where(a < 50) 
    c = np.where(a >= 50)[0]
    print(b) # >>>(array([0, 1, 2, 3, 4]),)
    print(c) # >>>[5 6 7 8 9]

if __name__ == '__main__':
    # arr1 = np.array([[2,0],[0,2]])
    # arr2 = np.array([[1,1],[1,1]])
    # print(matrix_multiplication(arr2,arr1))
    drawLine()