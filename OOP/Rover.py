class Rover:
    def __init__(self,name,x,y,direct):
        self.__name=name
        self.__x=x
        self.__y=y
        self.set_dir(direct)

    def set_dir(self,d):
        self.__direct=d.lower()

    def get_dir(self): 
        return self.__direct
    
    def get_coordinates(self):
        return self.__x,self.__y
    
    def get_name(self):
        return self.__name
            
    def move(self,n):
        if n>0:
            if self.get_dir()=="forward":
                self.__y+=n
            
            elif self.get_dir()=="backward":
                self.__y-=n
            
            elif self.get_dir()=="right":
                self.__x+=n

            elif self.get_dir()=="left":
                self.__x-=n
        
        else:
            print("enter positive distance")

    def turn_right(self):
        if self.get_dir()=="forward":
            self.set_dir("right")

        elif self.get_dir()=="backward":
            self.set_dir("left")

        elif self.get_dir()=="right":
            self.set_dir("backward")

        elif self.get_dir()=="left":
            self.set_dir("forward")

    def turn_left(self):
        if self.get_dir()=="forward":
            self.set_dir("left")

        elif self.get_dir()=="backward":
            self.set_dir("right")

        elif self.get_dir()=="right":
            self.set_dir("forward")

        elif self.get_dir()=="left":
            self.set_dir("backward")
            

    def report(self):
        direct=self.get_dir()
        x,y=self.get_coordinates()
        print("Report :")
        print(f"x = {x}, y = {y}, direction = {direct}")

if __name__ == "__main__":
    r=Rover("ROV1",0,0,"forward")

    r.move(2)
    r.turn_right()
    r.move(1)
    r.report()

    r.turn_right()
    r.move(1)
    r.report()

    r.turn_right()
    r.move(2)
    r.report()