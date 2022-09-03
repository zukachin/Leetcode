#A pangram is a sentence where every letter of the English alphabet appears at least once.
#Given a string sentence containing only lowercase English letters, return true if sentence is a pangram, or false otherwise.
#Example 1:
#Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
#Output: true
#Explanation: sentence contains at least one of every letter of the English alphabet.



class solution:
    def pan(self,sentence: str)->str:
        if len(set(sentence))==26:
            return True
        else:
            return False

sentence="thequickbrownfoxjumpsoverthelazydog"
k=solution()
print(k.pan(sentence))