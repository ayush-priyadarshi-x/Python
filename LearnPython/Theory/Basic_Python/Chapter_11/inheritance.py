# Old way 
# class Employee: 
#     company = "Tesla"
#     language = "Python"

#     def show(self): 
#         print(f"The information about self is {self.company} {self.language}")

# class Programmar: 
#      company = "Tesla"
#      language = "Python"

#      def show(self): 
#         print(f"The information about self is {self.company} {self.language}")

#      def changeLanguage(self, language): 
#          previousLang = self.language
#          self.language = language
#          print(f"The language changed from : {previousLang} \t to : {self.language} ")


# New way 
class Employee: 
    company = "Tesla"
    language = "Python"

    def show(self): 
        print(f"The information about self is {self.company} {self.language}")

class Programmar(Employee): 
     company= "TCS"

     def changeLanguage(self, language): 
         previousLang = self.language
         self.language = language
         print(f"The language changed from : {previousLang} \t to : {self.language} ")


a = Employee()
b = Programmar()

print(f"For Employee : {a.show()}")
print(f"For Programmar : {b.show()}")
