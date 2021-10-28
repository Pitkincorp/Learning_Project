def lengthOfLongestSubstring(s):
    ans = 0
    uniq = {}
    for i in range(len(s)):
        if s[i] not in uniq:
            uniq[s[i]] = i
        else:
            uniq = {k: v for k,v in uniq.items() if v > uniq[s[i]]}
            uniq[s[i]] = i
        if len(uniq) > ans:
            ans = len(uniq)
    return ans


s = "pwwkew"
print(lengthOfLongestSubstring(s))