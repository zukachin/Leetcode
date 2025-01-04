"""
Given a string s, return the number of unique palindromes of length three that are a subsequence of s.

Note that even if there are multiple ways to obtain the same subsequence, it is still only counted once.

A palindrome is a string that reads the same forwards and backwards.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
 
Input: s = "aabca"
Output: 3
Explanation: The 3 palindromic subsequences of length 3 are:
- "aba" (subsequence of "aabca")
- "aaa" (subsequence of "aabca")
- "aca" (subsequence of "aabca")

"""
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        l=set(s)
        cnt=0
        for x in l :
            left,right=s.index(x),s.rindex(x)
            b=set()
            if left!=right : 
                b=set(s[left+1:right])
            cnt+=len(b)
        return cnt

sol = Solution()
s = "aabca"
print(sol.countPalindromicSubsequence(s))