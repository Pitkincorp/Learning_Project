def longestPalindrome(s):
    lth = len(s)

    if len(set(s)) == 1:
        return s

    centers = {}  # index of centers of palindroms and their length
    ans = s[0]  # first symbol is our initial answer
    for i in range(1, lth):
        for center,length in centers.items():
            if length > 0:
                if s[i] == s[i-length-1]:
                    centers[center] += 2
                else:
                    if length > len(ans):
                        ans = s[i-length:i]
                    centers[center] = 0
        centers[i] = 1  # every new symbol is a center of minimal palindrom with length=1
        if s[i] == s[i - 1]:  # every doubled symbols have center of symmetry between them
            centers[(i - 1 + i)/2] = 2
    if len(ans) >= max(centers.values()):
        return ans
    print(f"{ans=}")
    maxim = max(centers.values())
    return s[lth-maxim:]


s = "ardrar"
print(f"lP= {longestPalindrome(s)}")
