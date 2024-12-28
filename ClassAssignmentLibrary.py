class AssignmentLibrary():
    def Subfields(str):
        if(str=="AI"):
            print("Sub-fields in AI are:")
            SubfieldsAI=["Machine Learning","Neural Networks","Visison","Robotics","Speech Processing","Natural Language Processing"]
        for field in SubfieldsAI:
            print(field)

    def OddEven():
        num=int(input("Enter a number:"))
        if ((num%2)==0):
            print(num,"is Even number")
            message="The given number is even number"
        else:
            print(num,"is Odd number")
            message="The given number is odd number"
        return message

    def Elegible():
        gen=input("Your Gender:")
        age=int(input("Your Age:"))
        if(gen=="Male" and age>=21):
            print("Eligible")
        elif(gen=="Female" and age>=18):
            print("Eligible")
        else:
            print("Not Eligible")

    def percentage():
        sub1=int(input("Subject1="))
        sub2=int(input("Subject2="))
        sub3=int(input("Subject3="))
        sub4=int(input("Subject4="))
        sub5=int(input("Subject5="))
        Total=sub1+sub2+sub3+sub4+sub5
        print("Total:",Total)
        percentage=float((Total/500)*100)
        print("Percentage:",percentage)
        return percentage
      
    def triangle():
            val1=int(input("Height:"))
            val2=int(input("Breadth:"))
            area=float(val1*val2)/2
            print("Area of Traianle:",area)
            H1=int(input("Height1:"))
            H2=int(input("Height2:"))
            Br=int(input("Breadth:"))
            perimeter=H1+H2+Br
            print("Perimeter of Triangle:",perimeter)
            return area,perimeter
     
     
        