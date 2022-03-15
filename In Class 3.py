class Person:
    # Set the main variable
    def __init__(self, name):
        self.name = name

    # Set the other variables
    def input_person_data(self, age, weight, height):
        self.age = age
        self.weight = weight
        self.height = height

    # Set the output content
    def get_person_data(self):
        print("name:", self.name)
        print("age:", self.age)
        print("weight:", self.weight)
        print("height:", self.height)

    # Set the data input
def main():
    p1 = Person("Yang")
    p2 = Person("Zhao")
    p1.input_person_data(21, "80", "175")
    p2.input_person_data(20, "70kg", "182")
    p1.get_person_data()
    p2.get_person_data()

# Output the result
if __name__ == '__main__':
    main()
