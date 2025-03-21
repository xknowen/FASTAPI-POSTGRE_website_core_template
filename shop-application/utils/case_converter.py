def camel_case_to_snake_case(input_str: str) -> str:
    chars = []
    for c_index, char in enumerate(input_str):
        if c_index and char.isupper():
            nxt_index = c_index + 1

            flag = nxt_index >= len(input_str) or input_str[nxt_index].isupper()
            prev_char = input_str[c_index - 1]
            if prev_char.isupper() and flag:
                pass
            else:
                chars.append('_')
        chars.append(char.lower())
    return ''.join(chars)