class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # find = target - num
        # use dictionary to store number and its position
        # if find is found -> return number and its position form dictionary
        d = dict()
        n = len(nums)
        for i in range(n):
            num = nums[i]
            find = target - num
            if num not in d:
                d[num] = i
            if find in d and d[find] != i:
                return [i,d[find]]
                