from Employee import Employee 

class Report:
    SERVER_PV = 9
    RUNNER_PV = 6
    BUSSER_PV = 5
    KITCHEN_HOST_PV = 3
    EXPO_PV = 7
    

    def __init__(self, employees = None, total_points=0):
        self.total_points = total_points
        self.employees = employees if employees is not None else []

    #To be finished later. Total PV
    def set_total_points(self, total):
        self.total_points = total
    

    def compute_totalCCTips(self):
        total = 0.0
        for employee in self.employees:
            total += employee.cctips
        return total
    
    def compute_totalGrat(self):
        total = 0.0
        for employee in self.employees:
            total += employee.gratuity
        return total
    
    def compute_totalCash(self):
        total = 0.0
        for employee in self.employees:
            total += employee.cashtips
        return total
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    
    def compute(self):
        totalcctips = self.compute_totalCCTips()
        totalgrat = self.compute_totalGrat()
        totalcash = self.compute_totalCash()
        
        print(f"\n{30*'-'} Employee Report {30*'-'}\n")
        print(f"{'Employee':<17}{'Position':<17}{'Net Sale':<17}{'Cash Tips':<17}{'Credit Card Tips':<17} {'Gratuity':>17}\n")
        
        for this_employee in self.employees:
            if(this_employee.position.casefold() == "Server" or this_employee.position.casefold() == "Bartender"):
                self.total_points+=9
            if(this_employee.position.casefold() == "Runner"):
                self.total_points+=6
            if(this_employee.position.casefold() == "Expo"):
                self.total_points+=7
            if(this_employee.position.casefold() == "Kitchen" or this_employee.position.casefold() == "Host"):
                self.total_points+=3
            if(this_employee.position.casefold() == "Busser"):
                self.total_points+=5

            print(f"{this_employee.name:<17}{this_employee.position:<17}{this_employee.netsale:<17}{this_employee.cashtips:<17}{this_employee.cctips:<17}{this_employee.gratuity:>13}") 

        if self.total_points == 0:
            print("Total points is 0. Can't compute.")
            return

        cash_pv = totalcash/self.total_points
        cc_pv = totalcctips/self.total_points
        grat_pv = totalgrat/self.total_points

        #computing server tipout
        server_payout = (cash_pv*self.SERVER_PV) + (cc_pv*self.SERVER_PV) + (grat_pv*self.SERVER_PV)

        runner_payout = (cash_pv*self.RUNNER_PV) + (cc_pv*self.RUNNER_PV) + (grat_pv*self.RUNNER_PV)
        
        expo_payout = (cash_pv*self.EXPO_PV) + (cc_pv*self.EXPO_PV) + (grat_pv*self.EXPO_PV)

        busser_payout = (cash_pv*self.BUSSER_PV) + (cc_pv*self.BUSSER_PV) + (grat_pv*self.BUSSER_PV)

        kithost_payout = (cash_pv*self.KITCHEN_HOST_PV) + (cc_pv*self.KITCHEN_HOST_PV) + (grat_pv*self.KITCHEN_HOST_PV)

       


      

        
        print(f"\n{35*'-'} Tip Out {35*'-'}\n")

        print(f"{'Employee':<17}{'Cash Tips':>15}{'CC Tips':>15}{'Gratuity':>15}")

        print(f"{'Servers':<17}{cash_pv*self.SERVER_PV:>15.2f}{cc_pv*self.SERVER_PV:>15.2f}{grat_pv*self.SERVER_PV:>15.2f}")
        print(f"{'Runner':<17}{cash_pv*self.RUNNER_PV:>15.2f}{cc_pv*self.RUNNER_PV:>15.2f}{grat_pv*self.RUNNER_PV:>15.2f}")
        print(f"{'Expo':<17}{cash_pv*self.EXPO_PV:>15.2f}{cc_pv*self.EXPO_PV:>15.2f}{grat_pv*self.EXPO_PV:>15.2f}")
        print(f"{'Busser':<17}{cash_pv*self.BUSSER_PV:>15.2f}{cc_pv*self.BUSSER_PV:>15.2f}{grat_pv*self.BUSSER_PV:>15.2f}")
        print(f"{'Kitchen/Host':<17}{cash_pv*self.KITCHEN_HOST_PV:>15.2f}{cc_pv*self.KITCHEN_HOST_PV:>15.2f}{grat_pv*self.KITCHEN_HOST_PV:>15.2f}")


        
