class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        result=[]
        lengthdata=lambda a:0 if(a==0) else a-1


        for i in s:
            if i=='(' or  i=='{' or i=='[':
                result.append(i)
            if (len(result))==0 and ( i==')' or  i==']' or  i=='}'):
                return False

            if i==')':
                if result[lengthdata(len(result))]=="(":
                    result.pop()
                else: return False
            elif i=='}':
                if result[lengthdata(len(result))]=="{":
                    result.pop()
                else: return False
            elif i==']':
                if result[lengthdata(len(result))]=="[":
                    result.pop()
                else: return False

    
        return len(result)==0 