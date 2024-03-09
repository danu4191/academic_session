class students:
    def __init__(self,serial_no,name,cnic,age,roll_no,school,marks):
        self.serial_no=serial_no
        self.name=name
        self.cnic=cnic
        self.age=age
        self.roll_no=roll_no
        self.school=school
        self.marks=marks
    def behaviour(self):
        print(self.serial_no)
        print(self.name)    
        print(self.cnic)    
        print(self.age)    
        print(self.roll_no)    
        print(self.school)    
        print(self.marks)


class family:
    def __init__(self,a,b,c,d):
        self.father_name=a
        self.father_oocupation=b
        self.father_income=c
        self.family_members=d
    def behaviour(self):
        print(self.father_name)
        print(self.father_oocupation)
        print(self.father_income)
        print(self.family_members)

 



class Account():
    def __init__(self,account_tittle,account_number,account_holder , balance, password):
        self.account_tittle=account_tittle
        self.account_number=account_number
        self.account_holder=account_holder       
        self.balance = int(balance)
        self.password = password
    def deposit(self, amountToDeposit, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        if amountToDeposit < 0:
            print('You cannot deposit a negative amount')
            return None
        self.balance = self.balance + amountToDeposit
        return self.balance
    def withdraw(self, amountToWithdraw, password):
        if password != self.password:
            print('Incorrect password for this account')
            return None
        if amountToWithdraw < 0:
            print('You cannot withdraw a negative amount')
            return None
        if amountToWithdraw > self.balance:
            print('You cannot withdraw more than you have in your account')          
            return None
        self.balance = self.balance - amountToWithdraw
        return self.balance
    def getBalance(self, password):
        if password != self.password:
            print('Sorry, incorrect password')
            return None
        return self.balance

          

    def show(self):
        print(' account_tittle:',self.account_tittle)
        print(' account_number:',self.account_number)
        print(' account_holder:',self.account_holder)       
        print(' Balance:', self.balance)
        print(' Password:', self.password)
 
        print()






def subj_avg(*dani):
    sum=0
    for a in dani:
        sum=sum+a
    avg=sum/len(dani)
    print(avg)
  
def sum(a,b):
    '''this will add two numbers'''
    return a+b
# print(sum(9,3))  
# print(sum.__doc__)  



class university:
    __uni_name=input('What is you university name:\n')
    __location=input('write the location of your university:\n')
    __rank=input('write the rank of our university:\n')
    __established=input('when was your university was made:\n')
    def uni_info(self):
        print('My university name is',self.__uni_name,'It is the one of the largest university of the pakistan and its rank in pakistan is ',self.__rank,'it is located in ', self.__location,'in Punjab ,pakistan.The Islamia University of Bahawalpur is a public university  Founded in 1925 as a religious institution, the university was renamed and opened up to secular candidates in' ,self.__established )
class departs(university):
    __dep1_name=input('write you any depart in IUB:\n ')
    __dep1_faculities=input('write  facilities in you depart:\n')
    def education_depart(self):
        print('The reason for which a university is made is its ',self.__dep1_name, 'Which is the main part of the uni ',self.__dep1_name,'is the charm of any university',self.__dep1_name,'has charm due to students .It should have many facilities like',self.__dep1_faculities )
    
my_uni_dep=departs()
my_uni_dep.uni_info()
my_uni_dep.education_depart()