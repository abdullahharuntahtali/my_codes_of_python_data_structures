import temp  #Bu Kütüphanemde append ve pop fonksiyonlarını kendim yazdım.Koduda aşağıda ;
"""def append(dizi,y):
    i=len(dizi)
    i+=1
    x=[None]*i
    for j in range (0,len(dizi)):
        x[j]=dizi[j]
    x[i-1]=y
    dizi=x
    return x
def pop(dizi):
    i=len(dizi)-1
    x=[None]*i
    
    for i in range(0,len(dizi)-1):
        x[i]=dizi[i]
    return x"""

class Stack:
    def __init__(self):
        self.dizi=[]
        self.sayac=0
    def isEmpty(self):
        return self.dizi==[]  #TRUE YADA FALSE
    def push(self,eleman):
        self.sayac+=1
        self.dizi=temp.append(self.dizi,eleman)
        
    def pop(self):
        self.dizi=temp.pop(self.dizi)
    def Top(self): #Son Elemanı Gösterir
        return self.dizi[len(self.dizi)-1]
    def boyut(self):
        return len(self.dizi)

x=Stack()
x.push(5)
print(x.dizi)
x.push(6)
print(x.dizi)
x.pop()
print(x.dizi)
x.push(99)
print(x.dizi)

print(x.Top())
print(x.boyut())