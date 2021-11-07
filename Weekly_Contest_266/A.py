class Solution:
    def countVowelSubstrings(self, s: str) -> int:
        n=len(s);c=0
        def solve(s):
            if 'a' not in s:
                return False
            if 'e' not in s:
                return False
            if 'i' not in s:
                return False
            if 'o' not in s:
                return False
            if 'u' not in s:
                return False
            for i in range(len(s)):
                if s[i]!='a' and s[i]!='e' and s[i]!='o' and s[i]!='u' and s[i]!='i':
                    return False
            return True
        for i in range(n):
            for j in range(n):
                if solve(s[i:j+1]):
                    c+=1
        return c