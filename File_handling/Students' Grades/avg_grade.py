def avgMax_G(fr,fw="Untitled.txt"):
    hand = open(fr,"r")
    student = hand.read()
    student = student.strip().split("\n")
    avr = []
    s = 0
    top_s = ""

    for i in range(len(student)):
        student[i] = student[i].strip().split(",")


    for i in range (len(student)):
        for j in range(1,6):
            s = s + float(student[i][j])
        avr.append(s/5)
        s = 0
    for i in range (len(avr)):
        if max(avr) == avr[i]:
            top_s = student[i][0]


    for i in range(0,len(student)):
        student[i].insert(1,":")
        student[i].insert(2,"[")
        student[i].insert(len(student[i]),"]")

    for i in range(0,len(student)):
        student[i] = " ".join(student[i])

    for i in range (0,len(student)):
        h = open(fw,"a")
        h.write(student[i] + "," + " Average = " + str(avr[i]) + "\n")
    h.write("----------------------------------------------\n")
    h.write("The Top Student is " + top_s + " With average Grade " + str(max(avr)) + "\n")
    h.close()
