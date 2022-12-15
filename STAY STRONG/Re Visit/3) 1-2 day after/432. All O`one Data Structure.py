class Node:
    def __init__(self, freq=0):

        self.freq = freq
        self.val = set()
        self.next = None
        self.prev = None


class AllOne:

    # table["name"]:Node(key)
    def printN(self):
        curr=self.head

        s=""
        while(curr!=None):
            s+=str(curr.freq) +" "+repr(curr.val)+" "
            curr=curr.next
        print(s)
    def __init__(self):
        self.table = {}
        self.head = Node()
        self.tail = Node()
        self.head.next = self.tail
        self.tail.prev = self.head

    def addMid(self, a, b, newNode):
        newNode.next = b
        newNode.prev = a
        
        a.next = newNode
        b.prev = newNode
    def remove(self,a):
        a.prev.next=a.next
        a.next.prev=a.prev

    def inc(self, key: str) -> None:

        if key in self.table:
            currNode = self.table[key]
            currNode.val.remove(key)
            
        else:
            currNode = self.head
       

        if currNode.freq+1 != currNode.next.freq:
            # create neew node in the middle of currNode and currNode.next
            # add key of curr into the new node freq

            
            temp = Node(currNode.freq+1)
            temp.val.add(key)
            self.addMid(currNode, currNode.next, temp)
            self.table[key]=temp
        else:
            # add key to the currNode.next.val
            currNode.next.val.add(key)
            self.table[key]=currNode.next
        if len(currNode.val) == 0 and  currNode!=self.head:
                self.remove(currNode)


    def dec(self, key: str) -> None:
        currNode = self.table[key]
        currNode.val.remove(key)
        if len(currNode.val) == 0:
            self.table.pop(key)
            self.remove(currNode)
        if currNode.freq == 1:
            return
        else:
            if currNode.prev.freq == currNode.freq-1:
                currNode.prev.val.add(key)
                self.table[key]=currNode.prev
            else:
                temp = Node(currNode.freq-1)
                temp.val.add(key)
                self.addMid(currNode.prev, currNode.next if len(currNode.val) == 0 else currNode , temp)
                self.table[key]=temp


    def getMaxKey(self) -> str:
        if len(self.table) == 0:
            return ""
        return  next(iter(self.tail.prev.val))

    def getMinKey(self) -> str:
        if len(self.table) == 0:
            return ""
      
        return next(iter(self.head.next.val))


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc("w1")
# obj.dec("w2")
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()
