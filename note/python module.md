# pickle



# sqlalchemy

> ##简介





> ## 要点

### sqlalchemy操作手册

orm操作是所有完整软件中后端处理最重要的一部分，主要完成了后端程序和数据库之间的数据同步和持久化的操作，本文基于sqlalchemy官方文档进行整理，完成sqlalchemy的核心操作

------

### 目录

1. 什么是ORM 2
2. 常见的ORM操作流程和步骤 2
3. sqlalchemy基础操作 3
   3.1. 安装 3
   3.2. 连接引擎 3
   3.3. 连接会话 4
   3.4. ORM之Object操作 4
   3.4.1. 基础类 4
   3.4.2. 数据类型创建 5
   3.4.3. 数据类型映射操作 5
   3.5. 增加和更新 6
   3.6. 查询对象Query 6
   3.6.1. 常规查询query 6
   3.6.2. 指定排序查询 6
   3.6.3. 指定列查询 7
   3.6.4. 指定列属性别名 7
   3.6.5. 指定类型别名 7
   3.6.6. 切片查询 7
   3.7. 条件筛选filter 7
   3.7.1. 等值条件——equals / not equals 8
   3.7.2. 模糊条件——like 8
   3.7.3. 范围条件——in / not in 8
   3.7.4. 空值条件——is null / is not null 8
   3.7.5. 并且条件——AND 8
   3.7.6. 或者条件——OR 9
   3.7.7. SQL语句查询 9
   3.8. 查询结果 9
   3.8.1. all()函数返回查询列表 9
   3.8.2. filter()函数返回单项数据的列表生成器 9
   3.8.3. one()/one_or_none()/scalar()返回单独的一个数据对象 9

------

### 1. 什么是ORM

ORM：Object Relation Mapping，最初主要描述的是程序中的Object对象和关系型数据库中Rlation关系(表)之间的映射关系，目前来说也是描述程序中对象和数据库中数据记录之间的映射关系的统称，是一种进行程序和数据库之间数据持久化的一种编程思想。

### 2. 常见的ORM操作流程和步骤

常规情况下，软件程序中的ORM操作主要有四个操作场景：增、删、改、查
核心操作一般会区分为：增删改、查询

- 增删改操作

  增加操作

  ：程序中存在的一个对象Object数据，通过[ORM]核心模块进行增加的函数定义将对象保存到数据库的操作过程；如~注册操作中，通过用户输入的账号密码等信息创建了一个独立的对象，通过add()函数将对象增加保存到数据库中，数据库中就存在用户这个对象数据了。

  修改操作

  ：程序中存在的一个对象Object数据，有自己的id编号(可以是程序中自行赋值定义、更多的操作是从数据库中查询出来存在的一个对象)，通过[ORM]核心模块进行修改函数的定义将对象改变的数据更新到数据库中已经存在的记录中的过程；如~用户更改登录密码操作时，根据程序中查询得到的一个用户[id编号、账号、密码、..]，在程序中通过改变其密码属性数据，然后通过update()函数将改变的数据更新保存到数据库中，数据库中原来的数据就发生了新的改变。

  删除操作

  ：程序中存在的一个对象或者已知的id编号，通过主键编号或者对象的任意属性进行数据库中数据记录的删除的操作过程；如~管理员删除某个会员账号的操作，通过获取要删除会员的账号，然后通过delete()函数将要删除的会员信息告知数据库执行删除操作，数据库中的某条存在的数据记录就被删除掉了。

  ### 3. sqlalchemy基础操作

  ORM操作在实际项目中的应用非常多，涉及到的框架也是根据不同的项目有不同的处理模块，不过操作流程和步骤都是大同小异基本没有什么太大变化，唯一需要注意的就是在实际操作过程中你要使用的ORM框架的处理性能和是否支持事务、是否支持分布式等特性来进行确定使用哪个ORM框架进行操作，一般在python程序中ORM操作都是对mysqldb和pymysql这样的底层模块进行的封装处理。例如文章中要讲解的sqlalchemy就是底层封装mysqldb的实现，不过我们的在使用过程中需要使用pymysql进行替代。

  #### 3.1. 安装

  ...

  

#### 3.2. 连接引擎

使用sqlalchemy进行数据库操作，首先我们需要建立一个指定数据库的连接引擎对象
建立引擎对象的方式被封装在了sqlalchemy.create_engine函数中，通过指定的数据库连接信息就可以进行创建

创建数据库连接引擎时参数设置语法：

```
dialect[+driver]://user:password@host/dbname[?key=value..]
# 引入建立引擎的模块
from sqlalchemy import create_engine
# 创建一个和mysql数据库之间的连接引擎对象
engine = create_engine("mysql://root:root@localhost/py1709", 
encoding="utf-8", echo=True)
```

> 指定的数据库连接字符串表示了目标数据库的配置信息；encoding配置参数指定了和和数据库之间交换的数据的编码方式，同时echo参数表示随时在控制台展示和数据库之间交互的各种信息
> create_engine()函数返回的是sqlalchemy最核心的接口之一，该引擎对象会根据开发人员指定的数据库进行对应的sql api的调用处理
> 连接postgresql数据库：
> engine = create_engine("postgresql://scott:tiger@localhost/test")
> 连接mysql数据库：
> engine = create_engine("mysql://scott:tiger@hostname/dbname",
> encoding='utf-8', echo=True)
> 其他连接方式请参考官方文档：<http://docs.sqlalchemy.org/en/latest/>

#### 3.3. 连接会话

创建了数据库连接引擎对象之后，我们需要获取和指定数据库之间的连接，通过连接进行数据库中数据的增删改查操作，和数据库的连接我们称之为和指定数据库之间的会话，通过指定的一个模块

```
sqlalchemy.sessionmaker进行创建
# 引入创建session连接会话需要的处理模块
from sqlalchemy.orm import sessionmaker
# 创建一个连接会话对象；需要指定是和那个数据库引擎之间的会话
Session = sessionmaker(bind=engine)
session = Session()
# 接下来~就可以用过session会话进行数据库的数据操作了。
```

> PS:如果在创建会话的时候还没有指定数据库引擎，可以通过如下的方式完成会话操作
>
> ```
> Session = sessionmaker()
> ..
> Session.configure(bind=engine)
> session = Session()
> ..
> ```

#### 3.4. ORM之Object操作

我们的程序中的对象要使用sqlalchemy的管理，实现对象的orm操作，就需要按照框架指定的方式进行类型的创建操作，sqlalchemy封装了基础类的声明操作和字段属性的定义限制方式，开发人员要做的事情就是引入需要的模块并在创建对象的时候使用它们即可

基础类封装在sqlalchemy.ext.declarative.declarative_base模块中
字段属性的定义封装在sqlalchemy模块中，通过sqlalchemy.Column定义属性，通过封装的Integer、String、Float等定义属性的限制

##### 3.4.1. 基础类

创建基础类的方式如下：

```
# 引入需要的模块
from sqlalchemy.ext.declarative import declarative_base

# 创建基础类
BaseModel = declarative_base()
```

##### 3.4.2. 数据类型创建

创建数据模型的操作

```
# 引入需要的模块
from sqlalchemy import Column, String, Integer

# 创建用户类型
class User(BaseModel):
    # 定义和指定数据库表之间的关联
    __tabelname__ = “user”
    # 创建字段类型
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)
```

> PS：定义的数据类型必须继承自之前创建的BaseModel，同时通过指定**tablename**确定和数据库中某个数据表之间的关联关系，指定某列类型为primary_key设定的主键，其他就是通过Column指定的自定义属性了。
> sqlalchemy会根据指定的**tablename**和对应的Column列字段构建自己的accessors访问器对象，这个过程可以成为instrumentation，经过instrumentation映射的类型既可以进行数据库中数据的操作了。

##### 3.4.3. 数据类型映射操作

完成了类的声明定义之后，Declarative会通过python的metaclass对当前类型进行操作，根据定义的数据类型创建table对象，构建程序中类型和数据库table对象之间的映射mapping关系

通过类型对象的metadata可以实现和数据库之间的交互，有需要时可以通过metadata发起create table操作，通过Base.metadata.create_all()进行操作，该操作会检查目标数据库中是否有需要创建的表，不存在的情况下创建对应的表

```
..

if __name__ == “__main__”:
Base.metadata.create_all()
..
```

##### 3.5. 增加和更新

下面就是核心的数据对象的处理了，在程序代码中根据定义的数据类型创建对象的方式比较简单，执行如下的操作创建一个对象：

```
$ user = User(name=”tom”, age=18)
$ print(user.name)
tom
$ print(user.id)
None
```

通过会话对象将对象数据持久化到数据库的操作

```
$ session.add(user)
$ print(user.id)
None
$ session.commit()
$ print(user.id)
1
```

#### 3.6. 查询对象Query

Session是sqlalchemy和数据库交互的桥梁，Session提供了一个Query对象实现数据库中数据的查询操作

##### 3.6.1. 常规查询query

直接指定类型进行查询

```
user_list = session.query(User)
for user in user_list:
    print(user.name)
```

##### 3.6.2. 指定排序查询

通过类型的属性指定排序方式

```
user_list = session.query(User).order_by(User.id) # 默认顺序
user_list = session.query(User).order_by(-User.id) # 指定倒序
user_list = session.query(User).order_by(-User.id, User.name) # 多个字段
```

##### 3.6.3. 指定列查询

指定查询数据对象的属性，查询目标数据

```
user_list = session.query(User, User.name).all()
for u in user_list:
    print(u.User, u.name)
```

##### 3.6.4. 指定列属性别名

对于名称较长的字段属性，可以指定名称在使用时简化操作

```
user_list = session.query(Usre.name.label(‘n’)).all()

for user in user_list:
    print(user.n)
```

##### 3.6.5. 指定类型别名

对于类型名称较长的情况，同样可以指定别名进行处理

```
from sqlalchemy.orm import aliased

user_alias = aliased(User, name=’u_alias’)

user_list = session.query(u_alias, u_alias.name).all()
for u in user_list:
    print(u.u_alias, u.name)
```

##### 3.6.6. 切片查询

对于经常用于分页操作的切片查询，在使用过程中直接使用python内置的切片即可

```
user_list = session.query(User).all()[1:3]
..
```

#### 3.7. 条件筛选filter

前一节中主要是对于数据查询对象query有一个比较直观的感受和操作，在实际使用过程中经常用到条件查询，主要通过filter和filter_by进行操作，重点讲解使用最为频繁的filter条件筛选函数

##### 3.7.1. 等值条件——equals / not equals

```
# equals
session.query(User).filter(User.id == 1) # 相等判断
# not equals
session.query(User).filter(User.name != ‘tom’)# 不等判断
```

##### 3.7.2. 模糊条件——like

```
session.query(User).filter(User.name.like(‘%tom%’))
```

##### 3.7.3. 范围条件——in / not in

```
# IN
session.query(User).filter(User.id.in_([1,2,3,4]))

session.query(User).filter(User.name.in_([
     session.query(User.name).filter(User.id.in_[1,2,3,4])
]))

# NOT IN
session.query(User).filter(~User.id.in_([1,2,3]))
```

##### 3.7.4. 空值条件——is null / is not null

```
# IS NULL
session.query(User).filter(User.name == None)
session.query(User).filter(User.name.is_(None)) # pep8

# IS NOT NULL
session.query(User).filter(User.name != None)
session.query(User).filter(User.name.isnot(None)) # pep8
```

##### 3.7.5. 并且条件——AND

```
from sqlalchemy import and_

session.query(User).filter(User.name=’tom’).filter(User.age=12)
session.query(User).filter(User.name=’tom’, User.age=12)
session.query(User).filter(and_(User.name=’tom’, User.age=12))
```

##### 3.7.6. 或者条件——OR

```
from sqlalchemy import or_
session.query(User).filter(or_(User.name=’tom’, User.name=’jerry’))
```

##### 3.7.7. SQL语句查询

某些特殊情况下，我们也可能在自己的程序中直接使用sql语句进行操作

```python
from sqlalchemy import text
session.query(User).from_statement(
text(‘select * from users where name=:name and age=:age’))
.params(name=’tom’, age=12).all()
```

#### 3.8. 查询结果

##### 3.8.1. all()函数返回查询列表

```python
session.query(User).all()
[..]
```

##### 3.8.2. filter()函数返回单项数据的列表生成器

```python
ret = session.query(User).filter(..)
for d in rety:
  ...

<..>
```

##### 3.8.3. one()/one_or_none()/scalar()返回单独的一个数据对象

```pythonp
session.query(User).filter(..).one()/one_or_none()/scalar()
..
```



简单使用示意图

![屏幕快照 2019-04-19 下午8.34.35](/Users/suxiaohan/Desktop/屏幕快照 2019-04-19 下午8.34.35.png)



# pandas

> ## 简介

[中文API]("http://www.pypandas.cn")



> ## 要点

pandas + mysql + sqlalchemy的联合使用



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





