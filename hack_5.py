"""
text: "fooziman" output => "f00z1m@n"
"""

def fn_hack_5():
    result = "fooziman"
    r = 0
    result = list(result)
    while (r < len(result)):
        if result[r] == "o":
            result[r] = "0"
        elif result[r] == "i":
            result[r] = "1"
        elif result[r] == "a":
            result[r] = "@"
        r += 1
    result = "".join(result)
    return result