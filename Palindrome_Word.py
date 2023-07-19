def palindrome_String(Palindrome):
    for i in range(len(Palindrome)//2):
        if Palindrome[i] != Palindrome[-1-i]:
            return False
    return True

print(palindrome_String("non"))
print(palindrome_String("maaaam"))
print(palindrome_String("no"))
print(palindrome_String("false"))

#Run:****************************************
#True
#True
#False
#False
