def longestPalindrome(s):
    lth = len(s)

    if len(set(s)) == 1:
        return s

    palindroms = []  # lengths of current palindroms
    ans = s[0]  # first symbol is our initial answer
    # to_del = []  # list of completed palindroms to delete from current
    for i in range(1, lth):
        for j in range(len(palindroms)):
            if palindroms[j]:
                if (i - palindroms[j] - 1)>= 0 and s[i] == s[i-palindroms[j]-1]:
                    palindroms[j] += 2
                else:
                    if palindroms[j] > len(ans):
                        ans = s[i-palindroms[j]:i]
                    palindroms[j] = 0

        if s[i] == s[i - 1]:  # every doubled symbols have center of symmetry between them
            palindroms.append(2)
        if (i-2)>=0 and s[i] == s[i-2]:
            palindroms.append(3)
    if not palindroms or len(ans) >= max(palindroms):
        return ans
    return s[lth-max(palindroms):]


s = "parrababar"
print(f"lP= {longestPalindrome(s)}")
