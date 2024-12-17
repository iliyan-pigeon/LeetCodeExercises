class Solution(object):
    def removeDuplicates(self, nums):

        while True:
            control = []

            for i in nums:
                if i in control:
                    nums.remove(i)
                    break
                else:
                    control.append(i)

            if len(control) == len(nums):
                break

        return len(nums)        
                
