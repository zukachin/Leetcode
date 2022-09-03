#You are given a string s and an integer array indices of the same length. The string s will be 
# shuffled such that the character at the ith position moves to indices[i] in the shuffled string.
#Return the shuffled string.

#Input: s = "codeleet", indices = [4,5,6,7,0,2,1,3]
#Output: "leetcode"
#Explanation: As shown, "codeleet" becomes "leetcode" after shuffling.

class solution:
    def shufflestring(self,s,indices):
       a=" "
       for i in range(len(s)):
        a+=s[indices.index(i)]
       return a

s=(input("Enter a string: "))
l=list(map(int,input("Type with a space: ").split()))
if len(l)>len(s):
    print( "Please check your length of the input given in the list.\nTry again!!!!")

sol=solution()
print(sol.shufflestring(s,l))




       
