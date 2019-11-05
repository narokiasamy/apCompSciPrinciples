# whether string or integer, program should see if it is a palindrome
palindrome = input("Enter word/number to see if it is a palindrome: ")

# reverse after swtiching to string
stringForm = str(palindrome)
reverse = (str(stringForm))[::-1]

# check to seee if palindrome
if (stringForm == reverse):
    print("Input is a palindrome!")
elif (stringForm != reverse):
    print("Input is not a palindrome!")