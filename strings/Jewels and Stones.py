#You're given strings jewels representing the types of stones that are jewels, and stones 
# representing the stones you have. Each character in stones is a type of stone you have. You want to know how many of the stones you have are also jewels.
#Letters are case sensitive, so "a" is considered a different type of stone from "A".
#Example 1:
#Input: jewels = "aA", stones = "aAAbbbb"
#Output: 3


class solution:
    def jands(self,jewels: str ,stones: str) -> str:
        count=0
        for gem in stones:
            if gem in jewels:
                count+=1
        return count

jewels="aA"
stones="aAAAbbbbb"
sol=solution()
print(sol.jands(jewels,stones))