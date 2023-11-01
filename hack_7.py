"""
loop: while [] output => [5,4,3,2,1,0]
"""

def fn_hack_7():
    result = []
    n = 0
    while(n <= 5):
        result.append(5-n)
        n += 1
    return result