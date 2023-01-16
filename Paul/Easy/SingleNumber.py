class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # dict to add num and their count
        # loop through dict to check for one
        d =dict()
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num] += 1
        for (key,val) in d.items():
            if val == 1:
                return key


# NEED TO USE ^ operator (Xor)
# https://www.youtube.com/watch?v=5rzjWwHFrDo&ab_channel=PersistentProgrammer