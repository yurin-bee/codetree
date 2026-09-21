A = input()

# Please write your code here.

def palindrome(string):
    if string == string[::-1]:
        print("Yes")
    else:
        print("No")
palindrome(A)