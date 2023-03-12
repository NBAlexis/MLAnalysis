# 这是一个Python基础教学1

# Python的语法相对比较简单，这个是我们需要掌握的一些最基础的东西

# 变量赋值，显示


a = 3
# **符号表示次方, 如果a是整数，%表示余数
print("结果1：", a, a - 1, a * 2, a / 1.5, a ** 3, a % 2)


# 字符串


b = "5"
# 把数字变成字符串
c = str(a)
# 字符串可以相加连接在一起
print("结果2：", a, b, b + c)
# "{} {} {}".format(a, b, c)是把a, b, c按顺序填到{}位置。很方便的一种用法
print("结果3：", "{} {} {}".format(1, a, b))


# 数组（列表）


lista = [1, 2, 3, 4, 5]
print("结果4：", lista)
print("结果5：", lista[0], lista[1], lista[4])
# 列表长度
print("结果6：", len(lista))
# 2维列表
listb = [[1, 2], [3, 4]]
print("结果7：", listb)
print("结果8：", listb[0], listb[0][1])
print("结果9：", len(listb), len(listb[1]))
# 改一改列表的内容
listb[0] = [2, 1]
listb[1][0] = 4
print("结果10：", listb)
# 往列表里加东西
listb = listb + [[5, 6]]
print("结果11：", listb, len(listb), len(listb[0]))
# 去掉列表里的东西
del listb[1]
print("结果12：", listb, len(listb), len(listb[0]))


# 循环，和条件判断


for i in range(3, 7):
    # 注意这里前面必须加4个空格，表示缩进，缩进后的代码都是"for"统治下的
    print("结果13：", i)
    if 5 == i:
        # 注意这里前面必须加4个空格，表示缩进，缩进后的代码都是"if"统治下的
        print("结果14：", i)
for x in [0.1, 0.3, 0.77]:
    print("结果15：", x)
# 我们以冰雹猜想为例（百度一下冰雹猜想）
# https://baike.baidu.com/item/%E5%86%B0%E9%9B%B9%E7%8C%9C%E6%83%B3/659469?fr=aladdin
# 如果是奇数，那么把它变成3n + 1
# 如果是偶数，那么把它变成n / 2
# 从任何一个数字出发，都能回到1
n = 123
while n != 1:
    print("结果16：", n)
    if 0 == (n % 2):
        n = n / 2
    else:
        n = 3 * n + 1


# 函数，函数调用


# 定义一个函数
def func1(a, b):
    # 注意这里前面必须加4个空格，表示缩进，缩进后的代码都是这个函数统治下的
    return a * a + b * b
# 定义一个函数
def func2(lista):
    retvalue = 0
    for v in lista:
        retvalue = retvalue + v**2
    return retvalue
# 调用函数
print("结果17：", func1(3, 4))
print("结果18：", func2([3, 4]))
print("结果19：", func2([1, 2, 3, 4, 5]))
