def W_file(name=" ",opt="a",empty=0,f="Untitled.txt",padding=" "):
    hand=open(f,opt)
    if empty==0:
        hand.write(name+padding)
    hand.close()

def R_file(f):
    hand=open(f,"r")
    stds=hand.read()
    stds=stds.strip().split("\n")
    hand.close()
    return(stds)

