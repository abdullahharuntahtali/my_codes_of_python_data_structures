import appendinsertvepopfonksiyonu
class Queue: #FIFO İLK GİREN İLK ÇIKAR
    def __init__(self):
        self.dizi=list()
    def isEmpty(self):
        return self.dizi==[]
    def enqueue(self,eleman) :#elemanı başa ekler
        self.dizi=appendinsertvepopfonksiyonu.insert(self.dizi,0,eleman)
        print(self.dizi)
    def dequeue(self): #İlk eklenen elamanı yani son indexteki elemanı siler
        self.dizi=appendinsertvepopfonksiyonu.pop(self.dizi)
        print(self.dizi)
    def size(self):
        print(len(self.dizi))

x=Queue()
x.enqueue(0)
x.enqueue(1)
x.enqueue(2)
x.enqueue(3)
x.enqueue(4)
x.dequeue()
x.dequeue()
x.dequeue()
x.dequeue()
