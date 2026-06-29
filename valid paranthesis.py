def is_valid(string):  # Renamed 'str' to avoid overwriting Python's built-in keyword
    stack = []
    for c in string:
        # Step 1: If it's an opening bracket, push it and move to the next character
        if c == "{" or c == "[" or c == "(":
            stack.append(c)
            continue  # Critical: Skip the pop logic for opening brackets!
            
        # Step 2: If we see a closing bracket but the stack is empty, it's invalid
        if not stack:
            return False
            
        # Step 3: Pop the last opening bracket to match it with the current closing bracket
        p = stack.pop()
        if c == "}" and p == "{":
            pass
        elif c == "]" and p == "[":
            pass
        elif c == ")" and p == "(":
            pass
        else:
            return False
            
    # Step 4: Moved outside the loop! Returns True only after checking everything.
    return len(stack) == 0

def main():
    test_str = "()[]"
    print(is_valid(test_str))

if __name__ == "__main__":  # Fixed to standard Python execution guard
    main()
