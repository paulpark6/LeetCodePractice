class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # dictionary that stores numbers as keys and position as values
        store = dict()
        # loop 
        n = len(nums)
        for i in range(n):
            num = nums[i]
            # find = target - num
            find = target - num
            # if num not in dictionary add it
            if num not in store:
                store[num] = i
            # if find in dictionary and different position return
            if find in store and store[find] != i:
                return [store[find], i]
