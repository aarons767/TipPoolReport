from Employee import Employee as e

class Report:

    def __init__(self, employees, total_points):
        self.total_ = total_points
        self.employee = []

    #To be finished later. Total PV
    def calculate_totalPoints():
        return
    

    def compute_totalCCTips(self):
        total = 0.0
        for employee in self.employee:
            total += employee.get_cctips()
        return total
    
    def compute_totalGrat(self):
        total = 0.0
        for employee in self.employee:
            total += employee.get_gratuity()
        return total
    
    def compute_totalCash(self):
        total = 0.0
        for employee in self.employee:
            total += employee.get_cash()
        return total
    
    

    
    
