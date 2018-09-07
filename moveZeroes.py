#给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序
#方法一：268ms时间太长
class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for i in range(len(nums)):
        	if nums[i]==0:
        		nums.remove(0)
        		nums+=[0]
#方法二  在于用i<j,j等于列表倒序遍历，第一个不为零的值的索引值
class Solution:
    def moveZeroes(self, digits):
    	i=0
    	j=len(digits)
    	while i<j:
    		if digits[i]==0:
    			digits.pop(i)
    			digits.append(0)
    			j-=1
    		
    		else:
    			i+=1

    	print(digits)
