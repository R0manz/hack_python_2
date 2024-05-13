"""
text: [{"a":"b"},{"c","d"},{"e":"f"}] output => [{"1":"2"},{"3","4"},{"5":"6"}]
"""

def letter_to_number(letter):
    # Convertir la letra a su posición en el alfabeto (1-26)
    return str(ord(letter.lower()) - ord('a') + 1)

def fn_hack_10(result):
    output_list = []
    for dictionary in result:
        new_dict = {}
        for key, value in dictionary.items():
            new_key = letter_to_number(key)
            new_value = letter_to_number(value)
            new_dict[new_key] = new_value
        output_list.append(new_dict)
    return output_list

result = [{"a": "b"}, {"c": "d"}, {"e": "f"}]

output_list = fn_hack_10(result)

print(output_list)