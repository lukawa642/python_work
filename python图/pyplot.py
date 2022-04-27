# 一、matplotlib库的介绍
# Matplotlib库是一个非常强大的二维绘图库
# Matplotlib库与NumPy库都是科学计算生态系统SciPy中的一个组成部分，两个库无缝连接
# Matplotlib提供了两个便捷的绘图子模块
#      %pyplot:通过简单的退户函数实现不同的绘图功能
#      %pylab:使用方法与pyplot模块类似
# 二、pyplot模块的使用
import matplotlib.pyplot as plt
import matplotlib
import numpy as np

matplotlib.rcParams['font.family'] = 'SimHei'  # 设置中文字体为黑体
matplotlib.rcParams['axes.unicode_minus'] = False
x = np.linspace(0, 10, 100)
y = np.sin(x)
plt.plot(x, y, "r*")
f1 = plt.figure(256)
plt.title("我是图表题")
plt.xlabel("我是X轴标签")
plt.xlabel("我是Y轴标签")
plt.text(np.pi, 0.6, "我是图文字")
plt.ylim(-2, 2)
plt.legend(labels=["我是图例"])
plt.show()

# 三、pyplot.plot()绘图函数的使用
# plot()函数是pyplot模块中最基本的一个绘图函数，其基本格式如下：
#    plot(x,y,s,linewidth):在二维坐标系中绘制直线、曲线或者离散的点，返回一个列表对象
#     x：横坐标的取值范围，可选，省略时，默认用Y数据集的索引作为X
#     Y:与x对应的纵坐标的取值范围
#     s:控制线型的格式字符串，可选，省略时，绘制的线型采用默认格式linewidth:线的宽度
import matplotlib.pyplot as plt
plt.plot([1,2,3])
plt.show()
