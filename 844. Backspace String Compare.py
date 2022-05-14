class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        
        
        def rotae(data):
            
            while "#" in data:
                at=data.find("#")
                if at==0:
                    data=data[at+1:]
                else:
                    data = data[:at-1]+data[at+1:]
            return data
                    
                
        
        return (rotae((s))==rotae((t)))