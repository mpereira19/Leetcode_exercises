'''
506. Relative Ranks

You are given an integer array score of size n, where score[i] is the score of the ith athlete in a competition. All the scores are guaranteed to be unique.

The athletes are placed based on their scores, where the 1st place athlete has the highest score, the 2nd place athlete has the 2nd highest score, and so on. The placement of each athlete determines their rank:

    The 1st place athlete's rank is "Gold Medal".
    The 2nd place athlete's rank is "Silver Medal".
    The 3rd place athlete's rank is "Bronze Medal".
    For the 4th place to the nth place athlete, their rank is their placement number (i.e., the xth place athlete's rank is "x").

Return an array answer of size n where answer[i] is the rank of the ith athlete.


Example 1:

    Input: score = [5,4,3,2,1]
    Output: ["Gold Medal","Silver Medal","Bronze Medal","4","5"]
    Explanation: The placements are [1st, 2nd, 3rd, 4th, 5th].

Constraints:

n == score.length
1 <= n <= 104
0 <= score[i] <= 106
All the values in score are unique.
'''

def findRelativeRanks(score: list[int]) -> list[str]:
    podium = {"1": "Gold Medal", "2": "Silver Medal", "3": "Bronze Medal"}
    placard = {str(j): podium[str(i+1)] if str(i+1) in podium.keys() else str(i+1) for i, j in enumerate(sorted(score, reverse=True))}
    return [placard[str(x)] for x in score]