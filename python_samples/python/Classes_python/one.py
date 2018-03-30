class employee:
    def __init__(self):
        self.name='user'
        self.age=999

    def second_init(self):
        xx=0
        print("done:")

    def setmethod(self,name,age):
        self.name=name
        self.age=age
        self.mail=name + str(age) + '@company.com'
    
    def getmethod(self):
        xx+=1
        return (self.name,self.age,self.mail,xx)

x=employee()
x.second_init()
x.setmethod('hari',17)
for each in x.getmethod():
    print(each)

        
