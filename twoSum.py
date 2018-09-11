#给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。

#你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
            	if nums[i]+nums[j]==target:
            		return [i,j]
nums=[3,2,4]
target=6
print(Solution().twoSum(nums,target))

#方法2，最快，使用字典以及for in dic 查找键
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for i, num in enumerate(nums):
            if (target - num) in dic:#字典键查找，找待查元素在字典中是否存在键与之相等，将元素存为键，将索引存为值
                return i,dic[target - num]
            dic[num] = i

