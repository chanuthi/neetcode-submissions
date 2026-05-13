class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        maxcnt = 0 
        for i in nums:
          if i == 1:
            count+=1
          else:
            count = 0
          
          if maxcnt < count:
            maxcnt = count
        
        return maxcnt