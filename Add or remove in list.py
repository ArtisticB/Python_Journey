My_List=[1,2,43,45,7,33,90]
print(f"The Current List Has:{My_List}")
print("What Do You Want to Add And What You Want To Remove?")
add=int(input("Add:"))
remove=int(input("Remove:"))

My_List.remove(remove)
My_List.append(add)

print(f"Now The List Has:{My_List}")