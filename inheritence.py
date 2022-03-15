class Student(object):
    def __init__(self,name,rollno,admno,clg):
        self.name=name
        self.rollno=rollno
        self.admno=admno
        self.clg=clg

    def displayDetails(self):
        print(self.name+"\n"+self.rollno+"\n"+self.admno+"\n"+self.clg)

class Exam(Student):
    def __init__(self,name,rollno,admno,clg,examname,englishmarks,mathsmarks,chemistrymarks,physicsmarks):
        self.examname=examname
        self.englishmarks=englishmarks
        self.mathsmarks=mathsmarks
        self.chemistrymarks=chemistrymarks
        self.physicsmarks=physicsmarks

        Student.__init__(self,name,rollno,admno,clg)


    def printDetails(self):
        print("name =", self.name)
        print("rollno =", self.rollno)
        print("admno =", self.admno)
        print("clg =", self.clg)
        print("examname =", self.examname)
        print("englishmarks =", self.englishmarks)
        print("mathsmarks =", self.mathsmarks)
        print("chemistrymarks =", self.chemistrymarks)
        print("physicsmarks =", self.physicsmarks)

x = Exam("sri","960","1191","East point","Finalexams","93","85","88","90")
x.printDetails()
x.displayDetails()
