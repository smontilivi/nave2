class Nau:

    def __init__(self,x,y):        
        self.x=x
        self.y=y
        self.incr=1

    def moure_dreta(self):
        self.x=self.x+self.incr
        
    def moure_esquerre(self):
        self.x=self.x-self.incr

    def moure_amunt(self):
        self.y=self.y+self.incr
        
    def moure_avall(self):
        self.y=self.y-self.incr
        
    def mostrar(self):
        print()
        print("   *")
        print("  ***")
        print(" *****")
        print("*******")
        print(f"x:{self.x}, y:{self.y}")        
        print()