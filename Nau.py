class Nau:

    def __init__(self,x,y):        
        self.x=x
        self.y=y
        self.incr=1

    def moure_dreta(self):
        self.x=self.x+self.incr
        
    def moure_esquerre(self):
        pass

    def moure_amunt(self):
        pass
        
    def moure_avall(self):
        pass
        
    def mostrar(self):
        print()
        print("   *")
        print("  ***")
        print(" *****")
        print("*******")
        print(f"x:{self.x}, y:{self.y}")        
        print()