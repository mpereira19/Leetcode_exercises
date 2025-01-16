"""
12. Integer to Roman

Seven different symbols represent Roman numerals with the following values:

Symbol	Value
I	1
V	5
X	10
L	50
C	100
D	500
M	1000

Roman numerals are formed by appending the conversions of decimal place values from highest to lowest. Converting a decimal place value into a Roman numeral has the following rules:

If the value does not start with 4 or 9, select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
If the value starts with 4 or 9 use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
Given an integer, convert it to a Roman numeral.


Example 1:

    Input: num = 3749
    Output: "MMMDCCXLIX"

Explanation:

3000 = MMM as 1000 (M) + 1000 (M) + 1000 (M)
 700 = DCC as 500 (D) + 100 (C) + 100 (C)
  40 = XL as 10 (X) less of 50 (L)
   9 = IX as 1 (I) less of 10 (X)
Note: 49 is not 1 (I) less of 50 (L) because the conversion is based on decimal places

Example 2:

    Input: num = 58
    Output: "LVIII"

Explanation:

50 = L
 8 = VIII

Example 3:

    Input: num = 1994
    Output: "MCMXCIV"

Explanation:

1000 = M
 900 = CM
  90 = XC
   4 = IV

Constraints:

1 <= num <= 3999

"""

def intToRoman(num: int) -> str:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    string = ""
    value = list(roman.values())
    while num != 0:
        if num >= 1000:
            string += list(roman.keys())[list(roman.values()).index(1000)]
            num -= 1000
        elif 900 <= num < 1000:
            string += list(roman.keys())[list(roman.values()).index(900)]
            num -= 900
        elif 500 <= num < 900:
            string += list(roman.keys())[list(roman.values()).index(500)]
            num -= 500
        elif 400 <= num < 500:
            string += list(roman.keys())[list(roman.values()).index(400)]
            num -= 400
        elif 100 <= num < 400:
            string += list(roman.keys())[list(roman.values()).index(100)]
            num -= 100
        elif 90 <= num < 100:
            string += list(roman.keys())[list(roman.values()).index(90)]
            num -= 90
        elif 50 <= num < 90:
            string += list(roman.keys())[list(roman.values()).index(50)]
            num -= 50
        elif 40 <= num < 50:
            string += list(roman.keys())[list(roman.values()).index(40)]
            num -= 40
        elif 10 <= num < 40:
            string += list(roman.keys())[list(roman.values()).index(10)]
            num -= 10
        elif 9 <= num < 10:
            string += list(roman.keys())[list(roman.values()).index(9)]
            num -= 9
        elif 5 <= num < 9:
            string += list(roman.keys())[list(roman.values()).index(5)]
            num -= 5
        elif 4 <= num < 9:
            string += list(roman.keys())[list(roman.values()).index(4)]
            num -= 4
        else:
            string += list(roman.keys())[list(roman.values()).index(1)]
            num -= 1
    return string

#or

def intToRoman(num: int) -> str:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    string = ""
    value = list(roman.values())
    value.sort()
    while num != 0:
        if num < value[-1]:
            value = value[:-1]
        else:
            string += list(roman.keys())[list(roman.values()).index(value[-1])]
            num -= value[-1]
    return string

# or

def intToRoman(num: int) -> str:
    roman = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000, "IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
    string = ""
    value = sorted(roman.values())
    i = -1
    while num != 0:
        if num < value[i]: i -= 1
        else:
            string += list(roman.keys())[list(roman.values()).index(value[i])]
            num -= value[i]
    return string