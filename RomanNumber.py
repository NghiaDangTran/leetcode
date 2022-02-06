def romanToInt(self, s):
    """
    :type s: str
    :rtype: int
    """
    data={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
    result=0
    
    
    i=0
    while i <(len(s)-1):
        if data[s[i]]==1 and  (data[s[i+1]]==5 or data[s[i+1]]==10):
            result+=(data[s[i+1]]-data[s[i]])
            i+=2
        elif data[s[i]]==10 and  (data[s[i+1]]==50 or data[s[i+1]]==100):
            result+=(data[s[i+1]]-data[s[i]])
            i+=2
        elif data[s[i]]==100 and  (data[s[i+1]]==500 or data[s[i+1]]==1000):
           result+=(data[s[i+1]]-data[s[i]])
           i+=2
        else:
            result+=data[s[i]]
            i+=1
        
       
    
    
  
    return  result+data[s[i]]
print(romanToInt(1,"MCMX"))