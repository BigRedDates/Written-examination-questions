class Solution:
	def removeDuplicates(self, nums):
		
		if len(nums)<2:
			return len(nums)
		index = 1
		pre=nums[0]
		for i in range(len(nums)):
			if pre!=nums[i]:
				pre=nums[i]
				nums[index]=pre
				index+=1
		return index
					

		
nums=[0]
print(Solution().removeDuplicates(nums))