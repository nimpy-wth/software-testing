from itertools import combinations
def alternate(s):
    def check(strr, m, n):
        newstr = ""
        pre = None
        for i in strr:
            if i == pre:
                return 0
            if i == m or i == n:
                newstr += i
                pre = i
        return len(newstr)
    
    ans = 0
    for m, n in list(combinations(sorted(set(s)), 2)):
        ans = max(ans, check(s, m, n))
    return ans