"""
9. Palindrome Number

Given an integer x, return true if x is a palindrome, and false otherwise.


Example 1:

    Input: x = 121
    Output: true
    Explanation: 121 reads as 121 from left to right and from right to left.

Constraints:

-231 <= x <= 231 - 1

"""

def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]

# or
def isPalindrome(x: int) -> bool:
    if x < 0: return False
    temp = x
    reverse_num = 0
    while temp != 0:
        reverse_num = (reverse_num * 10) + (temp % 10)
        temp //= 10
    return x == reverse_num