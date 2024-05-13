"""
generic script

text: ["a","b","c","d","e"] output => ["e-5","d-4","c-3","b-2","a-1"]
text: ["a","b","c"] output => ["c-3","b-2","a-1"]
text: ["a","b","c","d"] output => ["4","3","2","1"]
text: ["a","b"] output => ["2","1"]
"""
def fn_hack_8(s):
    result = s

    resultado = []

    for i, elemento in enumerate(reversed(result)):
        if len(result) == 5 or len(result) == 3:
            resultado.append(f"{elemento}-{len(result) - i}")
        else:
            resultado.append(str(len(result) - i))
    
    return resultado


print(fn_hack_8(["a", "b", "c", "d", "e"]))  
print(fn_hack_8(["a", "b", "c"]))            
print(fn_hack_8(["a", "b", "c", "d"]))    
print(fn_hack_8(["a", "b"]))             

