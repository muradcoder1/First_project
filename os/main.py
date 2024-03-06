import os 
#create main function
def main():
    print("1. List contents of current directory")
    print("2. Create a new directory")
    print("3. Delete a directory")
    choice=input("What do you need 1/2/3")
    if choice=="1":
        print(os.listdir())
        for item in os.listdir():
           print(item)
    elif choice=="2":
         filename=input("filemame")
         os.makedirs(filename)
    elif choice=="3":
         filename=input("filename")
         os.rmdir(filename)
    else:
        print("Sistem eror")
#__name__
if __name__=="__main__":
    main()
       
