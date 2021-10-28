def lengthOfLongestSubstring(s):
    ans = 0
    uniq = {}
    for i in range(len(s)):
        if s[i] not in uniq:
            if i == len(uniq):
                ans += 1
            else:
                length += 1
                if length > ans:
                    ans = length
            uniq[s[i]] = i
        else:
            length = i - uniq[s[i]]
            uniq[s[i]] = i
            if length > ans:
                ans = length
    return ans


s = "a"
print(lengthOfLongestSubstring(s))