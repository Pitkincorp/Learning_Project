def longestPalindrome(s):


    def is_mirror(s):
        mid = len(s)//2
        if len(s) % 2:
            if s[:mid] == s[-1:mid:-1]:
                return True
        else:
            if s[:mid] == s[-1:mid-1:-1]:
                return True
        return False


    if len(set(s)) == 1:
        return s

    ans = ''
    for i in range(len(s)):
        for j in range(i,len(s)+1):
            if is_mirror(s[i:j]) and len(s[i:j]) > len(ans):
                ans = s[i:j]
    return ans


s = 'a'
print(longestPalindrome(s))
