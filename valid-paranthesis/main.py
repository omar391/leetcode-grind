def is_valid(s: str) -> bool:
    stack = []
    match = {"(": ")", "{": "}", "[": "]"}

    for char in s:
        if char in match:
            stack.append(match[char])
        elif not stack or stack[-1] != char:
            return False
        else:
            stack.pop()

    return not stack


print(is_valid("()"))
print(is_valid("()[]{}"))
print(is_valid("(]"))
print(is_valid("([)]"))
print(is_valid("{[]}"))
