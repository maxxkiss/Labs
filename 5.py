import random
IndAr = []
FlAr = []
s = 0
k = 0

class Index:
    def __init__(self, Number, Belong):
        self.Number = Number
        self.Belong = Belong

class File:
    def __init__(self, Number, Size, State):
        self.Number = Number
        self.Size = Size
        self.State = State

for i in range(70):
    Ind = Index(i, 0)
    IndAr.append(Ind)

for i in range(10):
    j = random.randint(1, 5)
    Fl = File(i + 1, j, 0)
    FlAr.append(Fl)
       
for i in range(70):
    j = random.randint(1, 3)
    if (j == 3) and (s < 20):
        IndAr[i].Belong = 11
        s += 1
        
print ("Primary state:")
for i in range(70):
    print (IndAr[i].Belong)

for i in range(10):
    j = random.randint(0, 9)
    if FlAr[j].State == 0:
        s = FlAr[j].Size
        while s != 0:
            if IndAr[k].Belong == 0:
                IndAr[k].Belong = FlAr[j].Number
                s -= 1
            k += 1
        FlAr[j].State = 1
                
print ("State after saving:")
for i in range(70):
    print (IndAr[i].Belong)

for i in range(10):
    j = random.randint(0, 9)
    k = 0
    if FlAr[j].State == 1:
        s = FlAr[j].Size
        while s != 0:
            if IndAr[k].Belong == FlAr[j].Number:
                IndAr[k].Belong = 0
                s -= 1
            k += 1
        FlAr[j].State = 0

print ("State after deleting:")
for i in range(70):
    print (IndAr[i].Belong)
