class MagicalContact:  
    def __init__(self, name, email, phone, trait):  
        self.name = name  
        self.email = email  
        self.phone = phone  
        self.trait = trait  
        self.traits = ["brave", "wise", "loyal", "cunning"]  
        self.houses = ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]   

    def __repr__(self):  
        return f"Wizard(name='{self.name}', email='{self.email}', phone='{self.phone}')"  

    def get_house(self):  
        if self.trait == self.traits[0]:  
            return self.houses[0]  # Gryffindor  
        elif self.trait == self.traits[1]:  
            return self.houses[1]  # Hufflepuff  
        elif self.trait == self.traits[2]:  
            return self.houses[2]  # Ravenclaw  
        elif self.trait == self.traits[3]:  
            return self.houses[3]  # Slytherin  
        else:  
            return None   

    def my_function(self):  
        print(self.name, self.trait)  
        house = self.get_house()  
        print(f"House: {house}")  
        return house   

class WandFactory:  
    @staticmethod  
    def create_wand(student: MagicalContact):  
        house = student.get_house()  
        if house == "Gryffindor":  
            print("Wand made of holly")  
        elif house == "Hufflepuff":  
            print("Wand made of walnut")  
        elif house == "Ravenclaw":  
            print("Wand made of wood")  
        elif house == "Slytherin":  
            print("Wand made of green wood")  
        else:  
            print("No wand for unrecognized house")   

class Wizard:  
    def __init__(self):  
        self.students = []  

    def add_student(self, name, email, phone, trait):  
        new_student = MagicalContact(name, email, phone, trait)  
        self.students.append(new_student)  
        print(f"Wizard '{new_student}' added.")  

    def list_students(self):  
        if not self.students:  
            print("No Wizards available.")  
        else:  
            print("List of Wizards:")  
            for student in self.students:  
                print(student)  

manager = Wizard()  

while True:  
    name = input("Enter name (or type 'exit' to finish): ")  
    if name.lower() == 'exit':  
        break  

    trait = input("Enter student trait (brave/wise/loyal/cunning): ")  
    valid_traits = ["brave", "wise", "loyal", "cunning"]  
    if trait not in valid_traits:  
        print("Invalid trait! Please enter one of the following: brave, wise, loyal, cunning.")  
        continue   

    email = input("Enter email: ")  
    phone = input("Enter phone number: ")  

    manager.add_student(name, email, phone, trait)  
    new_student = MagicalContact(name, email, phone, trait) 
    new_student.my_function()  
    WandFactory.create_wand(new_student)  

manager.list_students()
