"""
You are given a string s of lowercase English letters and a 2D integer array shifts where shifts[i] = [starti, endi, directioni]. For every i, shift the characters in s from the index starti to the index endi (inclusive) forward if directioni = 1, or shift the characters backward if directioni = 0.

Shifting a character forward means replacing it with the next letter in the alphabet (wrapping around so that 'z' becomes 'a'). Similarly, shifting a character backward means replacing it with the previous letter in the alphabet (wrapping around so that 'a' becomes 'z').

Return the final string after all such shifts to s are applied.


Input: s = "abc", shifts = [[0,1,0],[1,2,1],[0,2,1]]
Output: "ace"
Explanation: Firstly, shift the characters from index 0 to index 1 backward. Now s = "zac".
Secondly, shift the characters from index 1 to index 2 forward. Now s = "zbd".
Finally, shift the characters from index 0 to index 2 forward. Now s = "ace".

"""
class Solution:
    def shiftingLetters(self, s: str, shifts: list[list[int]]) -> str:
        n = len(s)
        combined = [0] * (n+1)
        
        for l,r,d in shifts:
            d = 2*d -1
            combined[l] += d
            combined[r+1] -= d

        ans =[]
        curr = 0
        for i in range(n):
            curr += combined[i]
            ans.append((ord(s[i]) - ord('a') + curr)% 26)
        return ''.join(chr(l  + ord('a')) for l in ans)
    
sol = Solution()
s = "abc"
shifts = [[0,1,0],[1,2,1],[0,2,1]]
print(sol.shiftingLetters(s, shifts))