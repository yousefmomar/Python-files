stds=list()
while True:
    opt=input("Enter your choice:\n 1.Enter new student\n 2.Print all\n 3.Search\n 4.Remove\n 5.Update\n 6.Sort or 'done' to exit\n").lower()

    if opt=="done":
        break

    elif opt=="1":
        name=input("Enter FN LN TERM GPA REG_NU : ").lower()
        stds.append(name)

    elif opt=="2":
        for i in range(0,len(stds)):
            print("Student ",i,":",stds[i],"\n")

    elif opt=="3":
        reg1=input("Enter REG_NU to Search for student : ")
        for name in stds :
            if reg1 in name:
                print(name,"\n")
                break
            else :
                print("Not Found!")

    elif opt=="4":
        reg2=input("Enter REG_NU to remove student : ")
        for name in stds :
            if reg2 in name:
                stds.remove(name)
                for i in range(0,len(stds)):
                    print("Student ",i,":",stds[i],"\n")
                break
            else :
                print("Not Found!")
            break
    elif opt=="5":
        reg3=input("Enter REG_NU to Update student's data : \n")
        for i in range(0,len(stds)):
            if reg3 in stds[i]:
                print(stds[i])
                new_name=input("\nEnter the new data for student : " ).lower()
                stds[i]=new_name
            break
    elif opt=="6":
        opt1=input("1.Sort a-z\n2.Sort z-a\n")
        if opt1=="1":
            stds=sorted(stds)
            for i in range(0,len(stds)):
                print("Student ",i,":",stds[i],"\n")
        
        elif opt1=="2":
            stds=sorted(stds,reverse=True)
            for i in range(0,len(stds)):
                print("Student ",i,":",stds[i],"\n")