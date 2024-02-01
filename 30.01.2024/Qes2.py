 Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

Example 1:

Input: nums = [1,2,3,1]
Output: true
Example 2:

Input: nums = [1,2,3,4]
Output: false
Example 3:

Input: nums = [1,1,1,3,3,4,3,2,4,2]
Output: true
 

Constraints:

1 <= nums.length <= 105
-109 <= nums[i] <= 109
Seen this question in a real interview before?  YesNo
Subscribe to see which companies asked this question.

Related Topics 
ArrayHash TableSorting
Similar Questions 
Contains Duplicate IIContains Duplicate IIIMake Array Zero by Subtracting Equal Amounts
Py3	



1
class Solution(object):
2
    def containsDuplicate(self, nums):
3
        """
4
        :type nums: List[int]
5
        :rtype: bool
6
        """
7
        hash = set()
8
        for n in nums:
9
            if n in hash:
10
                return True
11
            hash.add(n)
12
        return False
