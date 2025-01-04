"""
You are given a 0-indexed array of strings words and a 2D array of integers queries.
Each query queries[i] = [li, ri] asks us to find the number of strings present in the range li to ri (both inclusive) of words that start and end with a vowel.
Return an array ans of size queries.length, where ans[i] is the answer to the ith query.
Note that the vowel letters are 'a', 'e', 'i', 'o', and 'u'.

Input: words = ["aba","bcb","ece","aa","e"], queries = [[0,2],[1,4],[1,1]]
Output: [2,3,0]
Explanation: The strings starting and ending with a vowel are "aba", "ece", "aa" and "e".
The answer to the query [0,2] is 2 (strings "aba" and "ece").
to query [1,4] is 3 (strings "ece", "aa", "e").
to query [1,1] is 0.
We return [2,3,0].

"""
class Solution:
    def vowelStrings(self, words: list[str], queries: list[list[int]]) -> list[int]:
        vowel =set("aeiou")
        cnt = []
        final_output =[]
        for i in words:
            if  i[0] in vowel and i[-1] in vowel:
                cnt.append(1)
            else:
                cnt.append(0)
        for r in range(1,len(cnt)):
            cnt[r] = cnt[r] + cnt[r-1]
        for start, end in queries:
            result = cnt[end] - cnt[start-1] if start-1>=0 else cnt[end]
            final_output.append(result)

        return final_output

sol = Solution()
words =["aba","bcb","ece","aa","e"]
queries = [[0,2],[1,4],[1,1]]
print(sol.vowelStrings(words,queries))