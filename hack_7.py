"""
generic script

["1",2] => type string & type int
[0] => type int

text: ["a","b","c","d","e"] output => ["1",2,"3",4,"5"]
text: [0] output => [0] 
"""
def fn_hack_7(s):
    result = s
    if result == [0]:
        return [0]
    
    resultado = []

    for i, elementos in enumerate(result):
        if i%2==0:
            resultado.append(str(i + 1))
        else:
            resultado.append(i+1)
    return resultado

print(fn_hack_7(["a","b","c","d","e"]))
print(fn_hack_7([0]))