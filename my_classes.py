class Subject():
    def __innit__(self, name):
    def estimate_max_hr():
    
        
class Supervisor():
    def __innit__(self, name):


class Experiment():
    def __innit__(self, experiment_name, date, supervisor, subject):
        self.experiment_name = experiment_name
        self.date = date
        self.supervisor = supervisor
        self.subject = subject

class Person():
    def __innit__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def estimate_max_hr(self):
       if self.sex == "male":
        max_hr_bpm = 223 - 0.9 * age
    elif sex == "female":
        max_hr_bpm = 226 - 1.0 * age
    else:
        # der input() öffnet ein Eingabefenster für den Nutzer und speichert die Eingabe
        max_hr_bpm = input("Enter maximum heart rate:")
    return int(max_hr_bpm)
class Subject(Person):
    def __innit__(self, name, age):
        self.name = name
        self.age = age
class Examiner(Person):
    def __innit__(self, name, age):
        self.name = name
        self.age = age

