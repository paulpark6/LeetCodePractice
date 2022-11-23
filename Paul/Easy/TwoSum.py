class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # target = num1 + num2
        # find = target - num1
        # create dictionary of adding all number in dictionary with its position
        # find find in dictionary and return the position with current position
        pairs = dict()
        l = len(nums)
        for i in range(l):
            find = target - nums[i]
            if (nums[i] not in pairs):
                pairs[nums[i]] = i
            if find in pairs and pairs[find] != i:
                return [pairs[find], i]