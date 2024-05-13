"""
generic script

a = @
e = 3
i = ¡
o = 0
u = v

text: "fooziman" output => "F00z¡m@N" 
text: "barziman" output => "B@rz¡m@N" 
text: "3q" output => "3Q" 
text: "qu" output => "Qv" 
text: "qux" output => "QvX" 
"""
def fn_hack_3(s):
    replacements = {'a': '@', 'e': '3', 'i': '¡', 'o': '0', 'u': 'v'}
    text = s
    result = ''
    if len(text)>1:
        for char in text:
            if char in replacements:
                result += replacements[char]
            else:
                result += char   
    return result[0].upper() + result[1:-1] + result[-1].upper()

print(fn_hack_3("fooziman"))
print(fn_hack_3("barziman"))
print(fn_hack_3("3q"))
print(fn_hack_3("qu"))
print(fn_hack_3("qux"))
