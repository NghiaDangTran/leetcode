class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        n=len(arr)
        # if n%2==1:
        #     arr.append(1)
        result=0
        while(n>1):
            currMin=arr.index(min(arr))
            
            if 0<currMin<len(arr)-1:
                result+=arr[currMin]*min(arr[currMin+1],arr[currMin-1])
                arr=arr[:currMin]+arr[currMin+1:]
            else:
                result+=arr[currMin]*(arr[currMin+1] if currMin==0 else arr[currMin-1] )
                arr=arr[:currMin]+arr[currMin+1:]
                
                
            
            n=len(arr)
            
        return result
            

            
            
       
            
            
            
        
        
        
        return arr[0]
            