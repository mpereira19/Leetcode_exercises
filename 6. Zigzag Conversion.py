""" 
6. Zigzag Conversion

The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)

    P   A   H   
    A P L S I I G
    Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:

    Input: s = "PAYPALISHIRING", numRows = 3
    Output: "PAHNAPLSIIGYIR"

Example 2:

    Input: s = "PAYPALISHIRING", numRows = 4
    Output: "PINALSIGYAHRPI"
    Explanation:

    P     I    N
    A   L S  I G
    Y A   H R
    P     I

Example 3:

    Input: s = "A", numRows = 1
    Output: "A"

Constraints:

1 <= s.length <= 1000
s consists of English letters (lower-case and upper-case), ',' and '.'.
1 <= numRows <= 1000

"""

def convert(s: str, numRows: int) -> str:
    if numRows == 1: return s
    new_s = s[:numRows]
    add = 0 # 0: True, 1: False
    x = numRows-2
    y = 1
    for i in range(len(new_s), len(s)):
        if add == 0 and x != -1:
            new_s += (numRows-2)*" " + s[i]
            x -= 1
        elif x == -1:
            x = numRows-2
            add = 1
            new_s += s[i]
        elif add == 1 and y != numRows-2:
            y += 1
            new_s += s[i]
        elif y == numRows-2:
            y = 1
            add = 0
            new_s += s[i]
    lst = [[] for i in range(numRows)]
    for col in range(numRows):
        for i in range(0, len(new_s), numRows):
            try: lst[col].append(new_s[i+col])
            except: pass
    res = ""
    for z in range(len(lst)):
        for u in range(len(lst[z])):
            if lst[z][u] != "*": res += lst[z][u]        
    return res
