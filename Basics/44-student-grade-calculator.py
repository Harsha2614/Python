n=int(input("Enter the number of students to be Entered : "))
while(n>0):
    
        name=input("Enter the name of the Student: ")
        sub1=int(input("Enter the marks in subject 1 : "))
        sub2=int(input("Enter the marks in subject 2 : "))
        sub3=int(input("Enter the marks in subject 3 : "))
        sub4=int(input("Enter the marks in subject 4 : "))
        sub5=int(input("Enter the marks in subject 5 : "))
        total=sub1+sub2+sub3+sub4+sub5
        avg=total/5
        print("---------------*Marks Memo*--------------")
        print("Name of the Student : ",name)
        print("Total Marks : ",total)
        print("Average Marks : ",avg)
        if(avg>=90):
            print("Grade A")
            print("Excellent Performance!")
        elif(avg>=80 and avg <90):
            print("Grade B")
            print("Keep Practicing!")
        elif(avg>=70 and avg<80):
            print("Grade C")
            print("Keep Practicing!")
        elif(avg>=60 and avg<70):
            print("Grade D")
            print("Keep Practicing!")
        else:
            print("Grade F (Failed)")
            print("Keep Practicing!")
        print("----------------------xxxxxx--------------")
        n=n-1


    