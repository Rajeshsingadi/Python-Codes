def minSteps(s):
    def dp(s, prev, p_prev):
        if len(s)==0:
            return 0
        res = 1e9
        for i in range(1, len(s)+1):
            if s[:i] == prev:
                if p_prev == prev:
                    res = min(res, dp(s[i:], prev, p_prev))
                else:
                    res = min(res, 1 + dp(s[i:], prev, prev) )
            else:
                if s[:i] != s:
                    res = min(res, dp(s[:i], "", "") + dp(s[i:], s[:i], prev) )
                else:
                    res = min(res, len(s[:i]) + dp(s[i:], s[:i], prev))
        return res
    return dp(s, "", "")

# s="ABCABCE"
s="ABCDABCE"
print(minSteps(s))