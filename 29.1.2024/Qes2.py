 Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
Seen this question in a real interview before?  YesNo
Subscribe to see which companies asked this question.

Related Topics 
Math
Similar Questions 
Palindrome Linked ListFind Palindro…
[10:25 PM, 1/31/2024] Indhu: NumberCount Symmetric Integers
Py3	



1
class Solution:
2
    def isPalindrome(self, x: int) -> bool:
3
        if x< 0:
4
            return False
5
        div =1 
6
        while x>= div*10:
7
            div = div*10
8
        while x:
9
            right = x%10
10
            left = x // div
11
            if left!=right:
12
                return False
13
            x = (x % div)//10
14
            div =  div/100 
15
        return True






