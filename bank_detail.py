from __init__ import  Account

#my jazzcash accountinfo 
a1=Account('jazzcash','03020874092','Muhammad Adnan',20000,'danubhai')
a1.deposit(1000,'danubhai')
a1.withdraw(500,'danubhai')
a1.getBalance('danubhai')
print(a1.account_holder)
a1.account_holder='Allah Wasaya'

a1.show()

#jb jb hum naya account btain ge woh naye ki detail deta jaye ga 
#aap hr account ki raqam niklwana dalna alag alag kr skte hn aur pasward ka 
#thk hona laazmi hai 

#my easypaisa account info
a2=Account('easypaisa','03020874092','Muhammad Adnan',10000,'medimrzi')
a2.deposit(2000,'medimrzi')
a2.deposit(2500,'medimrzi')
a2.withdraw(500,'medimrzi')
a2.getBalance('medimrzi')


#yahn pr mn ne apna pasward change kya hai aap pichle code mn changement kye bghair getter aur 
#setter method se change kr skte hn hr class mn tabdeeli kr skte hn 
print(a2.password)
a2.password='dani'
a2.deposit(2000,'dani')

a2.show()

#my nayapay account info
a3=Account('nayapay','03020874092','Muhammad Adnan',16000,'galhi run(gr)')
a3.deposit(2500,'galhi run(gr)')
a3.withdraw(2000,'galhi run(gr)')
a3.show()

#my sadapay account info
a4=Account('sadapay','03020874092','Muhammad Adnan',125000,'crush')
a4.deposit(2500,'crush')
a4.withdraw(2000,'crush')
a4.show()

#user se info le kr account bnanan

#ye user se input lene se hi account bne ga so is ko jb mn use krn ga is 
#uncomment kr dn ga 

# tittle=input(' account_tittle:')
# holder=input(' account_holder:')
# number=input(' account_number:')
# balance=input('balance')
# balance=int(balance)
# pasward=input('pasward:')
# a5=Account(tittle,holder,number,balance,pasward)
# a5.deposit(1000,pasward)
# my_baance=a4.getBalance(pasward)
# print()
# print(balance)

# a5.deposit(1000,'adnan')
# a5.show()

#pehle account mn paise jamma krwaye hn mn ne ab naya balnce kuch u ho ga 

#aap agr ghalat info dn ge tou kuch output us k mutabiq aye gi jis trah ap ne 
#set ki ho gi 

a1.deposit(1000,'hdghg')
a1.withdraw(-4000,'danubhai')
a1.withdraw(1000000,'danubhai')
a1.getBalance('dafhh')

# jb bhi hum ye print ko call krn ge tou ye sab detil de ga jitne bhi account bnain hn 
#agr ye nhai dn ge tou jo most recent call function ho ga us ki sirf detail de ga


print()
