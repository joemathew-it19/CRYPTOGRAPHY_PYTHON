class student_worker:
    __teachernumber=[]
    __teachername=[]
    __subjecttaking=[]
    __workernumber=[]
    __workerid=[]
    __workername=[]
    __workerdept=[]
    __workerphonenum=[]
    __teachermailid=[]
    __teacherphonenum=[]
    
    def getdata1(self):
        self.p=int(input(("ENTER HOW MANY NO OF TEACHER YOU NEED TO GENERATE REPORT:")))
        for x in range(self.p):
            self.__teachernumber.append(str(input("ENTER THE ID:")))
            self.__teachername.append(str(input("ENTER THE NAME OF THE TEACHER:")))
            self.__subjecttaking.append(str(input("ENTER THE SUBJECT TAKING  OF THE TEACHER:")))
            self.__teachermailid.append(str(input("ENTER THE MAIL-ID OF THE TEACHER:")))
            self.__teacherphonenum.append(str(input("ENTER THE PHONE NUMBER OF THE TEACHER:")))
        print("\n")
            
    def getdata2(self):
        self.p=int(input(("ENTER HOW MANY NO OF WORKERS YOU NEED TO GENERATE REPORT:")))
        for x in range(self.p):
            self.__workerid.append(str(input("ENTER THE WORKER NUMBER:")))
            self.__workername.append(str(input("ENTER THE NAME OF THE WORKER:")))
            self.__workerdept.append(str(input("ENTER THE WORKING PLACE OF THE WORKER:")))
            self.__workerphonenum.append(str(input("ENTER THE PHONENUMBER OF THE WORKER:")))
        print("\n")

    def display1(self):
        
        print("--------------------------------------------------------------------------------------------------------------------------------")
        print("                                  TEACHER DETAILS                                                             ")
        print("--------------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        print("********************************************************************************************************************************")
        print("ID\t\tNAME\t\t\SUBJECT\t\t\tMAIL-ID\t\t\tPHONENUMBER")
        for x in range(self.p):
            print(self.__teachernumber[x],"\t","\t",self.__teachername[x],"\t","\t",self.__subjecttaking[x],"\t","\t",self.__teachermailid[x],"\t","\t",self.__teacherphonenum[x])
        
        print("********************************************************************************************************************************")
        print("\n")
         
        
    
        
 

    def display2(self):
        print("--------------------------------------------------------------------------------------------------------------------------------")
        print("                                  WORKER DETAILS                                                             ")
        print("--------------------------------------------------------------------------------------------------------------------------------")
        print("\n")
        print("********************************************************************************************************************************")
        print("WORKERID\t\tWORKERNAME\t\tWORKERDEPT\t\tWORKERPHONENUMBER")
        for x in range(self.p):
            print(self.__workerid[x],"\t","\t","\t",self.__workername[x],"\t","\t","\t",self.__workerdept[x],"\t","\t","\t","\t",self.__workerphonenum[x])
        
        print("********************************************************************************************************************************")
        print("\n")
            
        
            
   
      
print("********************************BANNARI AMMAN INSTITUTE OF TECHNOLOGY **********************************************************")
print("\n")
print("--------------------------------------------------------------------------------------------------------------------------------")
print("                                TEACHER AND WORKER DETAILS                                                                      ")
print("--------------------------------------------------------------------------------------------------------------------------------")
print("\n")
a=student_worker()
a.getdata1()
a.getdata2()
print("click the option ")
for i in range(1000):

    print("1.Display the Teacher details \t \t 2. Display the worker details \t \t 3. Both Teacher and worker \t \t 4.exit ")
    r=int(input("ENTER THE OPTION: "))
    if r==1:
        a.display1()
    elif r==2:
         a.display2()
    elif r==3:
        a.display1()
        a.display2()
    elif r==4:
         break
