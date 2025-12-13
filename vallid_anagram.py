from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
             s1 = Counter(s)
             t1 = Counter(t)
            
        return s1 == t1
