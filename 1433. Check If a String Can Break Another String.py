class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:

        data = list((s1))
        data1 = list((s2))
        data.sort()
        data1.sort()
        result = []
        result2 = []
        for i in range(len(data)):
            if ord(data[i]) > ord(data1[i]):
                result.append(data[i])
            elif ord(data[i]) == ord(data1[i]):
                result.append(data[i])
                result2.append(data1[i])
            else:
                result2.append(data1[i])

        if(len(result) == len(s1) or len(result2) == len(s1)):
            return True
        return False
