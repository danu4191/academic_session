from __init__ import  Account
#acount ki lists k lye aik empty list bnain
#aap is mn jetna mrzi accounts bnaate jain baad mn agr aap ne in mn 
#changement krni hai tou sirf us ko us k index number aur us ki mutaliqa changement se function call krna hai 
account_list=[]
a1=Account('jazzcash','03020874092','Muhammad Adnan',20000,'danubhai')
account_list.append(a1)
a2=Account('easypaisa','03020874092','Muhammad Adnan',10000,'medimrzi')
account_list.append(a2)
a3=Account('nayapay','03020874092','Muhammad Adnan',16000,'galhi run(gr)')
account_list.append(a3)
a4=Account('sadapay','03020874092','Muhammad Adnan',125000,'crush')
account_list.append(a4)
account_list[0].show()
account_list[1].show()
account_list[2].show()
account_list[3].show()
print()


#agr alag alag krn ge tou woh pehle waali info bhi de ga aur recent bhi 
#lakin agr uper hi likh dn aur function call krwain tou woh sirf rcent detail de ga 
account_list[0].deposit(500,'danubhai')
account_list[1].deposit(500,'medimrzi')
account_list[2].withdraw(1000,'galhi run(gr)')
account_list[2].deposit(4000,'galhi run(gr)')
account_list[2].deposit(1000,'galhi run(gr)')
account_list[3].withdraw(900,'crush')
account_list[0].show()
account_list[1].show()
account_list[2].show()
account_list[3].show()
print()