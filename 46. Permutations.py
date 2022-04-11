class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def try1(a, l, r):
            if l == r:
                print(a)
                result.append(a.copy())
            else:
                for i in range(l, r):
                    a[l], a[i] = a[i], a[l]

                    try1(nums, l+1, r)
                    a[l], a[i] = a[i], a[l]

        try1(nums, 0, len(nums))
        return result
