class university:
    __uni_name=input('What is you university name:\n')
    __location=input('write the location of your university:\n')
    __rank=input('write the rank of our university:\n')
    __established=input('when was your university was made:\n')
    def uni_info(self):
        print('ISLAMIA UNIVERSITY OF BAHAWALPUR')
        print('My university name is',self.__uni_name,'It is the one of the largest university of the pakistan and its rank in pakistan is ',self.__rank,'it is located in ', self.__location,'in Punjab ,pakistan.The Islamia University of Bahawalpur is a public university  Founded in 1925 as a religious institution, the university was renamed and opened up to secular candidates in' ,self.__established )

class departs(university):
    
    __dep1_name=input('write you any depart in IUB:\n ')
    __dep1_faculities=input('write  facilities in you depart:\n')
    def education_depart(self):
        print('\n 1-ACADEMIC DEPART')
        print('The reason for which a university is made is its ',self.__dep1_name, 'Which is the main part of the uni ',self.__dep1_name,'is the charm of any university',self.__dep1_name,'has charm due to students .It should have many facilities like',self.__dep1_faculities )

    __dep2_name=input('Write another depart name:\n ')
    __dep2_location=input('write your depart location in which campus is its main branch:\n ')
    __dep2_purpose=input('write the purpose of this depart in your own words:\n ')

    def admission_cell(self):
        print('\n 2-ADMISSION CELL')
        print('one of the depart which is also the main part of the university or any other institute is the ',self.__dep2_name,'. About all the campuses have an admission cell but the main admission cell is in ',self.__dep2_location,self.__dep2_purpose)

    __dep2_name=input('2nd major dep:\n')
    __dep2_head=input('head name:\n')
    def dsa(self):
        print(' \n 3-DIRECTORATE OF STUDENTS AFFAIRS DEPART')
        print('for students affairs it has',self.__dep2_name,'.It is most important for an instute to run because where some people are present there are chances of ueerl among them .So,there should be a depart which resolve all the problems of the students so ',self.__dep2_name,' is necessary for this .whose head is',self.__dep2_head,'who control whole the problems')




my_uni_dep=departs()
my_uni_dep.uni_info()
my_uni_dep.education_depart()
my_uni_dep.admission_cell()
my_uni_dep.dsa()

