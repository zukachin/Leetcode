pos=-1

def binarysearch(list,n):
    #assign the start and end of the array in the list [5,7,9,13,32,33,42,54,56,88]
    #                                                   l                        u
    l=0
    u=len(list)-1

    #the search element should not be greater than the given the list of array
    while l<=u:
    #now find the mid point of the array
       mid=l+u//2
    #now check whether the mid value == search element
       if list[mid]==n:
    #now we need the index of the element so we using pos--index
         globals()['pos'] = mid
         return True
       else:
         if list[mid]<n:
            l= mid+1
         else:
            u=mid+1
    return False


#given a array in a list
list=[5,7,9,13,32,33,42,54,56,88]
#mention the search key 
n=9
#return found or not found using conditional statements
if binarysearch(list,n):
    print("found at",pos+1)
else:
    print("not found at",pos+1)
    
    
    
    
 -------------ANOTHER WAY--------------------------------
class Solution:
    def search(self, nums: List[int], target: int) -> int:
       pos=-1
       l,u=0,len(nums)-1
       while l<=u:
        mid=(l+u)//2
        if nums[mid]< target:
                l=mid+1
        elif nums[mid]> target:
                u=mid-1           
        else:
            return mid
       return -1
        
        
       
