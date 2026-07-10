String=input("Anagram Checker\n\nEnter The Word:")
String2=input("Enter Another The Word:")

result=sorted(String)
result2=sorted(String2)

if result2==result:
   print("You've Got Yourself An Anagram") 
   
else:
    print("It's Not An Anagram")