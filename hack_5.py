"""
generic script

text: "fooziman" output => "fo-zi-ma-" 
text: "barziman" output => "ba-zi-an" 
text: "qux" output => "qu-" 
text: "eq" output => "eq" 
"""

def fn_hack_5(text):

    resultado = ""
    
    for i in range(0, len(text), 2):
        segment = text[i:i+2]
        
        resultado += segment
        
        if i + 2 < len(text):
            resultado += "-"
    
    return resultado

texts = ["fooziman", "barziman", "qux", "eq"]

for text in texts:
    print(fn_hack_5(text))
