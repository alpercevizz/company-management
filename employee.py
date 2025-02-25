import json
from abc import ABC, abstractmethod

# Soyut Sınıf

class EmployeeBase(ABC):
    def __init__(self, emp_id, name, age, email, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.email = email
        self.__salary = salary

    @abstractmethod
    def show_informations(self):
        pass

    def update_salary(self, new_salary):
        if new_salary > 0:
            self.__salary = new_salary
            print(f"{self.name}'s salary is updated: {self.__salary} TRY")
        else:
            print("Salary cannot be negative!")

    def to_dict(self):
        """Çalışan bilgilerini json'a çevirmek"""

        return {
            "emp_id": self.emp_id,
            "name": self.name,
            "age": self.age,
            "email": self.email,
            "salary": self.__salary
        }
    
# Genel Çalışan Sınıfı

class Employee(EmployeeBase):
    def show_informations(self):
        print(f"ID: {self.emp_id}, Name: {self.name}, Age: {self.age}, Email: {self.email}")
        
# Yönetici Sınıfı

class Manager(Employee):
    def __init__(self, emp_id, name, age, email, salary, department):
        super().__init__(emp_id, name, age, email, salary)
        self.department = department
    
    def show_informations(self):
        super().show_informations()
        print(f"Department: {self.department}")

# Yazılımcı Sınıfı

class Developer(Employee):
    def __init__(self, emp_id, name, age, email, salary, programming_langugage):
        super().__init__(emp_id, name, age, email, salary)
        self.programming_language = programming_langugage

