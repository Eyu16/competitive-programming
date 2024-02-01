def swap_case(s):
    result = ""
    for letter in s:
        if letter.islower():
            result += letter.upper()
        elif letter.isupper():
            result += letter.lower()
        else:
            result += letter
    return result
            

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)
