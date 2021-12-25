class Solution(object):
    def abbreviateProduct(self, left, right):
        MAX = 10 ** 20
        pre, suf, c = 1, 1, 0
        for n in range(left, right + 1):
            pre *= n
            suf *= n
            while suf % 10 == 0:
                c += 1
                suf //= 10
            if suf > MAX:
                suf %= MAX
            while pre > MAX:
                pre //= 10
        if suf < 10 ** 10:
            return str(suf) + 'e' + str(c)
        else:
            return str(pre)[:5] + '...' + str(suf)[-5:] + 'e' + str(c)