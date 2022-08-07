# -*- coding: cp1251 -*-
import random
Array = []
ResourceArray = []
AccessingArray = []
RTime = 1
Num = 0
Num2 = 0
SWaiting = 0
R1L = random.randint(7, 12)
R2L = random.randint(5, 10)
R3L = random.randint(5, 10)
R4L = random.randint(5, 10)
R5L = random.randint(5, 10)
R6L = random.randint(5, 10)

class Process:
    def __init__(self, Number, N, Time, A, P, Waiting, LessTime):
        self.Number = Number
        self.N = N
        self.Time = Time
        self.A = A
        self.P = P
        self.Waiting = Waiting
        self.LessTime = LessTime

class Resource:
    def __init__(self, Number, R1, R2, R3, R4, R5, R6):
        self.Number = Number
        self.R1 = R1
        self.R2 = R2
        self.R3 = R3
        self.R4 = R4
        self.R5 = R5
        self.R6 = R6

for i in range(10):
    j = random.randint(1, 10)
    Proc = Process(i, 0, j, 0, 0, 0, 0)
    Array.append(Proc)
    print "The time of", i + 1, "process =", j

for i in range(10):
    j = random.randint(0, 3)
    k = random.randint(0, 3)
    l = random.randint(0, 3)
    m = random.randint(0, 3)
    n = random.randint(0, 3)
    o = random.randint(0, 3)
    Res = Resource(i, j, k, l, m, n, o)
    ResourceArray.append(Res)

for i in range(10):
    if (ResourceArray[i].R1 == 0) and (ResourceArray[i].R2 == 0) and (ResourceArray[i].R3 == 0)and (ResourceArray[i].R4 == 0) and (ResourceArray[i].R5 == 0) and (ResourceArray[i].R6 == 0):
        ResourceArray[i].R1 = 1
        
for i in range(20):
    j = random.randint(0, 9)
    AccessingArray.append(j)

#FCFS
for i in range(200):
    RTime -= 1
    for k in range(10):
        if (Array[k].A == 1) and (Array[k].P == 0):
            Array[k].Waiting += 1
    if i < 20:
        j = AccessingArray[i]
        if Array[j].A == 0:
            Array[j].A = 1
            Array[j].N = Num
            Num += 1
    if RTime == 0:
        for k in range(10):
            if Array[k].P == 1:
                Array[k].A = 0
                Array[k].P = 0
        TempMin = 11
        for k in range(10):
            if (Array[k].A == 1) and (Array[k].N < TempMin):
                TempMin = Array[k].N
                Num2 = Array[k].Number
                Array[Num2].P = 1
                RTime = Array[Num2].Time

for i in range(10):
    SWaiting += Array[i].Waiting
SWaiting = SWaiting / 10
print "The average waiting time in FCFS =", SWaiting

#SJF
Num = 0
SWaiting = 0
RTime = 1
for i in range(10):
    Array[i].A = 0
    Array[i].P = 0
    Array[i].Waiting = 0

for i in range(200):
    RTime -= 1
    for k in range(10):
        if (Array[k].A == 1) and (Array[k].P == 0):
            Array[k].Waiting += 1
    if i < 20:
        j = AccessingArray[i]
        if Array[j].A == 0:
            Array[j].A = 1
    if RTime == 0:
        for k in range(10):
            if Array[k].P == 1:
                Array[k].A = 0
                Array[k].P = 0
        TempMin = 11
        for k in range(10):
            if (Array[k].A == 1) and (Array[k].Time < TempMin):
                TempMin = Array[k].Time
                Num = Array[k].Number
                Array[Num].P = 1
                RTime = Array[Num].Time
      
for i in range(10):
    SWaiting += Array[i].Waiting
SWaiting = SWaiting / 10
print "The average waiting time in SJF =", SWaiting

#RR
Num = 0
Num2 = 0
NumRes = 11
SWaiting = 0
for i in range(10):
    Array[i].A = 0
    Array[i].P = 0
    Array[i].Waiting = 0

for i in range(200):
    for k in range(10):
        if (Array[k].A == 1) and (Array[k].P == 0):
            Array[k].Waiting += 1
    if i < 20:
        j = AccessingArray[i]
        if Array[j].A == 0:
            Array[j].A = 1
            Array[j].N = Num
            Array[j].LessTime = Array[j].Time
            Array[j].Waiting -= Array[j].Time
            Num += 1
    TempMin = 100
    for k in range(10):
        if (Array[k].A == 1) and (Array[k].N < TempMin) and (Array[k].P == 0):
            TempMin = Array[k].N
            Num2 = Array[k].Number
    if Num2 != NumRes:
        if (R1L - ResourceArray[Num2].R1 >= 0)or(R2L - ResourceArray[Num2].R2 >= 0)or(R3L - ResourceArray[Num2].R3 >= 0)or(R4L - ResourceArray[Num2].R4 >= 0)or(R5L - ResourceArray[Num2].R5 >= 0)or(R6L - ResourceArray[Num2].R6 >= 0):
            R1L -= ResourceArray[Num2].R1
            R2L -= ResourceArray[Num2].R2
            R3L -= ResourceArray[Num2].R3
            R4L -= ResourceArray[Num2].R4
            R5L -= ResourceArray[Num2].R5
            R6L -= ResourceArray[Num2].R6        
            Array[Num2].LessTime -= 1
            Array[Num2].P = 1
        NumRes = Num2
    else:
        for k in range(10):
            Array[k].P = 0
    if Array[Num2].LessTime == 0:
        Array[Num2].A = 0
        R1L += ResourceArray[Num2].R1
        R2L += ResourceArray[Num2].R2
        R3L += ResourceArray[Num2].R3
        R4L += ResourceArray[Num2].R4
        R5L += ResourceArray[Num2].R5
        R6L += ResourceArray[Num2].R6

for i in range(10):
    SWaiting += Array[i].Waiting
SWaiting = SWaiting / 10
print "The average waiting time in RR =", SWaiting
