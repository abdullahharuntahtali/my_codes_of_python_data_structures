class Node:
    """BaşaEkleme,OrtayaEkleme,SonaEkleme,BasıSilme,OrtayıSilme,SonuSilme
    HeadGösterme,TailGösterme,DoublyLinkedListGösterme fonksiyonları bulunmaktadır"""
    def __init__(self,value):
        self.value=value
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def basaekle(self,data):
        new_node=Node(data)
        new_node.next=self.head
        self.head=new_node
    def sonaekle(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=self.head
        else:
            temp=self.head
            while temp.next!=None:
                temp=temp.next
            temp.next=new_node
            self.tail=new_node
    def ortayaekle(self,onceki,data):
        new_node=Node(data)
        temp=self.head
        
        while(temp.value!=onceki):
            temp=temp.next
        new_node.next=temp.next
        temp.next=new_node
    def bassil(self):
        self.head=self.head.next
    def sonsil(self):
        temp=self.head
        while(temp.next!=self.tail):
            temp=temp.next
        temp.next=None
        self.tail=temp
    def ortasil(self,data):
        temp=self.head
        while(temp.next.value!=data):
            temp=temp.next
        temp.next=temp.next.next
    def headgoster(self):
        x=self.head
        print("LinkedList'imizin ilk elemanı = {}".format(x.value))
    def tailgoster(self):
       x=self.tail
       print("LinkedList'imizin son elemanı = {}".format(x.value))
        
    def goster(self):
        temp=self.head
        while temp:
            print(temp.value)
            temp=temp.next
a=LinkedList()
a.basaekle(5)
a.basaekle(4)
a.basaekle(3)
a.basaekle(2)
a.basaekle(1)
a.sonaekle(6)
a.basaekle(0)
a.ortayaekle(3,99)
a.sonaekle(7)
a.goster()
a.headgoster()
a.tailgoster()
a.bassil()
a.sonsil()
a.ortasil(99)
a.goster()