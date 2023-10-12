class user:
        def __init__(self,name,phone_number,email,address,password):
                self.name =name
                self.phone_number =phone_number
                self.email=email
                self.address =address
                self.password =password
        def __str__(self):
                return f"Name: {self.name} \n Phone Number: {self.phone_number} \n Email: {self.email} \n Address :{self.address} \n Password: {self.password}"  
              
        def get_name(self):
                return self.name
        def get_phone_number(self):
                return self.phone_number
        def get_email(self):
                return self.email
        def get_address(self):
                return self.address
        def get_password(self):
                return self.password
        def set_name(self,name):
                self.name = name
        def set_phone_number(self,phone_number):
                self.phone_number =phone_number
        def set_email(self,email):
                self.email =email
        def set_address(self,address):
                self.address =address
        def set_password(self,password):
                self.password =password                                







