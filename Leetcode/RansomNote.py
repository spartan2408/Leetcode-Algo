class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        for e in ransomNote:
            if e in magazine:
                magazine = magazine.replace(e, "", 1)
            else:
                return False
        return True
