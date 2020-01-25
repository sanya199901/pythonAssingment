class automobile:
    def __init__(self,make,model,mileage,price):
        self.make=make
        self.model=model
        self.mileage=mileage
        self.price=price

    def set_make(self,n):
        self.make=n
    def set_model(self,m):
        self.model=m
    def set_mileage(self,p):
        self.mileage=p
    def set_price(self):
        return self.price
    def get_make(self):
        return self.make
    def get_model(self):
        return self.model
    def get_mileage(self):
        return self.mileage
    def get_price(self):
        return self.price
obj=automobile(20,"zest","40kmph",600000)
print(obj.get_make())
