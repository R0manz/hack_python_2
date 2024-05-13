"""
generic script

["1","-"] => type string
["0"] => type string

text: ["a","b","c","d","e"] output => ["1","-","3","-","5"]
text: [] output => ["0"] 
"""
def fn_hack_6(s):
    result = s
    if not result:
        return ["0"]
    
    resultado = []
    
    for i, elemento in enumerate(result):
        if i % 2 == 0:
            resultado.append(str(i+1))
        else:
            resultado.append("-")
    return resultado

print(fn_hack_6(["a","b","c","d","e"]))
print(fn_hack_6([]))

