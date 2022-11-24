class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # creat dic to store num and count
        num_count = dict()
        for num in nums:
            if num not in num_count:
                num_count[num] = 1
            else:
                num_count[num] += 1
        for num  in num_count:
            if (num_count[num] == 1):
                return num


# NEED TO USE ^ operator (Xor)