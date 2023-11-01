"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    for i in result:
        if i == 1 or i == 9:
            result.remove(i)
    return result  