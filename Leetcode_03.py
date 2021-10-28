def lengthOfLongestSubstring(s):
    ans = 0
    for i in range(len(s)):
        uniq = []
        for el in s[i:]:
            if el not in uniq:
                uniq.append(el)
            else:
                break
        if len(uniq) > ans:
            ans = len(uniq)
    return ans


s = "abcabcbb"
print(lengthOfLongestSubstring(s))
