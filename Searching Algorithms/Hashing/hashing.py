class hashing:
    def __init__(self):
        hashing.x=[]
    def dizi(self):
        
        for i in range(10):
            hashing.x+=[[0]*1]
       
    def ekle(self,sayi):
        mod=sayi%10
        hashing.x[mod]+=[sayi]
        print(hashing.x)
    def sil(self,sayi):
        mod=sayi%10
        a=0
        for i in hashing.x[mod]:
            if(hashing.x[mod]!=sayi):
                a+=1
        a-=1
        hashing.x[mod].pop(a)
        print(hashing.x[mod])  
a=hashing()
a.dizi()
a.ekle(3)
a.ekle(4)
a.ekle(10)
a.ekle(50)
a.sil(50)
a.ekle(11)
