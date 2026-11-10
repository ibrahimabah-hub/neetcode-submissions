class Solution:
    def validPalindrome(self, s: str) -> bool:
        
        def isPalindrome(word):

            for i in range(len(word)//2):
                if word[i] != word[-(i+1)]:
                    return False

            return True

        if isPalindrome(s):
            return True

        for i in range(len(s)):

            newWord = list(s)
            newWord.pop(i)
            newWord = "".join(newWord)
            if isPalindrome(newWord):
                return True
            
        return False