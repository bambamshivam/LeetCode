class Solution:
    def kMirror(self, k: int, n: int) -> int:
        
        def fn(x):
            s = list(x)
            n = len(s)//2
            for i in range(n, len(s)): 
                if int(s[i])+1 < k: 
                    s[i] = s[~i] = str(int(s[i])+1)
                    for ii in range(n, i): s[ii] = s[~ii] = '0'
                    return "".join(s)
            return "1" + "0"*(len(s)-1) + "1"
                
        x = "0"
        ans = 0
        for _ in range(n): 
            x = fn(x)
            val = int(x, k)
            while str(val)[::-1] != str(val): 
                x = fn(x)
                val = int(x, k)
            ans += val
        return ans 