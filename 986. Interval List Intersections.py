class Solution:
    def intervalIntersection(self, data1: List[List[int]], data2: List[List[int]]) -> List[List[int]]:
        
#         dst=max(data1[-1][1],data1[-1][1])
#         data1d=[0]*(data1[-1][1]+1)
#         data2d=[0]*(data2[-1][1]+1)
#         result=[]
        
        
#         for i in data1:
#             for j in range(i[0],i[1]+1):
#                 data1d[j]=1
#         i=0 
#         j=0
#         for i in data2:
#             for j in range(i[0],i[1]+1):
#                 data2d[j]=1
#         # for i in range(dst+1):
#         #     if i>len(data1d) or i>len(data2d):
#         #         break
#         #     elif data1d[i] ==data2d[i]==1:
#         #         result.append([i])
                
#         i=0
#         while i<dst+1:
#             if i>len(data1d) or i>len(data2d):
#                 break
#             elif data1d[i] ==data2d[i]==1:
#                 start=i
#                 while i<dst+1:
#                     if i>len(data1d) or i>len(data2d):
#                         break
#                     if data1d[i] ==0 or data2d==0:
#                         result.append([start,i])
#                         break
                    
                            
#                     i+=1
#             i+=1'

        first=0
        second=0
        result=[]
        while first<len(data1) and second<len(data2):
            
            lower=max(data1[first][0],data2[second][0])
            
            upper=min(data1[first][1],data2[second][1])
            if lower<=upper:
                result.append([lower,upper])
            if data1[first][1]>data2[second][1]:
                second+=1
            else:
                first+=1
           
                
        
                
        return (result)
            
            