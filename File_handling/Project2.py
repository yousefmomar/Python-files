import file_lib
from Stds_lib import*

while True:
    opt=input("Enter your choice:\n 1.Enter new student\n 2.Print all\n 3.Search\n 4.Remove\n 5.Update\n 6.Sort or 'done' to exit\n").lower()

    if opt=="done":
        break
    elif opt=="1":
        name=file_lib.enter_std()

        if name!="wrong":
            file_lib.W_file(name,f="Students.txt",padding="\n")
    
    elif opt=="2":
        stds=file_lib.R_file("Students.txt")
        print_all(stds)
    
    elif opt=="3":
        stds=file_lib.R_file("Students.txt")
        search(stds)
    
    elif opt=="4":
        stds=file_lib.R_file("Students.txt")
        remove("Students.txt",stds)

    elif opt=="5":
        stds=file_lib.R_file("Students.txt")
        update("Students.txt",stds)

    elif opt=="6":
        stds=file_lib.R_file("Students.txt")
        SrtPrint(stds)
       
