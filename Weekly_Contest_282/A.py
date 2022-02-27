class Solution:
    def prefixCount(self, words: list[str], pref: str) -> int:
        c=0
        for i in words:c+=i.startswith(pref)
        return c