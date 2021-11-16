def longestPalindrome(s: str) -> str:
    if s == s[::-1]:
        return s

    length = 1
    longestLen = 1

    for i in range(1, len(s)):
        oddLen = i - length - 1
        evenLen = i - length
        upto = i + 1

        oddWord = s[oddLen:upto]
        evenWord = s[evenLen:upto]

        if oddLen >= 0 and oddWord == oddWord[::-1]:
            longestLen = oddLen
            length += 2
        elif evenLen >= 0 and evenWord == evenWord[::-1]:
            longestLen = evenLen
            length += 1

    return s[longestLen:longestLen + length]


s = "parrabsdrd"
print(f"lP= {longestPalindrome(s)}")
