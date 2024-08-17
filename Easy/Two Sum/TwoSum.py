from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
       
       resultDict={}

       for index ,value in enumerate(nums):
            
            findValue=target-value


            if findValue in resultDict:
                print(resultDict[findValue],index)
                print(resultDict[findValue])

                store=[resultDict[findValue],index]
                return store
            else:

                resultDict[value]= index




           
              

