class Contect:
    def __init__(self,name,phone_no,email):
        self.name=name
        self.phone_no=phone_no
        self.email=email
        
    def get_name(self):
        return self.name


    def get_phone_no(self):
        return self.phone_no


    def get_email(self):
        return self.email


    


    
def main():
    object=Contect('sanya','909','google.com')
    print('name is ',object.get_name())
    print('no. is ',object.get_phone_no())
    print('mail is ',object.get_email())

main()




    
