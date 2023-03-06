#  innitial work
class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
       
        res=[]
        for i in range(len(t)-1, -1, -1):
            curr=0
            for j in range(i+1,len(t)):
                curr+=1
                if t[j]>t[i]:
                    res.insert(0,curr)
                    break
            else:res.insert(0,0)

        return res
class Solution:
    def dailyTemperatures(self, t: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(t)
        for i in range(len(t)-1,-1,-1):
            while stack and stack[-1][1]<=t[i]:
                res+=1
                stack.pop()
            if stack:
                res+=1
                # res[i]=stack[-1][0]-i
            
            
            stack.append((i,t[i]))
            
            
        return res
                        
                        
                

                
            
                
                
                

            
            