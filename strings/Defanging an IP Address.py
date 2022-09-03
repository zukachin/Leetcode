#Given a valid (IPv4) IP address, return a defanged version of that IP address.
#A defanged IP address replaces every period "." with "[.]".
#Example 1:
#Input: address = "1.1.1.1"
#Output: "1[.]1[.]1[.]1"

class solution:
    def defanIPadd(self,a:str)-> str:
        c=a.replace(".","[.]",len(a)-1)
        return c


address =input("Enter the ip address: ")
sol=solution()
print(sol.defanIPadd(address))