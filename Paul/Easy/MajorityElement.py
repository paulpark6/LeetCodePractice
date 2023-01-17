class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # maj = n/2 times
        # create dictionary to store num and it's count
        c = dict()
        n = len(nums)
        maj = n/2
        for num in nums:
            if num not in c:
                c[num] = 1
            else:
                c[num] += 1
            if c[num] > maj:
                return num