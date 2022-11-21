class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        sums = dict()
        max = len(nums)/2
        for num in nums:
            if num not in sums:
                sums[num] = 1
            else:
                sums[num] += 1
            if sums[num] > max:
                return num
        