# a = [7,11,15,2]
# target = 9

# newDict = {}


# for index, val in enumerate(a):
#     if newDict.get(target - val) == None:
#         newDict[val] = index
#     else:
#         print(index, val, newDict)
#         print( index, newDict[target - val] )
#         break

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        newDict = {}
        for index, val in enumerate(nums):
            if newDict.get(target - val) == None:
                newDict[val] = index
            else:
                return [ index, newDict[target - val] ]