class Solution:
    def kthSmallestProduct(self, A, B, k):
            n, m = len(A), len(B)
            A1,A2 = [-a for a in A if a < 0][::-1], [a for a in A if a >= 0]
            B1,B2 = [-a for a in B if a < 0][::-1], [a for a in B if a >= 0]

            neg = len(A1) * len(B2) + len(A2) * len(B1)
            if k > neg:
                k -= neg
                s = 1
            else:
                k = neg - k + 1
                B1, B2 = B2,B1
                s = -1

            def count(A, B, x):
                res = 0
                j = len(B) - 1
                for i in range(len(A)):
                    while j >= 0 and A[i] * B[j] > x:
                        j -= 1
                    res += j + 1
                return res

            left, right = 0, 10**10
            while left < right:
                mid = (left + right) // 2
                if count(A1, B1, mid) + count(A2, B2, mid) >= k:
                    right = mid
                else:
                    left = mid + 1
            return left * s