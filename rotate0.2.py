#题目：给定一个数组，将数组中的元素向右移动 k 个位置，其中 k 是非负数。

#方法一：翻折数组先翻折后k个，再翻折前n-k个，最后全部翻折
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        n=len(nums)
        k=k%n
        for i in range(int((n-k)/2)):
            nums[i],nums[n-k-1-i]=nums[n-k-1-i],nums[i]
        print(nums)
        for i in range(n-k,n-k+int(k/2)):
            nums[i],nums[n-1-i+n-k]=nums[n-1-i+n-k],nums[i]
        print(nums)
        for i in range(int(n/2)):
            nums[i],nums[n-1-i]=nums[n-1-i],nums[i]
        	
#方法二：移动后 倒数第k个必然变为第一个，第一个变为第k个，所以取后k个，再取前n-k个，后变前前变后，拼接即可      
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        length = len(nums)
        i = k % length
        nums[:] = nums[-i:]+nums[:-i]
        nums[i]
nums=[1,2,3]
k=2
#Solution().rotate(nums,k)
#print(nums)
print(nums)
print(nums[-2:])
print(nums[:-2])

