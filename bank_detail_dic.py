from __init__ import  Account
dic={}
account_number=0
a1=Account('jazzcash','03020874092','Muhammad Adnan',20000,'danubhai')
jazzcash=account_number
dic[jazzcash]=a1
account_number=account_number+1


a2=Account('easypaisa','03020874092','Muhammad Adnan',10000,'medimrzi')
easypaisa=account_number
dic[easypaisa]=a2
account_number=account_number+1

a3=Account('nayapay','03020874092','Muhammad Adnan',16000,'galhi run(gr)')
nayapay=account_number
dic[nayapay]=a3
account_number=account_number+1

a4=Account('sadapay','03020874092','Muhammad Adnan',125000,'crush')
sadapay=account_number
dic[sadapay]=a4
account_number=account_number+1


dic[jazzcash].show()
dic[easypaisa].show()
dic[nayapay].show()
dic[sadapay].show()
print()

#aap ne invalid info nhai deni agr dn ge tou woh us k mutabiq us ko deal kre ga jo us info di gye hai 

dic[jazzcash].deposit(1000,'danubhai')
dic[easypaisa].withdraw(2000,'dan')
dic[nayapay].deposit(1000,'galhi run(gr)')
dic[sadapay].deposit(-500,'danubhai')


dic[jazzcash].show()
dic[easypaisa].show()
dic[nayapay].show()
dic[sadapay].show()
print()