def longestPalindrome( s):
    '''Manacher algorith'''
    _str = '$#' + '#'.join(s) + '#@'
    _id,mx = 0,0
    p = [0 for i in range(len(_str) + 1)]
    for i in range(1,len(_str) - 1):
        if i < mx:
            p[i] = min(mx - i,p[2 * _id - i])
        else:
            p[i] = 1
        while _str[i - p[i]] == _str[i + p[i]]:
            p[i] += 1
        if mx < i + p[i]:
            _id = i
            mx = i + p[i]
    _id,mx = 0,0
    for i in range(len(_str)):
        if mx < p[i]:
            _id = i
            mx = p[i]
    return _str[_id - p[_id] + 1:_id + p[_id]].replace('#','')


s = "trabbarabba"
print(longestPalindrome(s))
