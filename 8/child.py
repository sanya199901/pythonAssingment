from automobile import*
import automobile
class Car(automobile):
    def __init__(self,make,model,mileage,price,doors):
        automobile.__init_(self,make,model,mileage,price)
        self.doors=doors
    def set_doors(self,d):
        self.doors=d
    def get_doors(self):
        return self.doors
class Truck(automobile):
    def __init__(self,make,model,mileage,price,drive_type):
        automobile.__init_(self,make,model,mileage,price)
        self.drive_type=drive_type
    def set_drive_type(self,t):
        self.drive_type=t
    def get_drive_type(self):
        return self.drive_type
class SUV(automobile):
    def __init__(self,pass_cap,make,model,mileage,price):
        automobile.__init_(self,make,model,mileage,price)
        self.pass_cap=pass_cap
    def set_pass_cap(self,c):
        self.pass_cap=c
    def get_pass_cap(self):
        return self.pass_cap

obj1=Car(35,'bmw','swift',876,203942)
obj1.set_doors(30)
print(obj1.get_doors())
