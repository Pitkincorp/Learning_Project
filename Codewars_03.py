def recoverSecret(triplets):
    r = list(set([i for l in triplets for i in l]))
    for l in triplets:
        fix(r, l[1], l[2])
        fix(r, l[0], l[1])
    return ''.join(r)


def fix(l, a, b):
    """let l.index(a) < l.index(b)"""
    if l.index(a) > l.index(b):
        l.remove(a)
        l.insert(l.index(b), a)


triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]
triplets2 = [
    ['l', 'e', 'd'],
    ['o', 'e', 'd'],
    ['o', 'l', 'e'],
    ['o', 'v', 'e'],
    ['s', 'o', 'l'],
    ['s', 'e', 'd'],
    ['s', 'l', 'e'],
    ['v', 'e', 'd'],
    ['o', 'l', 'v'],
    ['l', 'v', 'd']
]
triplets3 = [
    ['t', 's', 'f'],
    ['a', 's', 'u'],
    ['m', 'a', 'f'],
    ['a', 'i', 'n'],
    ['s', 'u', 'n'],
    ['m', 'f', 'u'],
    ['a', 't', 'h'],
    ['t', 'h', 'i'],
    ['h', 'i', 'f'],
    ['m', 'h', 'f'],
    ['a', 'u', 'n'],
    ['m', 'a', 't'],
    ['f', 'u', 'n'],
    ['h', 's', 'n'],
    ['a', 'i', 's'],
    ['m', 's', 'n'],
    ['m', 's', 'u']
]
triplets4 = [
    ['g', 'a', 's'],
    ['o', 'g', 's'],
    ['c', 'n', 't'],
    ['c', 'o', 'n'],
    ['a', 't', 's'],
    ['g', 'r', 't'],
    ['r', 't', 's'],
    ['c', 'r', 'a'],
    ['g', 'a', 't'],
    ['n', 'g', 's'],
    ['o', 'a', 's']
]
print(recoverSecret(triplets))
print(recoverSecret(triplets2))
print(recoverSecret(triplets3))
print(recoverSecret(triplets4))