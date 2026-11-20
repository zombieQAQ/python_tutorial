class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:

        count = 0
        for j in range(len(nums)-1):
            count_temp = 1
            for i in range(len(nums)-j-1):
                if nums[i+j+1] > nums[j+i]:
                    temp = nums[i+j]
                    count_temp += 1
                else:
                    break
            if count_temp > count:
                count = count_temp
        if len(nums) == 1:
            count = 1
        return count


class Solution:
    def findLengthOfLCIS(self, nums: list[int]) -> int:

        ans = 1

        length = 1

        for i in range(1,len(nums)):
            if nums[i]>nums[i-1]:
                length+=1
            else:
                length=1
            ans = max(ans,length)
        return ans




