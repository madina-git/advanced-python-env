# Base class
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary  # private-like attribute (encapsulation)

    def get_salary(self):
        return self._salary

    def get_role(self):
        return "Employee"


# Child class
class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    # Polymorphism: override get_role
    def get_role(self):
        return "Manager"

    def get_bonus(self):
        return self.bonus


# Function to print roles and salaries
def print_employee_info(employee_list):
    for emp in employee_list:
        print(f"{emp.name} - Role: {emp.get_role()}, Salary: {emp.get_salary()}")


# --- Demonstration ---
emp1 = Employee("Nazgul", 50000)
emp2 = Manager("Medet", 80000, 15000)

employees = [emp1, emp2]
print_employee_info(employees)

# Optional: show bonus for managers
print(f"{emp2.name}'s bonus is {emp2.get_bonus()}")
