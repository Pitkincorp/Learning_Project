ls = [
    0,
    0,
    [
        0,
        [
            0,
            [
                0
            ],
            0,
            0
            ],
        0,
        0,
        0,
        [
            0,
            0
        ]
        ],
    [
        [
            [
                [
                    0
                ]
            ]
        ]
    ]
    ]

def lev_rec(ls, el):
    '''accepts iterable sequence and returns the quantity of
     elements on each level of matrix'''

    def recursion(ls, el, level):
        nonlocal ans
        level += 1
        # number = 0
        for i in ls:
            if i == el:
                # number += 1
                if level in ans:
                    ans[level] += 1
                else:
                    ans[level] = 1
            elif type(i) == list:
                recursion(i, el, level)


    level = 0
    ans = {}
    recursion(ls, el, level)
    return ans

print(lev_rec(ls, 0))
