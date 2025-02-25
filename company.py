import json
from employee import Employee, Manager, Developer

class Company:
    def __init__(self, db_file = "database.json"):
        self.db_file = db_file
        self.employees = self.load_data()
    
    def load_data(self):
        """JSON dosyasında çalışanları yükler"""

        try:
            with open(self.db_file, "r", encoding="utf-8") as file:
                data = json.load(file)

                if isinstance(data, list):
                    return data
                else:
                    return []

        except (FileNotFoundError, json.JSONDecodeError):
            return []
        
    def save_data(self):
        """JSON dosyasına çalışanları kaydeder"""
        with open(self.db_file, "w", encoding="utf-8") as file:
            return json.dump(self.employees, file, ensure_ascii=False, indent=4)
    
    def add_employee(self, employee):
        """Yeni çalışan ekler"""

        self.employees.append(employee.to_dict())
        self.save_data()
        print(f"{employee.name} added succesfully!")
    
    def list_employees(self):
        """Tüm çalışanları listeler"""
        print("\n Employee List:")
        for emp in self.employees:
            print(f"ID: {emp['emp_id']}, Name: {emp['name']}, Age: {emp['age']}, Email: {emp['email']}")

            
    def update_salary(self, emp_id, new_salary):
        """Çalışan maaşını güncelle"""

        for emp in self.employees:
            if emp["emp_id"] == emp_id:
                emp["salary"] = new_salary
                self.save_data()
                print(f"Salary updated for {emp["name"]}: {new_salary} TRY")
                return
        print("Employee not found!")

    def delete_employee(self, emp_id):
        """Çalışanları ID'ye göre silme"""
        for emp in self.employees:
            if emp["emp_id"] == emp_id:
                self.employees.remove(emp)
                self.save_data()
                print(f"Employee with ID {emp_id} deleted successfully!")
                return
        print("Employee not found.")
    
    def search_employee(self, keyword):
        """İsme veya ID'ye göre arama"""

        found = False

        for emp in self.employees:
            if keyword.lower() in emp["name"].lower() or str(emp["emp_id"]) == str(keyword):
                print(f"Found employee: {emp}")
                found = True
        if not found:
            print("No employee found with given keyword!")
    
    def list_by_department(self, department):
        """Belirtilen departmandaki yöneticileri listeler"""

        print(f"\n Employees in {department} Department")

        for emp in self.employees:
            if "department" in emp and emp["department"].lower() == department.lower():
                print(f"ID: {emp['emp_id']}, Name: {emp['name']}, Email: {emp['email']}")

    def company_statistics(self):
        """Toplam çalışan sayısını ve maaş ortalamasını hesapla"""

        total_salary = sum(emp["salary"] for emp in self.employees)
        avg_salary = total_salary / len(self.employees) if self.employees else 0
        print(f"Total employees: {len(self.employees)}")
        print(f"Average salary: {avg_salary:.2f} TRY")

company = Company()
emp1 = Employee(1, "Alper", 28, "alper@alper.com", 48000)
mgr1 = Manager(2, "Can", 40, "can@can.com", 85000, "IT")
dev1 = Developer(3, "Ali", 34, "ali@ali.com", 55000, "Python")

# Çalışanları ekleme
company.add_employee(emp1)
company.add_employee(mgr1)
company.add_employee(dev1)

# Çalışanları Listeleme

company.list_employees()

# Bir çalışanın maaşını güncelleme

company.update_salary(3, 60000)

# Güncellenmiş liste 

company.list_employees()

# Çalışanları Silme
company.delete_employee()

# Çalışan Arama
company.search_employee()

# Çalışan Listeleme
company.list_by_department("IT") # IT departmanındaki yöneticiler

# Çalışan Sayısı ve Maaş Ortalaması 

company.company_statistics()