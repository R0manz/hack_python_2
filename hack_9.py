"""
text: {"foo":"fooziman","bar":"barziman"} output => {"Foo":"Fooziman"}
"""


def fn_hack_9(s):
    result = s
    output_dict = {}
    
    first_key = next(iter(result))
    first_value = result[first_key]
    new_key = first_key.capitalize()
    new_value = first_value.capitalize()
    
    output_dict[new_key] = new_value
    
    return output_dict
print(fn_hack_9({"foo":"fooziman","bar":"barziman"}))