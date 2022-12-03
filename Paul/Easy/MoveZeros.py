class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        tmp = list()
        c = 0 # count zeros
        for num in nums:
            if num != 0:
                tmp.append(num)
            else:
                c += 1
        for i in range(len(tmp)):
            nums[i] = tmp[i]
        for i in range(c):
            nums[-1 * (i + 1)] = 0
        
                
        