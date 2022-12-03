# 2022-11-27 14:32:38
class LRUCache:

    def __init__(self, capacity: int):
        self.table = {}
        self.track = []*capacity
        self.cap = capacity

    def get(self, key: int) -> int:
        if key in self.table:
            self.track.remove(key)
            self.track.insert(0, key)

        return self.table.get(key, -1)

    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.table[key] = value
            self.track.remove(key)
            self.track.insert(0, key)

        elif self.cap != 0:
            self.table[key] = value
            self.track.insert(0, key)
            self.cap -= 1
        else:
            self.table.pop(self.track[-1], None)
            self.track.insert(0, key)
            self.track = self.track[:-1]

            self.table[key] = value

class Node:
    def __init__(self,key=None,value=None):
    
        self.key=key
        self.val=value
        self.next=None
        self.prev=None
class LRUCache:

    def __init__(self, capacity: int):
        self.table={}
        self.head=Node()
        self.tail=Node()    
        self.cap=capacity
        self.head.next=self.tail
        self.tail.next=self.head
        
    def deleteN(self,key):
        todel=self.table[key]
        todel.prev.next=todel.next
        todel.next.prev=todel.prev
        self.table.pop(key,None)
        
  
    def add(self,key,value):
        curr=Node(key,value)
        curr.next=self.head.next       
        curr.prev=self.head
        self.head.next.prev=curr
        self.head.next=curr
        self.table[key]=curr
        
        
        

        

    def get(self, key: int) -> int:
        if key not in self.table:
            return -1
        
        temp=self.table[key].val
        self.deleteN(key)

        self.add(key,temp)

        
        return temp
        
        
        
    def put(self, key: int, value: int) -> None:
        if key in self.table:
            self.deleteN(key)
            self.add(key,value)

            # self.table[key]=temp
        elif len(self.table)!=self.cap:
            self.add(key,value)
        else:
            getK=self.tail.prev.key
            self.deleteN(getK)
            self.add(key,value)
            
        
            
            
        