

from dataclasses import asdict


class Solution:
    def maxSlidingWindow(self, nums, k: int) :
        def findmax(a,b):
            stop=min(b,len(nums)-1)
            curr=nums[a]
            pos=a
            for i in range(a,stop+1):
                if nums[i]>nums[a]:
                    curr=nums[i]
                    pos=i
            return [curr,pos]
        check=   findmax(0,0+k-1)     
        currmax,pos,at=check[0],check[1],k-1
        res=[]
        while at<len(nums)-1:
            print(currmax,pos,at)
            if pos%k==0:
                check=   findmax(pos,pos+k-1) 
                currmax,pos,at=check[0],check[1],at+1
                res.append(currmax)
            else:
                atmove=0
                print(at+pos%k)
                for i in range(at,at+pos%k):
                    if currmax>=nums[i]:
                        res.append(currmax)
                        pos+=1
                        at+=1
                    else:
                        currmax=nums[i]
                        pos=i
                        at+=1
                        res.append(currmax)
                        break
                
            print(currmax,pos,at)
            
        
        
        return res
# techinically we can do it but problem arise when array isd in decreasing shortcuts
# print(Solution.maxSlidingWindow(1,[1,3,-1,-3,5,3,6,7],2))
# print(Solution.maxSlidingWindow(1,[1,5,7,9,10,10,0],2))
            
class Solution:
    def maxSlidingWindow(self, nums, k: int) :
        res=[]
        stack=[]
        for i in range(len(nums)):
            while stack and nums[i]>=nums[stack[-1]]:
                stack.pop(-1)
                
            stack.append(i)
            if   stack[-1]-stack[0]==k:
                stack.pop(0)           

            if i>=k-1 :
                # print(stack[0]>len(nums))
                res.append(nums[stack[0]])
        return res

print(Solution.maxSlidingWindow(1,[1,3,-1,-3,5,3,6,7],3))
# print(Solution.maxSlidingWindow(1,[1,5,7,9,10,10,0],3))
print(Solution.maxSlidingWindow(1,[7,2,4],2))
print(Solution.maxSlidingWindow(1,[1,3,1,2,0,5],3))
# print(Solution.maxSlidingWindow(1,[1,3,1,2,0,5],3))
            
