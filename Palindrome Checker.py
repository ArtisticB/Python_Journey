String=input("Palindrome Checker\n\nEnter The Word:")
result=""
for i in String:
    result=i+result

if result==String:
   print("You've Got Yourself A Palindrome") 
   
else:
    print("It's Not A Palindrome")
    
print(f"Because The Word's Reverse Is:{result}")