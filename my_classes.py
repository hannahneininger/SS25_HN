class Person():
    def __innit__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        

class Subject(Person):
    super.init__ = Person.__init__
    def __innit__(self, sex, age, date_of_birth):
        self.sex = sex
        self.age = age
        self.__date_of_birth = date_of_birth

    def estimate_max_hr(self):
        if self.sex == "male":
            max_hr_bpm = 223 - 0.9 * self.age
        elif self.sex == "female":
            max_hr_bpm = 226 - 1.0 * self.age
        else:
        # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
            max_hr_bpm = input("Enter maximum heart rate:")
        return int(max_hr_bpm)
    
        
class Supervisor(Person):
    super.init__ = Person.__init__
    pass

class Experiment():
    def __innit__(self, experiment_name, date, supervisor):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
    

    def add_subject(self,subject):
        self.subject = subject
        return subject
    
    def add_supervisor(self,supervisor):
        self.supervisor = supervisor
        return supervisor
    

