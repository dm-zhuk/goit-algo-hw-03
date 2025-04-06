def check_delimiters(expression):
    pairs = {")": "(", "]": "[", "}": "{"}
    # stack to store opening delimiters
    stack = []

    for char in expression:
        if char in "([{":
            stack.append(char)
        elif char in ")]}":
            # check if the top of the stack (stack[-1]) matches the expected opening delimiter
            if not stack or stack[-1] != pairs[char]:
                return "Несиметрично"
            # Match found, pop the stack
            stack.pop()

    # if stack is empty, all delimiters matched
    return "Симетрично" if not stack else "Несиметрично"


def main():
    print("\n|              Test case 1            |")
    print("|-------------------------------------|")

    test_cases = ["( ){[ 1 ]( 1 + 3 )( ){ }}", "( 23 ( 2 - 3);", "( 11 }"]

    for test in test_cases:
        result = check_delimiters(test)
        print(f"{test}: {result}")

    print("\n|                     Test case 2                    |")
    print("|----------------------------------------------------|")

    input_expression = input("Введіть Ваш рядок з розділювачами (, ), [, ], {, }: ")
    result = check_delimiters(input_expression)
    print(result)


if __name__ == "__main__":
    main()
