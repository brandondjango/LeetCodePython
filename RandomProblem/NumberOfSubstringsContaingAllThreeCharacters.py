#1358. Number of Substrings Containing All Three Characters
#Medium
#Topics
#Companies
#Hint
#Given a string s consisting only of characters a, b and c.
#
#Return the number of substrings containing at least one occurrence of all these characters a, b and c.
#
#
#
#Example 1:
#
#Input: s = "abcabc"
#Output: 10
#Explanation: The substrings containing at least one occurrence of the characters a, b and c are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again).
#Example 2:
#
#Input: s = "aaacb"
#Output: 3
#Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb".
#Example 3:
#
#Input: s = "abc"
#Output: 1
#
#Constraints:
#
#3 <= s.length <= 5 x 10^4
#s only consists of a, b or c characters.
from operator import contains


def return_number_of_substrings(s: str):
    i = 0
    j = 0
    lowest_hash = {}
    lowest_hash["a"] = None
    lowest_hash["b"] = None
    lowest_hash["c"] = None
    count = 0
    while(j < len(s)):
        lowest_hash[s[i]] = i
        window = s[j:i]
        print(j)
        print(i)
        print(window)

        all_vals_in_bool = False
        if None not in lowest_hash.values():
            for value in lowest_hash.values():
                if value < i and value >= j:
                    all_vals_in_bool = True

        if all_vals_in_bool:
            right_window_mark = max(lowest_hash.values())
            left_window_mark = min(lowest_hash.values())
            count += len(s) - (right_window_mark)
            print("Count: " + str(count))
            j = left_window_mark + 1

        i+=1

        if i >= len(s):
            return count

s = "abcabbba"
print(return_number_of_substrings(s))
