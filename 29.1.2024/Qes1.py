Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
Seen this question in a real interview before?  YesNo
Subscribe to see which companies asked this question.

Related Topics 
ArrayHash Table
Similar Questions 
3Sum4SumTwo Sum II - Input Array Is SortedTwo Sum III - Data structure designSubarray Sum Equals KTwo Sum IV - Input is a BSTTwo Sum Less Than KMax Number of K-Sum PairsCount Good MealsCount Number of Pairs With Absolute Difference KNumber of Pairs of Strings With Concatenation Equal to TargetFind All K-Distant Indices in an ArrayFirst Letter to Appear TwiceNumber of Excellent PairsNumber of Arithmetic TripletsNode With Highest Edge ScoreCheck Distances Between Same LettersFind Subarrays With Equal SumLargest Positive Integer That Exists With Its NegativeNumber of Distinct AveragesCount Pairs Whose Sum is Less than Target
Py3	



1
class Solution(object):
2
    def twoSum(self, nums, target):
3
     
4
        num_dict = {}  
5
​
6
        for i, num in enumerate(nums):
7
            complement = target - num
8
​
9
            if complement in num_dict:
              
10           return [num_dict[complement], i]
11
​
12
            num_dict[num] = i
13
​
14
        return []
