def decode_string(s: str) -> str:
    count_stack = []
    string_stack = []

    curr_str = ""
    curr_num = 0

    for char in s:
        if char.isdigit():
          curr_num = curr_num * 10 + int(char)

        elif char == "[":
          count_stack.append(curr_num)
          string_stack.append(curr_str)
          curr_num = 0
          curr_str = ""

        elif char == "]":
          repeat = count_stack.pop()
          prev = string_stack.pop()
          curr_str = prev + curr_str * repeat

        else:
          curr_str += char

    return curr_str
