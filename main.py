from Employee import Employee
from Report import Report
from time import sleep

def main():
   
    employees = []

    while(True):

        employeeadd = input("Create new employee? (y/n)")

        if(employeeadd == 'y'):
            name = input("Name:  ")
            position = input("Position:  ")
            netsale = float(input("NetSale:  "))
            cctips = float(input("Credit Card tips:  "))
            cashtips = float(input("Cash Tips:  "))
            grat = float(input("Gratuity:  "))
            sleep(1)
            print(f"SUCCESS {name} has been added to the Report!")

            print("")
            
            emp = Employee(netsale, name, cctips, grat, cashtips, position)
            employees.append(emp)
        else:
            break
    
    report1 = Report(employees, 27)
    report1.compute()
        
   

if __name__ == '__main__':
    main()

