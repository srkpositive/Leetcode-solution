
def isPalindrome(x):
    if str(x) == str(x)[::-1]:
        return True
    else: 
        return False
print(isPalindrome(130))