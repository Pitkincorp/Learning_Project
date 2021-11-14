def longestPalindrome(s):
    lth = len(s)

    if len(set(s)) == 1:
        return s

    centers = {}  # index of centers of palindroms and their lengths
    ans = s[0]  # first symbol is our initial answer
    for i in range(1, lth):
        for center,length in centers.items():
            if length > 0:
                if (i - length - 1)>= 0 and s[i] == s[i-length-1]:
                    centers[center] += 2
                else:
                    if length > len(ans):
                        ans = s[i-length:i]
                    centers[center] = 0

        if s[i] == s[i - 1]:  # every doubled symbols have center of symmetry between them
            centers[i - 0.5] = 2
        if (i-2)>=0 and s[i] == s[i-2]:
                    centers[i - 1] = 3
    if not centers or len(ans) >= max(centers.values()):
        return ans
    maxim = max(centers.values())
    return s[lth-maxim:]


s = "par"
print(f"lP= {longestPalindrome(s)}")
