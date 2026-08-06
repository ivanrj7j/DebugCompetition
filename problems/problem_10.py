def decode_string(s: str) -> str:
    """
    Given an encoded string, return its decoded string.

    The encoding rule is: k[encoded_string], where the encoded_string inside the 
    square brackets is being repeated exactly k times. Note that k is guaranteed 
    to be a positive integer.

    You may assume that the input string is always valid; there are no extra white spaces, 
    square brackets are well-formed, etc. Furthermore, you may assume that the original 
    data does not contain any digits and that digits are only for those repeat numbers, k. 
    For example, there will not be input like 3a or 2[4].

    Examples:
    Input: s = "3[a]2[bc]"
    Output: "aaabcbc"

    Input: s = "3[a2[c]]"
    Output: "accaccacc"

    Input: s = "2[abc]3[cd]ef"
    Output: "abcabccdcdcdef"
    """
    stack = []
    current = ""
    repeat = 0
    for char in s:
        if char.isdigit():
            repeat = repeat * 10 + int(char)
        elif char == "[":
            stack.append((current, repeat))
            current = ""
            repeat = 0
        elif char == "]":
            prefix, count = stack.pop()
            current = prefix + current * count
        else:
            current += char

    return current
