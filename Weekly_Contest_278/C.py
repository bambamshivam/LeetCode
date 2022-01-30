class Solution:
    def subStrHash(self, s: str, power: int, modulo: int, k: int, hashValue: int) -> str:
        n = len(s)
        val = 0
        ans = ""
        
        p_k_1 = 1
        for j in range(k - 1):
            p_k_1 = (p_k_1 * power) % modulo
        
        for i in range(n - k, -1, -1):
            sub = s[i:i+k]
            
            if i == n - k:
                val = self.hash(sub, power, modulo)
            else:
                c_val = ord(s[i + k]) - ord('a') + 1
                val = (val - c_val * p_k_1 + modulo) % modulo  
                val = (val * power) % modulo
                val = (val + ord(s[i]) - ord('a') + 1) % modulo
    
            if hashValue == val:
                ans = sub

        return ans
    
    def hash(self, s, p, m):
        
        hash_val = 0
        v = 1
        for i in range(len(s)):
            val = ord(s[i]) - ord('a') + 1
            hash_val = (hash_val + (val * v) % m) % m
            v = (v * p) % m 
            
        return hash_val