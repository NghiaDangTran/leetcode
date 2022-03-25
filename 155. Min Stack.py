from typing_extensions import Self


class MinStack:

    def __init__(self):
        self.data = []
        self.min = 0

    def push(self, val: int) -> None:
        # low=0
        # high=len(self.data)

        # while (low<high):
        #     mid=(low+high)//2
        #     if self.data[mid]<val:
        #         low=mid+1
        #     else:
        #         high=mid

        # self.data.insert(low,val)

        self.data.append(val)
        if len(self.data) == 1:
            self.min = val
        elif val < self.min:
            self.min = val

    def pop(self) -> None:
        if len(self.data)!=0:

            self.data.pop(len(self.data) - 1)
            self.min=self.data[0]
            for i in self.data:
                self.min=min(self.min,i)

    def top(self) -> int:
        if len(self.data)!=0:
        
             return self.data[len(self.data)-1]

    def getMin(self) -> int:
        return self.min
    def print(self):
        print(self.data)


# Your MinStack object will be instantiated and called as such:
# class MinStack:

#     def __init__(self):
#         self.stack = []
        
#     def push(self, val: int) -> None:
#         if self.stack:
#             self.stack.append((val, min(val, self.stack[-1][1])))
#         else:
#             self.stack.append((val, val))

            
#     def pop(self) -> None:
#         if self.stack:
#             self.stack.pop()
            

#     def top(self) -> int:
#         if self.stack:
#             return self.stack[-1][0]
        

#     def getMin(self) -> int:
#         if self.stack:
#             return self.stack[-1][1]
        