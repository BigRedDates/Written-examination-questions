#给定一个由整数组成的非空数组所表示的非负整数，在该数的基础上加一。

#方法一： 自己的，从尾部统计9的个数，分为9个数为0,9个数为len(digits),和其它三种情况
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        k=0
        for i in range(len(digits)-1,-1,-1):
        	if digits[i]!=9:
        		break
        	else:
        		k+=1
        if k==0:
        	digits[-1]=digits[-1]+1
        elif k==len(digits):
        	digits=[1]+[0]*k
        else :
        	digits[-k-1]+=1
        	digits=digits[:-k]+[0]*k

        	

        return digits
nums=[9]
print(Solution().plusOne(nums))

#方法2：最快 没有9 不会进位 直接+1   最后一位为9，取出数组中整数+1 在转换为数组
class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """ 
        result=[]
        if digits[-1]!=9:
            digits[-1]=digits[-1]+1
            result=digits
        else:
            num=0
            digits.reverse()
            for i in range(len(digits)):
                num=num+digits[i]*(10**(i))
            num=str(num+1)# 存为字符串
            for j in num:
                result.append(int(j))
        return result