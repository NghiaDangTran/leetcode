class Solution:
    def minimumSum(self, num: int) -> int:
        data = [(x) for x in str(num)]
        data.sort()
        return int(data[0]+data[2])+int(data[1]+data[3])                