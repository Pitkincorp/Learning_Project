def longestPalindrome(s):
    leng = len(s)

    def is_mirror(s):
        if s == s[::-1]:
            return True
        return False


    if len(set(s)) == 1:
        return s

    ans = s[0]
    for i in range(leng):
        if leng - i <= len(ans):
            break
        for j in range(i,leng+1):
            if j - i <= len(ans):
                continue
            if is_mirror(s[i:j]) and len(s[i:j]) > len(ans):
                ans = s[i:j]
    return ans


s = "trabbarabba"
print(longestPalindrome(s))
