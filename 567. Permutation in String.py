

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        count1 ={}
        count2 = {}
        #  learn here diction can be use in many thing
        # leason 2: counter is way better than nortmla dic

        for i in s1:
            count1[i] = count1.get(i, 0)+1
        
        for i, char in enumerate(s2):
            count2[char] = count2.get(char, 0)+1
            if i > len(s1)-1:
                chartoGet = s2[i-len(s1)]
                count2[chartoGet] = count2.get(chartoGet, 0)-1
                print(chartoGet)
                if count2[chartoGet] == 0:
                    count2.pop(chartoGet)
                    # count2[chartoGet] = 0
            print(count2)
            if len(count2)>=len(count1):
                for j in count2:
                    if count2[j] != count1.get(j, -1):
                        break
                else:
                    return True

        return False


print(Solution.checkInclusion(1, s1="hello", s2="ooolleoooleh"))
"hello"
"ooolleoooleh"