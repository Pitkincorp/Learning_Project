def lengthOfLongestSubstring(s):
    ans = 0
    max = len(set(s))
    for i in range(len(s)):
        if ans == max:
            break
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
