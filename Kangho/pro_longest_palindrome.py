# def solution(s):
#     sl = len(s)
#     rs = s[::-1]
#     dp = [[0] * (sl+1) for _ in range(sl+1)]
#     for i in range(1, sl+1):
#         for j in range(1, sl+1):
#             if s[i-1] == rs[j-1]:
#                 dp[i][j] = dp[i-1][j-1] + 1
#             else:
#                 dp[i][j] = max(dp[i-1][j], dp[i][j-1])
#     answer = dp[sl][sl]
#     return answer
# this code is for univ final exam

import sys
sys.setrecursionlimit(100000)
def p(s):
    if len(s) <= 1:
        return True
    
    if s[0] == s[-1]:
        return p(s[1:-1])
    else:
        return False

def solution(s):
    for cut in range(len(s), 0, -1):
        for start in range(0, len(s)):
            cutStr = s[start:start+cut]
            if p(cutStr) == True:
                return len(cutStr)
            
            if start+cut >= len(s):
                break

