class RandomizedSet:
    import random
    def __init__(self):
        self.table={}
        
        

    def insert(self, val: int) -> bool:
        if val in self.table:
            return False
        
        else:
            self.table[val]=1
            return True
        

    def remove(self, val: int) -> bool:
        if val in self.table:
            del self.table[val]
            return True
        
        else:
            
            return False
        

    def getRandom(self) -> int:
        temp=list(self.table.keys())
        
        
        return temp[random.randint(0,len(temp)-1)]
        
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()