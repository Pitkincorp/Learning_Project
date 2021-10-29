def lengthOfLongestSubstring(s):
    ans = [0]

    def leng(s, ans):
        uniq = {}
        count = 0
        max = len(set(s))
        for i in range(len(s)):
            if ans[0] == max:
                break
            if s[i] not in uniq:
                count += 1
                uniq[s[i]] = i
                if count > ans[0]:
                    ans[0] = count
            else:
                return leng(s[uniq[s[i]]+1:], ans)

    leng(s, ans)
    return ans[0]


s = "bababbca"
print(lengthOfLongestSubstring(s))