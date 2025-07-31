class Employees:
    company_name="capgemeini"
    
    def employee_details(self,name,emp_id,city,salary):
        self.name=name
        self.emp_id=emp_id
        self.city=city
        self.salary=salary
    
    def show_details(self):
        print(self.name,self.emp_id,self.city,self.salary,self.company_name)
p1=Employees()
p2=Employees()
p3=Employees()
p4=Employees()

p1.employee_details('abhi',36,'hyd','70k')
p2.employee_details('nani',37,'hyd','80k')
p3.employee_details('vig',38,'hyd','170k')
p4.employee_details('dev',39,'hyd','270k')

p1.show_details()
p2.show_details()
# p3.company_name='Tcs'
# p4.company_name='Tcs'
p3.show_details()
p4.show_details()
print(p1.name)
print(p2.name)
print(p1.city,p2.city,p3.city,p4.city)
print(p1.company_name,p2.company_name,p3.company_name,p4.company_name)

print(Employees.company_name)

















