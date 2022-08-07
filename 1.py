# -*- coding: cp1251 -*-
import random
Array = []
ReserveArray = []
AccessingArray = []
MemSize = 0
s = 0

class Descriptors:
    def __init__(self, Number, A, P, Size, BaseAdress, In, Out):
        self.Number = Number
        self.A = A
        self.P = P
        self.Size = Size
        self.BaseAdress = BaseAdress
        self.In = In
        self.Out = Out
        
for i in range(30):
    j = random.randint(35, 40)
    Desc = Descriptors(i, 0, 0, j, s, 0, 0)
    ReserveArray.append(s)
    s += j
    Array.append(Desc)

for i in range(1000):
    j = random.randint(0, 29)
    AccessingArray.append(j)
        
def Func(MemSize):
    global Array, ReserveArray, s
    s = 0
    Change = 0
    Position = 0
    TempEnd = 0
    Remain = MemSize
    
    for i in range(30):
        Array[i].A = 0
        Array[i].In = 0
        Array[i].Out = 0
        Array[i].BaseAdress = ReserveArray[i]
        s += Array[i].Size
        if s < MemSize:
            Array[i].P = 1
        else:
            Array[i].P = 0
        
    for i in range(1000):
        j = AccessingArray[i]
        if Array[j].P != 1:
            while (Remain < Array[j].Size):
                TempMin = 1000
                for t in range(30):
                    if Array[t].P == 1:
                        if Array[t].A < TempMin:
                            TempMin = Array[t].A
                            Position = Array[t].Number
                Array[Position].P = 0
                Array[Position].Out += 1
                Remain += Array[Position].Size
            Remain -= Array[j].Size
            for t in range(Position, 29):
                if Array[t].P == 1:
                    Array[t].BaseAdress -= Array[Position].Size
                    TempEnd = Array[t].BaseAdress + Array[t].Size
            Array[j].BaseAdress = TempEnd
            Array[j].P = 1
            Array[j].In += 1
            Change += 1
        Array[j].A += 1
    print ("The number of changes is ", Change)
    
    for i in range(30):
        print ("The number of inchanges in №", i,  "=", Array[i].In)
        print ("The number of outchanges in №", i, "=", Array[i].Out)

print ("1 Enter the size of memory")
MemSize = int(input())
Func(MemSize)

print ("2 Enter the size of memory")
MemSize = int(input())
Func(MemSize)

print ("3 Enter the size of memory")
MemSize = int(input())
Func(MemSize)
