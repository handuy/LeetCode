# Sort list 

count = 0

def quickSort(arr):
    global count
    count += 1

    less = []
    pivotList = []
    more = []
    if len(arr) <= 1:
        print("count:", count, "arr:", arr)
        return arr
    else:
        pivot = arr[0]
        for i in arr:
            if i < pivot:
                less.append(i)
            elif i > pivot:
                more.append(i)
            else:
                pivotList.append(i)
        
        print("count:", count, "pivotList:", pivotList)
        print("count:", count, "less:", less)
        print("count:", count, "more:", more)

        less = quickSort(less)  
        more = quickSort(more)
        
        return less + pivotList + more

a = [4, 65, 2, -31, 0, 99, 83, 782, 1]
a = quickSort(a)

print("final", a)

# For each item k in sorted list, find: target - k

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         return []