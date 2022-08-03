class Patient:
    def __init__(self, age, sex, diagnosis):
        self.age = age
        self.sex = sex
        self.diagnosis = diagnosis

    def admit_dx(self):
        print(f"The ICD-10 admitting diagnosis of this {self.age} year old {self.sex} is {self.diagnosis} ")

    def adult(self):
        if self.age > 18:
            return True
        else:
            return False


if __name__ == '__main__':
    john = Patient(56, "M", "J44.9")
    carol = Patient(78, "F", "I21.1")
    paul = Patient(89, "M", "M62.82")
    lillian = Patient(16, "F", "M84.459")

john.admit_dx()
carol.admit_dx()
paul.admit_dx()
lillian.admit_dx()

print("Checking if patient is an adult")
print(john.adult())
print(carol.adult())
print(paul.adult())
print(lillian.adult())