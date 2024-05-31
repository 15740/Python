#课件二全部内容


# import keyword
# print(keyword.kwlist)
# print(len(keyword.kwlist))  #获取子的个数

"""
true='真'
True='真'    #True是Python中的保留字
"""

"""
print('luck_number的数据类型是：'.type(luck_number))
print(my_name,'的幸运数字是：',luck_number)

#   Python动态修改变量的数字类型，通过赋不同类型的值就可以直接修改
luck_number='北京欢迎你'
print('luck_number的数据类型是：'.type(luck_number))
"""

#在Python中允许多个变量指向同一个值
# no=number=1204      #no与number都指向了1204这个参数值
# print(no,number)
# print(id(no)) #id查看对象的内存地址的
# print(id(number))

# p1=3.1415926 #定义了一个变量
# PI=3.1415926 #定义了一个常量、

"""
num=987 #默认是十进制，表示整数
num2=0b1010101 #使用二进制表示整数
num3=0o765     #使用八进制表示整数
num4=0x87ABF   #使用十六进制表示整数
print(num)
print(num2)
print(num3)
print(num4)
"""

# x=10
# y=10.0
# print('x的数据类型：',type(x))    #int
# print('y的数据类型：',type(y))    #float
# x=1.99E1413
# print('科学计数法：',x,'x的数据类型',type(x))


# print(0.1+0.2)#不确定的尾数问题
# print(round(0.1+0.2,1)) #0.3

# x=123+456j
# print('实数部分：',x.real)
# print('虚数部分',x.imag)


# print('hello\tooo')     #hello是5个字符，一个制表位是8个字符
# print('hello\toooooo')
# print('hellooooooo')
# print('老师说：\'好好学习，天天向上\'')


#原字符，是转义字符失效的符号r或R
# print('北\n京\n欢\n迎你')
# print(r'北\n京\n欢\n迎你')
# print(R'北\n京\n欢\n迎你')

"""
s='HELLOWORLD'
print(s[0],s[-10])  #序号0和序号-10表示的是同一个字符
print('北京欢迎你'[4])#获取字符串中索引为4
print('北京欢迎你'[-1])
print(s[2:7])       #从2开始到7结束不包含7，正向递增
print(s[-8:-3])     #反向递增
print(s[:5])        #默认N从0开始
print(s[5:])        #M  默认是切到字符串的结尾
"""

#
# x='2022'
# y='北京冬奥会'
# print(x+y) #连接两个字符
# print(x*10)#对x这个字符串的内容复制10次
# print(10*x)
#
# print('北京' in y)#True
# print('上海' in y)#Flase


# x=True
# print(x)
# print(type(x))
# print(x+10) #11
# print(False+10)#10


# print('----------------------')
# print(bool(18)) #测试一下整数18的布尔值 True
# print(bool(0),bool(0.0)) #False
# #总结：非0的整数的布尔值都是True
# print(bool('北京欢迎你'))#True
# print(bool('')) #False

# print(bool(False))
# print(bool(None))


#
# x=10
# y=3
# z=x/y   #   在执行除法运算的时候，将运算的结果赋值给z
# print(z,type(z)) #  隐式转换，通过运算隐式的转了结果的类型
#
# #float类型转成int类型，只保留整数部分
# print('float类型转成int类型：',int(3.14))
# print('float类型转成int类型：',int(3.9))
# print('float类型转成int类型：',int(-3.14))
# print('float类型转成int类型：',int(-3.9))
# #   将int类型转成float类型
# print('int类型转成float类型：',float(10))
# 将 str转成int类型
# print(int('100')+int('200'))
#将字符串转成int或float时报错的情况
# print(int('18a'))#ValueError: invalid literal for int() with base 10: '18a'
# print(int('3.14'))#ValueError: invalid literal for int() with base 10: '3.14'
# print(float('45a.987'))#ValueError: could not convert string to float: '45a.987'

#chr()ord()一对
# print(ord('杨'))     #杨在Unicode表中对应的整数值
# print((chr(26472))) #26472整数在Unicode表中对应的字符
#
# #   进制之间的转换操作，十进制与其他进制之间的转换
# print('十进制转成十六进制：',hex(26472))
# print('十进制转成八进制：',oct(26472))
# print('十进制转成二进制：',bin(26472))

#
# s='3.14+3'
# print(s,type(s))
# x=eval(s)           #使用 eval函数去掉=这个字符串中左右的引号，执行加法运算
# print(x,type(x))

#  eval()函数经常与input()函数一起使用，用来获取用户输入的数值
# age=eval(input('请输入您的年龄：')) #将字符串转成int类型，相当于int(age)
# print(age,type(age))
#
# height=eval(input('请输入您的身高：'))
# print(height,type(height))


# hello='北京欢迎你'
# print(hello)
# print(eval('hello')) #输出了”北京欢迎你“
# print(eval('hello'))

#
# print('加法：',1+1)
# print('减法：',1-1)
# print('乘法：',2*3)
# print('除法：',10/2)
# print('整除：',10//3)
# print('取余：',10%3)
# print('幂运算：',2**4) #2*2*2*2
# print(10/0)  #ZeroDivisionError: division by zero


# x=20  #直接赋值，将20赋值给左侧变量x
# y=10
# x=x+y #将x+y的和赋值给x，x的值为30
# x+=y  #40  相当于x=x+y
# x-=y  # 相当于x=x-y
# print(x)
# x*=y
# print(x)#300
# x/y
# print(x)
# print(type(x))
# x%=2
# print(x)
# z=3
# y//=z
# print(y)
# y**=2
# print(y)


# a=b=c=100
# print(a,b,c)
# #Python支持系列解包赋值
# a,b=10,20
# print(a,b)
#
# print('-----如何交换两个变量的值呢？-----')
# a,b=b,a
# print(a,b)

# print('98大于90吗？',98>90)
# print('98小于90吗？',98<90)
# print('98等于90吗？',98==90)
# print('98不等于90吗？',98!=90)
# print('98大于等于90吗？',98>=90)
# print('98小于等于90吗？',98<=90)


"""
print(True and True)
print(True and False)
print(False and False)
print(False and True)
print('-'*40)

print(8>7 and 6>5) #True
print(8>7 and 6<5)
print(8<7 and 10/0)#False

print('-'*40)
print(True or True)
print(True or False)
print(False or False)
print(False or True)

print('-'*40)
print(8>7 or 10/0)
print('-'*40)
print(not True)#False
print(not False)#True
print(not (8>7))#False
"""

# print('按位与运算：',12&8)
# print('按位或运算；',4|8)
# print('按位异或运算符；',31^22)
# print('按位取反：',~123)
#
# print('左移位：',2<<2)
# print('左移位：',2<<3)
# print('右移位：',8>>2)
# print('右移位：',-8>>2)

"""
习题一
从键盘获取一个4位整数，分别输出个位、十位、百位、千位上的数字。
需求：
使用eval()函数或者int()函数将从获取的数字串转成int类型，通过整除和取余操作分别获取数字。

"""
"""
# 从键盘获取一个4位整数，可以使用 input() 函数获取用户输入的字符串
# 由于我们想要获取整数，可以将输入转换为 int 类型
# 使用 int() 函数将输入转换为整数
number = int(input("请输入一个4位整数："))

# 获取个位上的数字
last_digit = number % 10

# 获取十位上的数字
second_last_digit = (number % 100) // 10

# 获取百位上的数字
third_last_digit = (number % 1000) // 100

# 获取千位上的数字
first_last_digit = number // 1000

# 输出结果
print("个位上的数字是：", last_digit)
print("十位上的数字是：", second_last_digit)
print("百位上的数字是：", third_last_digit)
print("千位上的数字是：", first_last_digit)
"""


"""
习题二
根据父母身高预测儿子的身高。
需求：
从键盘输入父母的身高，并使用eval()或float()转换输入的数据类型。
计算公式：儿子身高=(父亲身高+母亲身高)*0.54
"""
# 从键盘获取父亲和母亲的身高
father_height = float(input("请输入父亲的身高（单位：米）："))
mother_height = float(input("请输入母亲的身高（单位：米）："))

# 使用公式计算儿子的身高
son_height = (father_height + mother_height) * 0.54

# 输出结果
print("根据父母身高预测，儿子的身高大约为：", son_height, "米")