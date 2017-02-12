def check_balanced(string):
    stack = []
    for char in string:
        if char is '(' or char is '{' or char is '[':
            stack.append(char)
        else:
            if len(stack) > 0:
                cur = stack[-1]
                if (cur is '{' and char is '}') or (cur is '[' and char is ']') or (cur is '(' and char is ')'):
                    stack.pop()
            else:
                return False
    if len(stack) == 0:
        return True
    else:
        return False


def main():
    string = '()'
    print(string, 'is balanced:', check_balanced(string))
    string = '()([{}])'
    print(string, 'is balanced:', check_balanced(string))
    string = '()(){}{}[]'
    print(string, 'is balanced:', check_balanced(string))
    string = '()([{])'
    print(string, 'is balanced:', check_balanced(string))
    string = '()([]){'
    print(string, 'is balanced:', check_balanced(string))
    string = '{([])([])}'
    print(string, 'is balanced:', check_balanced(string))
    string = '()[])'
    print(string, 'is balanced:', check_balanced(string))
    string = '({['
    print(string, 'is balanced:', check_balanced(string))


if __name__ == '__main__':
    main()
