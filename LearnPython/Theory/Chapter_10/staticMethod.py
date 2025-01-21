class Employee : 
    language = "python"
    salary = 10 
    
    def getInfo(self): 
        print(f"Language : {self.language} \n Salary : {self.salary}")
    
    @staticmethod
    def getInfoStatic(language, salary): 
        print(f'Language : {language} \n Salary : {salary}')
    

harry = Employee()
print(harry)

harry.getInfo()
harry.salary = 10 * 10
harry.getInfoStatic(harry.language, harry.salary)