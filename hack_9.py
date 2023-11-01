"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    n = 0
    while(n <= 4):
        if n % 2 == 0:
            result.insert(n+1,"@")
        n += 1
    return result  