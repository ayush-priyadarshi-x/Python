class volunteer: 
    def __init__(self, name, age, occupation):
        self.name = name
        self.age = age
        self.occupation = occupation
    def show(self): 
        print(f"Volunteer \n\t Name : {self.name} \n\t Age : {self.age} \n\t occupation : {self.occupation}")

class sportsMen: 
    age = 19 
    sport = "Football"
    def showSportsMen(self): 
        print(f"Sports Men \n\t age : {self.age} \n\t sport : {self.sport}")


class studentVolunteer(volunteer, sportsMen): 
    occupation = "Student"
    sport = "Cricket"
    def showStudent(self): 
        print(f"Student \n\t Name : {self.name} \n\t age : {self.age} \n\t occupation : {self.occupation}")



ayush = studentVolunteer("Ayush", 17)