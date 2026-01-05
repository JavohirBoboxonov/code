class Fructis:
    def __init__(self, fructis_name):
        self.fructis_name = fructis_name
    
    def get_info(self):
        return f"""
Name:{self.fructis_name}
"""
    
class Shop:
    def __init__(self, name):
        self.name = name
        self.products = []
    
    def add_fruct(self, new_fruct):
        if new_fruct not in self.products:
            self.products.append(new_fruct)
    
    def show_products(self):
        for i in self.products:
            print(i)
    
    def show_five(self):
        for k in self.products:
            if len(k) >= 5:
                print(k)
s1 = Shop("Cola")
s2 = Fructis("Olma")
s1.add_fruct(s2)
# s1.show_products()
s3 = Fructis('LEMON')
s1.add_fruct(s3)
s1.show_five()  