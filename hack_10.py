"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"
    result = list(result.upper())
    for n in range(len(result)):
        if result[n] == "O":
            result[n] = "0"
        elif result[n] == "I":
            result[n] = "1"
        elif result[n] == "A":
            result[n] = "@"
    return result  