while True:
    try:
        sub1=int(input("Enter your English marks: "))
        sub2=int(input("Enter your Maths marks: "))
        sub3=int(input("Enter your physics marks: "))
        sub4=int(input("Enter your chemistry marks: "))
        sub5=int(input("Enter your computer marks: "))
    except (ValueError, SyntaxError, NameError):
        print("Marks should be in range 0-100.")
        continue
    if sub1>100 or sub2>100 or sub3>100 or sub4>100 or sub5>100 or sub1<0 or sub2<0 or sub3<0 or sub4<0 or sub5<0:
        print("Marks should be in range 0-100.")
        continue
    else:
        total=sub1+sub2+sub3+sub4+sub5
        print("Total marks: ",total)
        print("Average marks: ", total/5)
        highest=max(sub1,sub2,sub3,sub4,sub5)
        print("Highest marks:", highest)
        lowest=min(sub1,sub2,sub3,sub4,sub5)
        print("Lowest marks: ", lowest)
        if 450<=total<=500:
            print("Grade: A")
            print("Status: Pass")
        elif 400<=total<450:
            print("Grade: B")
            print("Status: Pass")
        elif 350<=total<400:
            print("Grade: C")
            print("Status: Pass")
        elif 300<=total<350:
            print("Grade: D")
            print("Status: Pass")
        elif 250<=total<300:
            print("Grade: E")
            print("Status: Pass")
        else:
            print("Grade: F")
            print("You failed, Better Luck Next Time")
        break