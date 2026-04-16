

class Employee:
    
    def __init__(self, netsale, name, cctips, gratuity, cashtips):
        self.name = name
        self.cctips = cctips
        self.gratuity = gratuity
        self.cashtips = cashtips
        self.netsale = netsale

    def get_name(self):
        return self.name
    
    def get_cctips(self):
        return self.cctips
    
    def get_gratuity(self):
        return self.gratuity
    
    def get_cash(self):
        return self.cashtips

    def get_netsale(self):
        return self.netsale



        
