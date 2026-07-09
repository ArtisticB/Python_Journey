word="letter"
set_var=set()
for i in word:
    if i not in set_var:
        set_var.add(i)
        
    else:
        print(f"Duplicate Letter Detected!!\n({i})")