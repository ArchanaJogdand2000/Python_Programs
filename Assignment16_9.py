#Write a program which display first 10 even numbers on screen
def Even():
    
    for i in range(2,21,2):
        print(i,end="  ")

def main():

    Even()
    
if __name__ == "__main__":
    main()