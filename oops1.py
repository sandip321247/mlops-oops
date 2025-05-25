#initate  a class
class Employee:
    # special method / magic method / dunder method to initialize the object - constructor
    def  __init__(self):
        print("started exceuting attribute/data")
        self.id =  123
        self.salary = 50000
        self.designation = "Software Engineer"
        print(" exceuting attribute/data initiated")

    def travel(self,destination):
        print("this travel function is called manually")
        return f"Employee is traveling to {destination} for work."

# create an object of the class
emp = Employee()
# access the attributes of the object
# print(emp.id)          # Output: 123
# print(emp.salary)      # Output: 50000
# print(emp.designation) # Output: Software Engineer
emp.travel("New York")  # Call the method
# Output: Employee is traveling to New York for work.
sam = emp.travel("New York")
print(sam)

