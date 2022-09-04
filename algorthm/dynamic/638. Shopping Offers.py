

from random import randint


class Solution:
    def shoppingOffers(self, price, special, needs) -> int:
        def sortSpcial(special):
            res = {}
            temp = []
            for i in range(len(special)):
                curr = tuple(special[i][0:-1])
                if curr in res.keys():
                    if res[curr] > special[i][-1]:
                        res[curr] = special[i][-1]
                else:
                    res[curr] = special[i][-1]
            for i in res.keys():
                temp.append(list(i)+[res[i]])

            return temp
        curr = {}

        def rec(price, special, need, currPrice):
            if price == [0]*(len(need)):
                return 0
            if tuple(need) in curr.keys():
                return curr[tuple(need)]

            res = currPrice
            for i in range(len(need)):
                res += price[i]*need[i]
            for i in range(len(special)):
                temp = []
                for j in range(len(need)):
                    if need[j]-special[i][j] < 0:

                        break
                    temp.append(need[j]-special[i][j])

                else:

                    res = min(res, rec(price, special, temp,
                              currPrice+special[i][-1]))
            
            curr[tuple(need)] = currPrice

            
            return res
        return rec(price, sortSpcial(special), needs, 0)


print(Solution.shoppingOffers(1, [9],
[[1, 10], [2, 2]],
[3]))


[9],
[[1, 10], [2, 2]],
[3]
