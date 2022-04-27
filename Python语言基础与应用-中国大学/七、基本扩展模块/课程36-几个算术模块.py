"""基本算术模块
〉 math模块和cmath模块
〉 decimal模块
〉 fractions模块
〉 random模块
"""

# math模块
# math模块支持浮点数运算
# math.sin()/math.cos()/math.tan()
# math.pi Π = 3.14159…
# math.log(x,a) 以a为底的x的对数
# math.pow(x,y) x^y



# cmath模块支持复数运算
# cmath.polar() 极坐标
# cmath.rect() 笛卡尔坐标
# cmath.exp(x) e^x
# cmath.log(x,a) 以a为底的x的对数
# cmath.log10(x) 以10为底x的对数
# cmath.sqrt(x) x的平方根。
import cmath
from decimal import Decimal
print(Decimal('0.1')+Decimal('0.1')+Decimal('0.1')-Decimal('0.3'))

cmath.log(x[,base])