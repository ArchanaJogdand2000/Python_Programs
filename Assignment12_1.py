#write a program which accept one chatacter and check whether it is vowel or consonant

def CheckVowel(leter):
     if((leter == 'a') or (leter == 'e')or(leter == 'i')or(leter == 'o')or(leter == 'u')or
     (leter == 'A')or(leter == 'E')or(leter == 'I')or(leter == 'O')or(leter == 'U')):
         
          print("it is vowel")

     else:
          print("it is consonant")
def main():
   
    print("Enter character : ")
    Char = input()

    CheckVowel(Char)
    
       

if __name__ == "__main__":
    main()    
    
