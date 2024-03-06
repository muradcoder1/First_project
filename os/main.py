import os 
#create main function
def list_directiry(path="."):
     print("Contents of directiry")
     for item in os.listdir():
           print(item)

def main():
    print("1. List contents of current directory")
    print("2. Create a new directory")
    print("3. Delete a directory")
    choice=input("What do you need 1/2/3")
    if choice=="1":
        list_directiry()
        
       
    elif choice=="2":
         filename=input("filemame")
         try:
            
            os.makedirs(filename)
         except FileExistsError:
            print("This file is exists please try another")
    elif choice=="3":
        filename=input("filename")
        try:
            
            os.rmdir(filename)
        except FileNotFoundError:
            print("There is not the file")
    else:
        print("Sistem eror")
#__name__
if __name__=="__main__":
    main()
       
