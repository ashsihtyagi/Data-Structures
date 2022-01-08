def isbalanced(str):
    mapping={"}":"{","]":"[",")":"("}
    stack=[]
    for ch in str:
        if ch in mapping:
            if len(stack)==0:#closing char
                return False

            top=stack.pop()
            if mapping[ch]!=top:
                return False

        else:
            stack.append(ch)#opening char

    return len(stack)==0


str=input()
print(isbalanced(str))