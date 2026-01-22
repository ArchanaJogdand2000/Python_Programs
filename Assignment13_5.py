# Write a program which accept marks and displays grade
# >=75--> Distingtion
# >=60--> First class
# >=50--> Second Class
# <50--> Fail

Invalid = -1
Fail = 1
Second_Class = 2
First_Class = 3
Distingtion = 4

def DisplayResult(marks):

    if((marks < 0) or (marks > 100)):
       return Invalid

    if((marks > 0)and(marks < 50)):
       return Fail 

    elif((marks >= 50)and(marks < 60)):
       return Second_Class 

    elif((marks >= 60)and(marks < 75)):   
       return First_Class
    
    elif((marks >= 75)and(marks <= 100)):
       return Distingtion
              

def main():
    print("Enter number Marks: ")
    Value = int(input())

    iRet = DisplayResult(Value)
   
    if(iRet == Invalid):
        print(" Your input is invalid ")
    if(iRet == Fail):
        print("Student is fail..") 
    elif(iRet == Second_Class):
        print("Studend pass with Second class..")
    elif(iRet == First_Class):
        print("Studend pass with First class..")  
    elif(iRet == Distingtion):
        print("Student is having distinction")

    
if __name__ == "__main__":
    main()
