#polymorphism ka mtlb hai k aik hi chez ka aik se zyada kaam krna jis trah yaha + 2 integersko add krti hai tou un ka sum math k mutabiq likh deta hai lakin jb ye strings pr lagate hn tou woh un do strings ko aik sath likh dete hn 
#EXAMPLE#1

a=10
b=20
print(a+b)
a='Muhammad '
b='Adnan'
print(a+b)

#Example #2

class pakistani:
    def __init__(self,name):
        name=self.name=name
    def speak(self):
       
        print('1-Urdu:\n',self.name,'is the national language of pakistan. When people ask about you they say \n '
        'kya haal hn jaani kya kr rhe ho ')

class upper_punjab(pakistani):
    def __init__(self,name):
        name=self.name=name
    def speak(self):
      
        print('2-punjabi:\n In upper punjab people speak',self.name,'and when they ask about you the say \n'
        'ki haal ne tere ki krna aa ')

class lower_punjab(pakistani):
    def __init__(self,name):
        name=self.name=name
    def speak(self):
        print('3-Saraiki \n',self.name,'is one of the most popular language in the world .It is sweet language when people ask about you the say \n wee aa sohnra kithan reh gain tabyat kewe he hee kadok da nizrya kainwi jaani khair howe chandr bnr gye khud ')



a1=pakistani('urdu')
a2=upper_punjab('punjabi')
a3=lower_punjab('saraiki')
list=[a1,a2,a3]
for b in list:
    b.speak()
