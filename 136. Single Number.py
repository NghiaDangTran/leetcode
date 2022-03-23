class Solution:

    def singleNumber(self, nums) -> int:
        #         for i in range(len(nums)):
        #             count=0
        #             for j in range(len(nums)):

        #                 if j!=i and nums[i]==nums[j]:
        #                     break
        #             else: count=1
        #             if count==1:
        #                 return nums[i]
        #           time limit exedd cant use bruto force
        # nums.sort()
        # check = dict()
        # for i in range(len(nums)):
        #     if check.get(nums[i]) == None:
        #         check[nums[i]] = 1
        #     else:
        #         check[nums[i]] += 1

        # print(check)
        # for key,value in (check.items()):
        #     if value==1:
        #         return key
        #         if len(nums)==1:
        #     return nums[0]
        #

        #  mathematic way to solve from https://leetcode.com/problems/single-number/discuss/1857685/Python-Easy-Mathematical-Solution-oror-Time%3A-O(n)-Space%3A-O(1)



        copy = set(nums)
        #  this will copy into new array but no duplicate value available
        sum1 = sum(nums)
        #  get the sum of all number
        # so the ideal is the max occourance is 2
        #  so if mutiple 2 by all the unique number we will get the max total posssibel sum
        sum2 = 2 * sum(copy)
        #  and suppose theier only one number has 1 occourance then sum2-sum1 will get the number we want
        return (sum2 - sum1)


print(Solution.singleNumber(1, [2, 2, 1]))
