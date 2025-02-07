class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazineLetters={}
        for i in range(len(magazine)):
            m=magazine[i]
            currentCount=magazineLetters.get(m,0)
            magazineLetters.update({m: currentCount+1})

        for i in range(len(ransomNote)):
            r=ransomNote[i]
            currentCount=magazineLetters.get(r,0)
            
            if currentCount==0:
                return False
            magazineLetters.update({r:currentCount-1})
        return True