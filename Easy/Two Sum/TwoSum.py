from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        primaryCounter=0
        secondryCounter=1
        print(len(nums))
        while primaryCounter<len(nums):
            contemp=target-nums[primaryCounter]
            print("co",contemp)
            if contemp in nums:
                
                break
            else:
                print("not present")
                primaryCounter=primaryCounter+1
           
        return None        


        

# Create an instance of the Solution class
solution_instance = Solution()

# Call the twoSum method with the required arguments
nums = [2, 7, 11, 15]
target = 9
result = solution_instance.twoSum(nums, target)

# Output the result
print(result)