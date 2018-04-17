class employee:
    no_of_emps=0
    emp_raise=1.04

    def __init__(self,name,age,pay):
        self.name=name
        self.age=age
        self.email=name+age+'@company.com'
        self.pay=pay
        employee.no_of_emps += 1
        

    def emp_raisE(self):
        self.pay=self.pay*self.emp_raise

    def increment(self,x=emp_raise):
        self.emp_raise = x
        self.emp_raisE()

    def throw(self):
        #return 'name:{} \nage:{} \nemail:{} \npay:{}'.format(self.name,self.age,self.email,self.pay)
        print self.pay


varun=employee('Varun','23',40000)
downey=employee('Downey','50',70000)

#print(varun.throw())
#print(downey.throw())
varun.throw()
varun.increment(3)
#varun.emp_raisE(varun.pay)
varun.throw()

#varun.emp_raisE()
#print(varun.emp_raise)
#print(employee.emp_raise)

print("Total emps:%d"%varun.no_of_emps)
        

        


