
class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if len(nums)==1:
            return True
        temp=0
        end=0
        while(temp<2):
            for i in range(len(nums)):
                if i+1<len(nums) and nums[i]>nums[i+1]:
                    nums.pop(i)
                    temp+=1
                    for j in range(len(nums)):
                        if j+1<len(nums) and nums[j]>nums[j+1]:
                            temp+=1
                            break
                if temp>1:
                    break
            break
        return True if temp<=1 else False

if __name__=='__main__':
    nums=[2,3,3,2,4]
    print(Solution().checkPossibility(nums))