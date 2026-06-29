def is_valid(string):
    stack = []
    for c in string:
        if c == "{" or c == "[" or c == "(":
            stack.append(c)
        if not stack:
            return False
        p = stack.pop()
        if c == "}" and p == "{":
            pass
        elif c == "]" and p == "[":
            pass
        elif c == ")" and p == "(":
            pass
        else:
            return False
    return len(stack) == 0
def main():
    test_str = "()[]"
    print(is_valid(test_str))
if __name__ == "__main__":  
    main()
