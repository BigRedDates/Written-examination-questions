#给定两个数组，编写一个函数来计算它们的交集。
'''
示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
'''
#方法1，自己写的，执行速率很慢，思路：先将重复元素找出，存储，然后用set去重，
#最后找到set元素中在两个数组中的个数，取最小值，存储最小值数目的该元素
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        nums=[]
        for i in range(len(nums1)):
        	if nums1[i] in nums2:
        		nums.append(nums1[i])
        nums=set(nums)
        nums=list(nums)
        for i in range(len(nums)):
        	k=0
        	if nums1.count(nums[i])<nums2.count(nums[i]):
        		k=nums1.count(nums[i])
        	else:
        		k=nums2.count(nums[i])
        	nums+=[nums[i]]*(k-1)
        return nums
#方法二   先将两个数组排序，之后进行遍历，比较大小，数值较小的数组，序号自加1，若想等两个数组序号同时+1，


class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rt
        """
        nums1.sort()
        nums2.sort()
        nums=[]
        i=0
        j=0
        while i<len(nums1) and j<len(nums2):
        	if nums1[i]<nums2[j]:
        		i+=1
        	elif nums1[i]>nums2[j]:
        		j+=1
        	else:
        		nums.append(nums1[i])
        		i+=1
        		j+=1
        return nums
#方法3：最快  counter是计数函数 ，返回值
import collections
class Solution:
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        # nums1=[0,1,3,5,4,0]    print((collections.Counter(nums1)))   Counter({0: 2, 1: 1, 3: 1, 5: 1, 4: 1})
        #nums2=[0,0]  print((collections.Counter(nums2)))  Counter({0: 2})
        return list((collections.Counter(nums1)&collections.Counter(nums2)).elements())#   [0, 0]

