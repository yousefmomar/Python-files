from file_lib import R_file,W_file

strs=R_file("./Session Python/Mail/mails.txt")

mails=0
n=1

for i in range(0,len(strs)) :
    if strs[i]=="From" :
        if (i+1)<len(strs):
            W_file("  "+str(n),f="./Session Python/Mail/mails_output.txt")
            W_file(":    "+strs[i+1],f="./Session Python/Mail/mails_output.txt",padding="\n")
            mails+=1
            n+=1

W_file("=============================================================",f="./Session Python/Mail/mails_output.txt",padding="\n")
W_file("You have "+str(mails)+" mails Received",f="./Session Python/Mail/mails_output.txt",padding="\n")