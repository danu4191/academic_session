# firt function define for dock string

def adnan(n):

    '''jb bhi hum koi function define krte hn tou agr string mn us ko call krain tou woh us ko utni dafa repeat kra d ga hn agr aap us ko integer mn call krat hn tou woh us ko multiply kr e ga us digit se jo likha gya hai '''

    print(n*2)
    print(n*4)
    
adnan(2)
adnan('2')    

# 2-----> 2nd function call for more detail 

def double(n:int)->int:
    '''jb ap int k lye function call krn tou woh just multiply kr deta hai '''
    print(n*3)
double(5)
help(double)


def double(n:str)->str:
    '''agr aap string k lye ye function call krte hn tou woh us ko multiply nhai krta bl k us ko utni dafa repeat kr deta hai jis int se multiply ho raha hota hai '''
    print(n*2)
double('5')

help(double)



def double(*n:int)->int:
    ''' agr aap aik se zyada parameters pass krn ge tou woh us ko multiply nhai kre ga chahe woh int hi q na ho bs woh us ko utni dafa repeat kre ga jis se multiply ho raha ho ga .'''
    print(n*3)
    #so is mn ye neeche wale 3 dafa repeat hn ge 
double(5,2,3)

help(double)
print(double.__doc__)

def list(my_list:list[str])->list[str]:
    
    '''yahan pr aap aik list ki bhi ducktype bna skte hn '''
    print([danu.replace('danu','gr') for danu in my_list])
list(['adnan','gr'])    
list('adnan')
help(list)

def dani(n):
    return n*2
print(dani(5))    