 #You are given an m x n integer grid accounts where accounts[i][j] is the amount of 
 # money the i​​​​​​​​​​​th​​​​ customer has in the j​​​​​​​​​​​th​​​​ bank. Return the wealth that the richest customer has.
#A customer's wealth is the amount of money they have in all their bank accounts. The richest customer is the customer that has the maximum wealth.
#Example 1:

#Input: accounts = [[1,5],[7,3],[3,5]]
#Output: 10
#Explanation: 
#st customer has wealth = 6
#2nd customer has wealth = 10 
#3rd customer has wealth = 8
#The 2nd customer is the richest with a wealth of 10.


class Solution:
    def maximumWealth(self, accounts):
       m=0
       for i in accounts:
            m=max(m,sum(i))
       return m

n=list(map(int,input("Enter the numbers").split(",")))
b=list(map(int,input("Enter the numbers").split(",")))
l=[n,b]
s=Solution()
print(s.maximumWealth(l) )