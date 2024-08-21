class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0
        
        i = 0  # Initialize the pointer for the place of the next unique element
        
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:  
                i += 1
                nums[i] = nums[j]  
        
        # Now nums[:i+1] contains the unique elements, and i+1 is the number of unique elements
        return i + 1

solution = Solution()
nums = [1, 1, 2]
k = solution.removeDuplicates(nums)


for idx in range(k, len(nums)):
    nums[idx] = '_'

print(k)        
print(nums)     
