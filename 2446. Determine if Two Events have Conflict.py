'''
2446. Determine if Two Events Have Conflict

You are given two arrays of strings that represent two inclusive events that happened on the same day, event1 and event2, where:

    event1 = [startTime1, endTime1] and
    event2 = [startTime2, endTime2].

Event times are valid 24 hours format in the form of HH:MM.

A conflict happens when two events have some non-empty intersection (i.e., some moment is common to both events).

Return true if there is a conflict between two events. Otherwise, return false.

Example 1:

    Input: event1 = ["01:15","02:00"], event2 = ["02:00","03:00"]
    Output: true
    Explanation: The two events intersect at time 2:00.

Constraints:

    event1.length == event2.length == 2
    event1[i].length == event2[i].length == 5
    startTime1 <= endTime1
    startTime2 <= endTime2

All the event times follow the HH:MM format.

'''

def haveConflict(event1: list[str], event2: list[str]) -> bool:
    ev1 = [float(x.replace(":", ".")) for x in event1]
    ev2 = [float(x.replace(":", ".")) for x in event2]
    if ev1[0] <= ev2[0] <= ev1[1] or ev2[0] <= ev1[0] <= ev2[1]: return True
    return False

# or
    
def haveConflict(event1: list[str], event2: list[str]) -> bool:
    ev1 = [float(x.replace(":", ".")) for x in event1]
    ev2 = [float(x.replace(":", ".")) for x in event2]
    if ev1[0] <= ev2[0] <= ev1[1]: return True
    elif ev2[0] <= ev1[0] <= ev2[1]: return True
    return False