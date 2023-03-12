# 这是一个Python基础教学2
# 注意！ 在运行前，需要把sm-s05-1.lhco文件，放到Applications/IsolationForest/文件夹下

# 在这个K means用到的基础的程序，Lession1就是全部了。
# 但是，除了基础的以外，Python真正方便的是大量的库，我们需要用到主要4个库


# 第一个库，math
# math库里主要是一些常用的数学函数，需要用到任何数学函数的时候可以网上搜一下


# 导入math库
import math
# 举例
print("结果1：", math.sqrt(2), math.sin(2), math.atan(2), math.exp(2), math.log(2))



# 第二个库，文件
# 文件库的函数其实是基础程序，所以不需要导入什么


# 逐行读入文件
with open("Lession2-data1.txt") as f:
    # 注意这里前面必须加4个空格，缩进后的代码都是这个with统治下的，只有在这个统治内部才有'f'这个变量，这个变量表示文件
    for lines in f.readlines():
        print("结果2：", lines)
# 逐行写入数据
listToWrite = [
    [1, 2, 3, 4, 5],
    [0.1, 0.2, 0.3, 0.4, 0.5],
    [5, 4, 3, 2, 1],
]
# 'w'表示写入一个文件（如果有这个文件会被覆盖）
# 'a'表示写入一个文件（如果有这个文件会接着最后一行写）
with open("Lession2-data2.txt", 'w') as f:
    for line in listToWrite:
        for i in range(0, len(line)):
            if i == len(line) - 1:
                # 只能写入字符串，所以用str(...), '\n'表示换行
                f.write(str(line[i]) + "\n")
            else:
                f.write(str(line[i]) + ", ")
# 注意，不要写中文（包括全角符号）
# 写完后，你这里应该多了一个Lession2-data2.txt文件，打开看看
# 这种写好的数据文件，叫做csv文件，（百度一下什么叫csv文件）
# 我们来读一下刚才写的文件
# 这一次，为了复习前面学过的函数，我们写一个函数，然后调用一个函数
def ReadCSVFile(filename):
    retlist = []
    with open(filename) as f:
        for lines in f.readlines():
            # 读进来的是字符串"1, 2, 3, 4, 5"这种内容
            # Python里有把这种字符串，变成字符串数组的函数
            strlist = lines.split(',')
            # 此时numberlist = ["1", "2, "3, "4, "5"]数组
            # 为了避免读进来的空行影响程序正常运行，我们只对len(strlist) > 0进行后面的操作
            if len(strlist) > 0:
                # 我们还需要把它变成数字数组
                numberlist = []
                for v in strlist:
                    # 和str(...)把东西变成字符串类似，float(...)把字符串变成数
                    numberlist = numberlist + [float(v)]
                retlist = retlist + [numberlist]
    return retlist
# 调用一下写好的函数来读我们刚才写的文件
listToRead = ReadCSVFile("Lession2-data2.txt")
# 我们写进去的数组
print("结果3：", listToWrite)
# 我们读出来的数组
print("结果4：", listToRead)


# 第三个库，随机数
import random
# 生成0 - 3之间一个随机整数（包括0和3）
print("结果5：", random.randint(0, 3), random.randint(0, 3), random.randint(0, 3))
# 生成0 - 1之间一个随机小数
print("结果6：", random.uniform(0, 1), random.uniform(0, 1), random.uniform(0, 1))



# 第四个库，就是CutExperiment本库


# 读取lhco文件的函数 LHCO全名是LHC（大型强子对撞机Large Hadron Collider）的Olympics文件
# import一下
from Interfaces.LHCOlympics import LoadLHCOlympics
# 调用函数
allEvents = LoadLHCOlympics("sm-s05-1.lhco")
# allEvents是一个对撞机上的碰撞事例集合
# allEvents是一个"EventSet"类型的变量，"EventSet"的代码在"DataStructure/EventSet.py"
# 不需要掌握，我们只需要知道数据都在这个变量的"events"成员里面就行了。
print("结果7：", "碰撞事例的数量", len(allEvents.events))
# 一个碰撞事例意思是质子-质子对撞，生成了哪些粒子，粒子的种类和动量是什么，我们看看第一个事例
# allEvents.events是一个"EventSample"类型的数组，"EventSample"类型的代码在"DataStructure/EventSample"，
# 不需要掌握，我们只需要知道（1）数据都在这个变量的"particles"成员里面就行了。（2）这个类型有一个DebugPrint()函数，能把它的信息变成字符串
print("结果8", "第一个事例\n", allEvents.events[0].DebugPrint())
print("结果9：", "第一个事例，粒子的数量", len(allEvents.events[0].particles))
# allEvents.events[0].particles是一个数组，内容是Particles，在"DataStructure/Particles.py"
# 这个文件要仔细看一看了。
# Particles里包含很多成员变量：PGDid，particleType, momentum这三个成员变量是我们要用到的关键，其中momentum是一个LorentzVector
# LorentzVector在"DataStructure/LorentzVector.py"  这个文件也要仔细看一看了。

########################################
# 这个例子是我们做K means项目需要用到的
# 我们用两种不同的理论，分别叫SM和nTGC，使用CEPC（就是王怡芳和杨振宁争论的那个）模拟碰撞，产生了两组碰撞事例集合
# 我们这篇论文要做的研究就是，如果我们把这些事例混在一起，能不能使用k means，自动把这两个理论得到的事例分辨出来？
# sm-s05-1.lhco，就是使用SM在碰撞能量等于0.5 TeV时碰撞的结果
# 我们研究的过程是 正负电子对e+ e- 碰撞产生正负电子对+光子， 或正负mu子对+光子的过程
# 我们只知道碰撞结果有哪些粒子，粒子的动量，希望能用k means自动把这两个理论得到的事例分辨出来。
# 所以第一步，我们要从sm-s05-1.lhco挑出，末态确实有正负电子对(mu子对)+光子的过程，并挑出动量最大的正负电子和光子
# 我们挑出这些事例，并把他们的动量（3个粒子，每个动量是4矢量）一共12个数字排成一个数组。
#########################################
from DataStructure.Particles import *
import random
resultList = []
loopLength = 20  # 虽然我们有500000个事例，但作为例子，我们只看前20个事例
for i in range(0, loopLength):
    theEvent = allEvents.events[i]
    largestPhotonIndex = -1  # 对于一个list, list[i] 这个i通常叫index
    largestPhotonEnergy = 0
    largestElectronIndex = -1
    largestElectronEnergy = 0
    largestAntiElectronIndex = -1
    largestAntiElectronEnergy = 0
    largestMuonIndex = -1
    largestMuonEnergy = 0
    largestAntiMuonIndex = -1
    largestAntiMuonEnergy = 0
    for theParticle in theEvent.particles:
        if theParticle.particleType == ParticleType.Photon:
            # 我们找到一个光子，看看它的能量
            photonEnergy = theParticle.momentum.Momentum()
            if photonEnergy > largestPhotonEnergy:
                largestPhotonEnergy = photonEnergy
                # 注意，列表的index是Particles.index - 1，这是CutExperiment库规定的规则
                largestPhotonIndex = theParticle.index - 1
        elif theParticle.particleType == ParticleType.Electron:
            # PDGId > 0的粒子是正常粒子（即带负电的电子），这是CutExperiment库规定的规则
            if theParticle.PGDid > 0:
                electronEnergy = theParticle.momentum.Momentum()
                if electronEnergy > largestElectronEnergy:
                    largestElectronEnergy = electronEnergy
                    largestElectronIndex = theParticle.index - 1
            else:
                # PDGId < 0的粒子是反物质粒子（即带正电的反电子，也叫正电子），这是CutExperiment库规定的规则
                antielectronEnergy = theParticle.momentum.Momentum()
                if antielectronEnergy > largestAntiElectronEnergy:
                    largestAntiElectronEnergy = antielectronEnergy
                    largestAntiElectronIndex = theParticle.index - 1
        elif theParticle.particleType == ParticleType.Muon:
            # 基本是照抄上面的
            if theParticle.PGDid > 0:
                muonEnergy = theParticle.momentum.Momentum()
                if muonEnergy > largestMuonEnergy:
                    largestMuonEnergy = muonEnergy
                    largestMuonIndex = theParticle.index - 1
            else:
                antimuonEnergy = theParticle.momentum.Momentum()
                if antimuonEnergy > largestAntiMuonEnergy:
                    largestAntiMuonEnergy = antimuonEnergy
                    largestAntiMuonIndex = theParticle.index - 1
    # 到这里，我们已经用for查看了所有粒子
    if largestPhotonIndex >= 0 and largestElectronIndex >= 0 and largestAntiElectronIndex >= 0:
        # 如果我们找到了光子，正负电子对，那么按照电子，反电子，光子，把动量做成一个数组，加入到resultList
        # 一行写不下了，可以用 \换行（不推荐这种写法）
        dot1 = theEvent.particles[largestElectronIndex].momentum * theEvent.particles[largestAntiElectronIndex].momentum
        dot2 = theEvent.particles[largestElectronIndex].momentum * theEvent.particles[largestPhotonIndex].momentum
        dot3 = theEvent.particles[largestAntiElectronIndex].momentum * theEvent.particles[largestPhotonIndex].momentum
        momentumList = [dot1, dot2, dot3] + [0, random.randint(0, 1)]
        resultList = resultList + [momentumList]
        print("事例", i, "的内容是\n")
        print(theEvent.DebugPrint())
        print("我们找到正负电子对和光子，结果是", momentumList, "\n")
    elif largestPhotonIndex >= 0 and largestMuonIndex >= 0 and largestAntiMuonIndex >= 0:
        dot1 = theEvent.particles[largestMuonIndex].momentum * theEvent.particles[largestAntiMuonIndex].momentum
        dot2 = theEvent.particles[largestMuonIndex].momentum * theEvent.particles[largestPhotonIndex].momentum
        dot3 = theEvent.particles[largestAntiMuonIndex].momentum * theEvent.particles[largestPhotonIndex].momentum
        momentumList = [dot1, dot2, dot3] + [0, random.randint(0, 1)]
        resultList = resultList + [momentumList]
        print("事例", i, "的内容是\n")
        print(theEvent.DebugPrint())
        print("我们找到正负缪子对和光子，结果是", momentumList, "\n")
    else:
        print("事例", i, "的内容是\n")
        print(theEvent.DebugPrint())
        print("我们没找到正负电子（缪子）对和光子\n")

"""
allEvents2 = LoadLHCOlympics("nTGC-....lhco")
for i in range(0, loopLength):
    theEvent = allEvents2.events[i]
    largestPhotonIndex = -1  # 对于一个list, list[i] 这个i通常叫index
    largestPhotonEnergy = 0
    largestElectronIndex = -1
    largestElectronEnergy = 0
    largestAntiElectronIndex = -1
    largestAntiElectronEnergy = 0
    largestMuonIndex = -1
    largestMuonEnergy = 0
    largestAntiMuonIndex = -1
    largestAntiMuonEnergy = 0
    for theParticle in theEvent.particles:
        if theParticle.particleType == ParticleType.Photon:
            # 我们找到一个光子，看看它的能量
            photonEnergy = theParticle.momentum.Momentum()
            if photonEnergy > largestPhotonEnergy:
                largestPhotonEnergy = photonEnergy
                # 注意，列表的index是Particles.index - 1，这是CutExperiment库规定的规则
                largestPhotonIndex = theParticle.index - 1
        elif theParticle.particleType == ParticleType.Electron:
            # PDGId > 0的粒子是正常粒子（即带负电的电子），这是CutExperiment库规定的规则
            if theParticle.PGDid > 0:
                electronEnergy = theParticle.momentum.Momentum()
                if electronEnergy > largestElectronEnergy:
                    largestElectronEnergy = electronEnergy
                    largestElectronIndex = theParticle.index - 1
            else:
                # PDGId < 0的粒子是反物质粒子（即带正电的反电子，也叫正电子），这是CutExperiment库规定的规则
                antielectronEnergy = theParticle.momentum.Momentum()
                if antielectronEnergy > largestAntiElectronEnergy:
                    largestAntiElectronEnergy = antielectronEnergy
                    largestAntiElectronIndex = theParticle.index - 1
        elif theParticle.particleType == ParticleType.Muon:
            # 基本是照抄上面的
            if theParticle.PGDid > 0:
                muonEnergy = theParticle.momentum.Momentum()
                if muonEnergy > largestMuonEnergy:
                    largestMuonEnergy = muonEnergy
                    largestMuonIndex = theParticle.index - 1
            else:
                antimuonEnergy = theParticle.momentum.Momentum()
                if antimuonEnergy > largestAntiMuonEnergy:
                    largestAntiMuonEnergy = antimuonEnergy
                    largestAntiMuonIndex = theParticle.index - 1
    # 到这里，我们已经用for查看了所有粒子
    if largestPhotonIndex >= 0 and largestElectronIndex >= 0 and largestAntiElectronIndex >= 0:
        # 如果我们找到了光子，正负电子对，那么按照电子，反电子，光子，把动量做成一个数组，加入到resultList
        # 一行写不下了，可以用 \换行（不推荐这种写法）
        momentumList = theEvent.particles[largestElectronIndex].momentum.values \
                       + theEvent.particles[largestAntiElectronIndex].momentum.values \
                       + theEvent.particles[largestPhotonIndex].momentum.values \
                       + [1, random.randint(0, 1)]
        resultList = resultList + [momentumList]
        print("事例", i, "的内容是\n")
        print(theEvent.DebugPrint())
        print("我们找到正负电子对和光子，结果是", momentumList, "\n")
    elif largestPhotonIndex >= 0 and largestMuonIndex >= 0 and largestAntiMuonIndex >= 0:
        momentumList = theEvent.particles[largestMuonIndex].momentum.values \
                       + theEvent.particles[largestAntiMuonIndex].momentum.values \
                       + theEvent.particles[largestPhotonIndex].momentum.values \
                       + [1, random.randint(0, 1)]
        resultList = resultList + [momentumList]
        print("事例", i, "的内容是\n")
        print(theEvent.DebugPrint())
        print("我们找到正负缪子对和光子，结果是", momentumList, "\n")
    else:
        print("事例", i, "的内容是\n")
        print(theEvent.DebugPrint())
        print("我们没找到正负电子（缪子）对和光子\n")
"""

print("\n\n最终结果:\n", resultList)
# 接下来，把resultList保存成一个.csv文件就可以了。
