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
    # Naive stack-free parser that is highly incorrect.
    # It cannot handle nested brackets (like 3[a2[c]]) or multiple blocks.
    # Students must implement stack state tracking from scratch.
    res = ""
    curr_num = 0
    stack=[]
    for char in s:
        if char.isdigit():
            curr_num = curr_num * 10 + int(char)
            if len(stack)>0 and stack[-1]==1:
                stack.pop()
            stack.append(curr_num)
        elif char == "[":
            curr_num=0
            stack.append(char)
        elif char == "]":
            c=stack.pop()
            r=""
            while c!="[":
                r +=c
                c=stack.pop()
            # res = res * curr_num
            # curr_num = 0
            stack.append(r[::-1]*stack.pop())
        else:
            stack.append(char)
    res=""
    for i in stack:
      res+=i
    return res
