class Solution(object):
    def wonderfulSubstrings(self, word: str) -> int:
        mask = 0
        mask_count = [0] * 1024
        mask_count[mask] += 1
        res = 0

        for letter in word:
            mask ^= 1 << ord(letter) - ord("a")
            res += mask_count[mask]
            for i in range(10):
                res += mask_count[mask ^ 1 << i]
            mask_count[mask] += 1
        return res

obj=Solution()
print(obj.wonderfulSubstrings("ccbbc"))

