""" 13. Roman to Integer

Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.


Example 1:

    Input: s = "III"
    Output: 3
    Explanation: III = 3.

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999]. 

"""

def romanToInt(s: str) -> int:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900, "P": 0}
    value = []
    for i in ["IV", "IX", "XL", "XC", "CD", "CM"]:
        if i in s:
            value.append(roman[i])
            s = s.replace(i, "")
    return sum(value + [roman[i] for i in s])

# or

def romanToInt(s: str) -> int:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900, "P": 0}
    value = []
    lst = list(s)
    for i in range(len(lst)):
        if lst[i] == "I" or lst[i] == "X" or lst[i] == "C":
            try:
                value.append(roman[lst[i]+lst[i+1]])
                lst[i+1] = "P"
            except:
                value.append(roman[lst[i]])
        else: value.append(roman[lst[i]])
    return sum(value)