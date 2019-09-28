class deneme:
    def __init__(self):
        self.index=0
        self.boyut=1
        self.dizi=[None]*self.boyut
    def bak(self,x):
        if(x<0 or x>self.index):
            print("hata")
        else:
            print(self.dizi[x])
    def ekle(self,k):
        if (len(self.dizi)==self.index):
            self.boyut=self.dizigenislet(self.boyut)
        self.dizi[self.index]=k
        self.index+=1
    def dizigoster(self):
        print(self.dizi)
    def dizigenislet(self,boyut):
        boyut*=2
        yeni=[None]*boyut
        for i in range(0,len(self.dizi)):
            yeni[i]=self.dizi[i]
        self.dizi=yeni
        return boyut
x=deneme()
x.ekle(1)
print("İndex = {} \nDizi Boyutu= {} ".format(x.index,x.boyut))
x.dizigoster()
x.ekle(2)
print("İndex = {} \nDizi Boyutu= {} ".format(x.index,x.boyut))
x.dizigoster()
x.ekle(3)
print("İndex = {} \nDizi Boyutu= {} ".format(x.index,x.boyut))
x.dizigoster()
x.ekle(4)
print("İndex = {} \nDizi Boyutu= {} ".format(x.index,x.boyut))
x.dizigoster()
x.ekle(5)
print("İndex = {} \nDizi Boyutu= {} ".format(x.index,x.boyut))
x.dizigoster()
