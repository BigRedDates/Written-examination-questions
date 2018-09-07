#给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素
#方法1：先排序 在对比前后三个元素，若前后三个元素不等，则中间的是只出现一次的
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        
        if len(nums)<2:
        	return nums[0]
        nums.sort()
        if nums[0]!=nums[1]:
        	return nums[0]
        if nums[n-1]!=nums[n-2]	:
        	return nums[n-1]
        for i in range(1,len(nums)-1):
        	if nums[i]!=nums[i+1] and nums[i]!=nums[i-1]:
        		return nums[i]



#方法2：set 无序且不重复的集合，利用set 去除重复，再乘二，和原来只差了一个不重复的数字，做差即可
class Solution:
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(list(set(nums)))*2 - sum(nums)
nums=[1,3,3,2,2,4,56,44,63,644]
