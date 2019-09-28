class Node:
    """BaşaEkleme,OrtayaEkleme,SonaEkleme,BasıSilme,OrtayıSilme,SonuSilme
    HeadGösterme,TailGösterme,DoublyLinkedListGösterme fonksiyonları bulunmaktadır"""
    def __init__(self,value):
        self.nextnode=None
        self.prevnode=None
        self.value=value
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def basaekle(self,data):
        new_node=Node(data)
        if(self.head==None):            
            self.head=new_node
            self.tail=self.head
        else:
            new_node.nextnode=self.head
            self.head.prevnode=new_node
            self.head=new_node        
    def sonaekle(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
        else:
            new_node.prevnode=self.tail
            self.tail.nextnode=new_node
            self.tail=new_node
    def ortayaekle(self,onceki,data):
        new_node=Node(data)
        temp=self.head
        while(temp.value!=onceki):
            temp=temp.nextnode
        new_node.nextnode=temp.nextnode
        new_node.nextnode.prevnode=new_node
        temp.nextnode=new_node
        new_node.prevnode=temp
    def bassil(self):
        self.head=self.head.nextnode
        self.head.prevnode=None
    def sonsil(self):
        self.tail=self.tail.prevnode
        self.tail.nextnode=None
    def ortasil(self,data):
        temp=self.head
        while(temp.value!=data):
            temp=temp.nextnode
        x=temp.nextnode
        y=temp.prevnode
        y.nextnode=temp.nextnode
        x.prevnode=temp.prevnode
        temp.nextnode=None
        temp.prevnode=None
        
                
    def headgoster(self):
        x=self.head
        print("LinkedList'imizin ilk elemanı = {}".format(x.value))
    def tailgoster(self):
       x=self.tail
       print("LinkedList'imizin son elemanı = {}".format(x.value))
    def goster(self):
        temp=self.head
        while(temp):
            print(temp.value)
            temp=temp.nextnode
a=DoublyLinkedList()
a.basaekle(4)
a.basaekle(3)
a.basaekle(2)
a.basaekle(1)
a.sonaekle(5)
a.sonaekle(6)
a.sonaekle(7)
a.ortayaekle(3,333)
a.basaekle(0)
a.sonaekle(8)
a.bassil()
a.bassil()
a.sonsil()
a.ortasil(3)
a.goster()
a.headgoster()
a.tailgoster()