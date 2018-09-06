'''
给定一个整数数组，判断是否存在重复元素。

如果任何值在数组中出现至少两次，函数返回 true。如果数组中每个元素都不相同，则返回 false。
'''
#方法1，先排序，然后将排序后的数组，遍历前后两个进行比较
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n=len(nums)
        
        if len(nums)<2:
        	return False
        nums.sort()
        for i in range(len(nums)-1):
        	if nums[i]==nums[i+1]:
        		return True
        return False
#方法二 set集合具有去重功能，将列表转换成set比较长度即可
class Solution:
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==len(set(nums)):
            return False
        else:
            return True
        