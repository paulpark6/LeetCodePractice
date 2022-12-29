class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # dictionary with number as keys and count as values
        counts = dict()
        # loop through nums
        for num in nums:
            if num not in counts:
                counts[num] = 1
            else:
                counts[num] += 1
        for num in counts:
            if counts[num] == 1:
                return num

# NEED TO USE ^ operator (Xor)