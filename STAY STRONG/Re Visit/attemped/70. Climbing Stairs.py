# class Solution:
#     def climbStairs(self, n: int) -> int:

#         if n == 1:
#             return 1
#         if n == 2:
#             return 2
#         return self.climbStairs(n-1)+self.climbStairs(n-2)
class Solution:
    def climbStairs(self, n: int) -> int:

        a=b=1
        for i in range(n):
            a,b=b,a+b
        return a
