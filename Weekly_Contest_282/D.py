class Solution:
    def minimumFinishTime(self, tires: list[list[int]], changeTime: int, numLaps: int) -> int:
        go_straight = [inf for _ in range(19)]
        for f, r in tires:
            tot = cur = f
            go_straight[1] = min(go_straight[1], tot)
            for i in range(2,19):
                cur *= r
                tot += cur
                if tot > 2e5: # 2e5 is the maximum possible time for `changetime + best first step`.
                    break
                go_straight[i] = min(go_straight[i], tot)

        DP = [0 for _ in range(numLaps+1)]
        for i in range(1, numLaps + 1):
            DP[i] = go_straight[i] if i < 19 else inf
            for j in range(1, i//2+1):
                DP[i] = min(DP[i], DP[j] + changeTime + DP[i-j])
        return DP[-1]