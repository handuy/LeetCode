Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Way 3-->Using HashMap -->O(n)
keep on storing the elements that we reach , also keep on check if target-element is already present in the hashmap or not , if it is , then we found a pair