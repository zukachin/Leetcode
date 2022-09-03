#Given a string s, return the string after replacing every uppercase letter with the same lowercase letter.
#Example 1:
#Input: s = "Hello"
#Output: "hello"


class solution:
    def lowercase(self,l:str)-> str:
        return l.lower()

l="HELLo"
s=solution()
print(s.lowercase(l))