
# print(mystr[::-1])

def reverse(s):
    return s[::-1]

def isPalindrome():
    mystr = input('enter any string:')
    if mystr == reverse(mystr):
        return "it's palindrom"
    else:
        return "not palindrome"

print(isPalindrome())