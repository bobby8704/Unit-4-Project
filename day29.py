def Palindrome(x):
    return str(x) == str(x)[::-1]   # This method is to check if the number is a palindrome number 

palindrome=[]
for x in range(100,1000): # for x is every number from 100 to 999
    for y in range(100,1000): # for y is every number from 100 to 999
        number = x*y * product of every three digits number 
        if Palindrome(number):  # check if the number is a palindrome number
            palindrome.append(number) # add the palindrome number to the list 
print(max(palindrome))
