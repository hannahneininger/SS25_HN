
class Sensor():
    """
    A sensor class that represents a sensor
    """
    #Konstruktor
    def _init_(self, id):
        self.id = id
        self.messwert = None
        self.messwerte = []
        self.__passwort = "123456" #tut dann so als gäbe es das Attribut nicht( versteckt), ausgabe wie unten (im dictl. kommt es trotzdem)
    
    def measure(self, messwert): 
        self.messwert = messwert
        self.messwerte.append(messwert)

    def calc_mean(self):
        self.mittelwert = sum(self.messwerte)/len(self.messwerte)
        return self.mittelwert #direkt zurückgeben
    
    def get_passwort(self, superpasswort):
        if superpasswort =="bier":
            return self.__passwort 
        
    def set_passwort(self, superpasswort, neues_passwort):
        if superpasswort =="bier":
            self.__passwort = neues_passwort
    
    def reset(self, passwort):
        if passwort == self.__passwort: 
            print("auf werkseinstellungen")
            self.messwert=None
            self.messwerte=[]
        else:
            print ("Falsches Passwort!") 

if __name__ == "_main_":
    s1= Sensor("123") #123 ist die id       
    print(s1.id)
    s1.measure(10)
    s1.measure(20)
    s1.measure(30)
    print(s1.messwerte)
    s1.calc_mean()
    print(s1.calc_mean())
    das_passwort=s1.get_passwort("bier")
    print(das_passwort)
    print(s1._dict_) #ein Dictionary mit allen Attributen (nicht Methoden) von Objekten, automatisch bei Klassen
    s1.reset(das_passwort)


class HR_sensor(Sensor):
    # hier ist kein Konstruktor 
    def calc_hrv(self):
        print('die HRV ist 60')

if __name__ == "_main_":
    s1=Sensor('1234')
    print(s1.id)

    s2=HR_sensor("2345")
    print(s2.id)
    s2.calc_hrv()

    


