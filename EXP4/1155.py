class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 1000000007
        dp = [0] * (target + 1)
        dp[0] = 1
        for _ in range(n):
            temp = [0] * (target + 1)
            x = 0
            for j in range(1, target + 1):
                x = (x + dp[j - 1]) % MOD
                if j - k - 1 >= 0:
                    x = (x - dp[j - k - 1] + MOD) % MOD
                temp[j] = x
            dp = temp
        return dp[target]