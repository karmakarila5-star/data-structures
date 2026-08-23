def palindrome(mytuple):
    end = len(mytuple) -1
    start = 0
    while (start<end):
        if (mytuple[start] != mytuple[end]):
            return False
        start += 1
        end-=1
    return True

mytuple = (1, 2, 3, 3, 2, 1)
if (palindrome(mytuple)):
    print("the tuple is palindrome")
else:
    print("the tuple is not palindrome")