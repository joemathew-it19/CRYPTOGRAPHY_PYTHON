class student:
    __rollnumber=[]
    __name=[]
    __maths=[]
    __physics=[]
    __che=[]
    __eng=[]
    __cp=[]
    __cgpa=[]
    __total=[]
    __mailid=[]
    __phonenum=[]
    
    def getdata(self):
        self.p=int(input(("ENTER HOW MANY NO OF STUDENTS YOU NEED TO GENERATE REPORT")))
        for x in range(self.p):
            self.__rollnumber.append(str(input("ENTER THE ROLL NUMBER")))
            self.__name.append(str(input("ENTER THE NAME OF THE STUDENT")))
            self.__mailid.append(str(input("ENTER THE MAIL-ID OF THE STUDENT")))
            self.__phonenum.append(str(input("ENTER THE PHONE NUMBER OF THE STUDENT")))
            self.__maths.append(float(input("ENTER THE MATHS MARK")))
            self.__physics.append(float(input("ENTER THE PHYSICS MARK")))
            self.__che.append(float(input("ENTER THE CHEMISTRY MARK")))
            self.__eng.append(float(input("ENTER THE ENGLISH MARK")))
            self.__cp.append(float(input("ENTER THE COMPUTER SCIENCE MARK")))
    def display(self):
        print("--------------------------------------------------------------------------------------------------------------------------------")
        print("                                  STUDENT DETAILS AND THIER MARKS                                                               ")
        print("--------------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        print("********************************************************************************************************************************")
        print("ROLL NUMBER\t\tNAME\t\tMAIL-ID\t\tPHONENUMBER\t\tMATHS\t\tPHYSICS\t\tCHEMISTRY\t\tENGLISH\t\tCOMPUTERSCIENCE")
        for x in range(self.p):
            print(self.__rollnumber[x],"\t","\t",self.__name[x],"\t","\t",self.__mailid[x],"\t","\t",self.__phonenum[x],"\t""\t",self.__maths[x],"\t""\t",self.__physics[x],"\t""\t",self.__che[x],"\t","\t",self.__eng[x],"\t","\t",self.__cp[x])
        
        print("********************************************************************************************************************************")    
            
    def report(self):
        for x in range(self.p):
            self.__total.append(self.__maths[x]+self.__physics[x]+self.__che[x]+self.__eng[x]+self.__cp[x])
        for x in range(self.p):
            y=0
            m=0
            y=self.__total[x]/500*10
            self.__cgpa.append(y)
        print("----------------------------------------------------------------------------------------------------------------------------------")
        print("                                         OVERALL FINAL RESULT                                                                     ")
        print("-----------------------------------------------------------------------------------------------------------------------------------")
        print("ROLL NUMBER \t\t NAME \t\t MAILID \t\t PHONENUMBER \t\t CGPA")
        for x in range(self.p):
            print(self.__rollnumber[x],"\t\t\t",self.__name[x],"\t\t\t",self.__mailid[x],"\t\t",self.__phonenum[x],"\t\t",self.__cgpa[x])
            
            
        
            
   
      
print("********************************BANNARI AMMAN INSTITUDE OF TECHNOLOGY **********************************************************")
print("\n")
print("--------------------------------------------------------------------------------------------------------------------------------")
print("                                REPORT CART GENERATOR                                                                           ")
print("--------------------------------------------------------------------------------------------------------------------------------")
print("\n")
a=student()
a.getdata()
print("click the option ")
for i in range(100):

    print("1. DISPLAY THE FETCHED DATA \t\t 2. DISPLAY THE FINAL REPORT \t\t  3.EXIT ")
    r=int(input("ENTER THE OPTION "))
    if r==1:
        a.display()
    elif r==2:
         a.report()
    elif r==3:
         break
