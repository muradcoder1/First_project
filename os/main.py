import os 
#create main function
def list_directiry(path="."):
     print("Contents of directiry")
     for item in os.listdir():
           print(item)
def create_directiry(directiry_name):
    try:
            
            os.makedirs(directiry_name)
    except FileExistsError:
            print("This file is exists please try another")
def remove_directory(directiry_name):
     try:
            os.rmdir(directiry_name)
     except FileNotFoundError:
            print("There is not the file")
def main():
    print("1. List contents of current directory")
    print("2. Create a new directory")
    print("3. Delete a directory")
    choice=input("What do you need 1/2/3")
    if choice=="1":
        list_directiry()
        
       
    elif choice=="2":
        filename=input("filemame")
        create_directiry(filename)
    elif choice=="3":
        filename=input("filename")
        remove_directory(filename)
        
    else:
        print("Sistem eror")
#__name__
if __name__=="__main__":
    main()
       
