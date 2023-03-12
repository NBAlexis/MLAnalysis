#############################################
# 这一课，讲一讲K means算法
# K means，算法是用来把一堆数据点按照距离分成两部分的算法。
# 1 - 随机的给数据点分配一个类别（0或1）
# 2 - 计算所有0数据点的中心，计算所有1数据点的中心
# 3 - 如果一个数据点距离0比较近，把它分配到0，如果一个数据点距离1比较近，把它分配到1。并记住改了多少个。
# 4 - 如果改动的数量>0，回到2，否则结束
#############################################

# 我们用3维空间的点来举例（我们要做的是12维空间，3维空间只是方便说明）
# 我们用5个数的列表来做这个例子，[x, y, z, type1, type2]
# type1是我们希望看到的结果，比如我们要做的问题，我们自己是知道事例是SM还是nTGC理论的事例
# type2是kmeans得到的结果。最后我们比较type1和type2
# 我们这个例子里，type1指的是这个数据点是在(1,1,1)附近，还是(-1, -1, -1)附近。
dataSample = []
# 我们在(1, 1, 1)附近随机生成50个点
import random
for i in range(0, 50):
    # x, y, z是1.1.1加上一个从-1到1之间的随机数。type1是0，type2按照上面第一步，是0,1随机数。
    point = [1 + random.uniform(-1, 1), 1 + random.uniform(-1, 1), 1 + random.uniform(-1, 1), 0, random.randint(0, 1)]
    dataSample = dataSample + [point]

# 我们在(-1, -1, -1)附近随机生成50个点
for i in range(0, 50):
    point = [-1 + random.uniform(-1, 1), -1 + random.uniform(-1, 1), -1 + random.uniform(-1, 1), 1, random.randint(0, 1)]
    dataSample = dataSample + [point]


import math
changedPointCount = 1
while changedPointCount > 0:
    # 第2步，计算中心点，N个点的中心点就是它们坐标加一起除以N
    type0Center = [0, 0, 0]
    type0Count = 0
    type1Center = [0, 0, 0]
    type1Count = 0
    for i in range(0, len(dataSample)):
        if 0 == dataSample[i][13]:
            type0Center[0] = type0Center[0] + dataSample[i][0]
            type0Center[1] = type0Center[1] + dataSample[i][1]
            type0Center[2] = type0Center[2] + dataSample[i][2]
            type0Count = type0Count + 1
        else:
            type1Center[0] = type1Center[0] + dataSample[i][0]
            type1Center[1] = type1Center[1] + dataSample[i][1]
            type1Center[2] = type1Center[2] + dataSample[i][2]
            type1Count = type1Count + 1
    type0Center[0] = type0Center[0] / type0Count
    type0Center[1] = type0Center[1] / type0Count
    type0Center[2] = type0Center[2] / type0Count
    type1Center[0] = type1Center[0] / type1Count
    type1Center[1] = type1Center[1] / type1Count
    type1Center[2] = type1Center[2] / type1Count
    # 第3步，根据距离重新分配
    changedPointCount = 0
    for i in range(0, 100):
        distance0 = math.sqrt((type0Center[0] - dataSample[i][0])**2
                              + (type0Center[1] - dataSample[i][1])**2
                              + (type0Center[2] - dataSample[i][2])**2)
        distance1 = math.sqrt((type1Center[0] - dataSample[i][0])**2
                              + (type1Center[1] - dataSample[i][1])**2
                              + (type1Center[2] - dataSample[i][2])**2)
        if distance0 < distance1:
            # 把它分配到0，分配前看看是不是改变了
            if dataSample[i][13] != 0:
                changedPointCount = changedPointCount + 1
                dataSample[i][13] = 0
        else:
            # 把它分配到1
            if dataSample[i][13] != 1:
                changedPointCount = changedPointCount + 1
                dataSample[i][13] = 1
    print("发生改变的点数量：", changedPointCount)

# 上面的代码，如果changedPointCount > 0，会自动跳到2，如果不再改变会自动结束循环
# 我们看看结果
for thePoint in dataSample:
    print(thePoint)

# 从结果看，kmeans确实能够把这批点正确分成两部分（0和1可能会相反，这不重要）
