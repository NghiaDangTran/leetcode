class Solution(object):

    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result = []
        currArr = []
        curr = 1
        while curr <= numRows:
            currArr = [1] * curr
            print(result)
            if curr >= 3:
               
                for i in range(1,len(currArr) - 1):
                    print(i)
                    currArr[i] = result[curr - 2][i - 1] + result[curr - 2][i]

            result.append(currArr)
            curr += 1
        return result


