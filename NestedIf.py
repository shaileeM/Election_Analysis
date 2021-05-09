marks = int(input("What are your marks"))
if marks >=90:
    print("your grade is A")
else:
    if marks >=80:
        print("grade is B")
    else:
        if(marks>=70):
            print("grade is C")
        else:
            if(marks>=60):
                print("grade is D")
            else:
                print("grade is f")