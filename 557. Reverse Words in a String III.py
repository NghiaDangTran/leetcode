class Solution:
    def reverseWords(self, s: str) -> str:
        data=s.split()
        for i in range(len(data)):
            data[i]=data[i][::-1]
        return ' '.join(data)