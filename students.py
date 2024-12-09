import json, os
from json import JSONEncoder

class Students:
  
  def __init__(self, row_id=None, name=None, grade=None):
    self.row_id = row_id
    self.name = name
    self.grade = grade
  
  # ახალი სტუდენტის დამატება
  def add_student(self):
    new_student = {"row_id": self.row_id, "name": self.name, "grade": self.grade}
    data.append(new_student)
    json_write(data)
    

  # სტუდენტების სრული სიის გამოტანა
  def full_list(self):
    print("-"*40)
    print(f"{'id':<10}{'Name':<10}{'Grade'}")
    print("="*40)
    for student in data:
      print(f"{student['row_id']:<10}{student['name']:<10}{student['grade']}")
      print("-"*40)
    
  # სტუდენტის ძებნა
  def find(self, row_id):
    for student in data:
      if row_id == student['row_id']:
        print("\n")
        print("-"*40)
        print(f"{'id':<10}{'Name':<10}{'Grade'}")
        print("="*40)
        print(f"{student['row_id']:<10}{student['name']:<10}{student['grade']}")

  # შეფასების განახლება
  def update_grade(self, row_id, new_grade):
    for student in data:
      if row_id == student['row_id']:
        
        student['grade'] = new_grade

        json_write(data)
    
# ენკოდერი 
class encoder(JSONEncoder):
  def default(self, o):
    return o.__dict__
  
# ფაილის ჩაწერის ფუნქცია   
def json_write(data):
  with open("students.json", mode='w', encoding='utf-8') as file:
    json.dump(data, file, cls=encoder, indent=2)

# ფაილის წაკითხვის ფუნქცია
def read_json():
  with open('students.json', mode='r', encoding='utf-8') as file:
    return json.load(file)
    #===============================


students = [
  Students(1, 'Nika', 'A' ),
  Students(2, 'Nika', 'B' ),
  Students(3, 'Shalva', 'B' ),
  Students(4, 'Nika', 'B' ),
  Students(5, 'Dato', 'A' ),
  Students(6, 'Nika', 'C' ),
  Students(7, 'Natia', 'B' ),
  Students(8, 'Lika', 'C' ),
]


def check():
  if os.path.isfile('students.json'):
    print(f"Error: The file '{"data.json"}' already exists. Aborting write operation.")
    return 
  
  json_write(students)

check()


data = read_json()



action_list = ['1', '2', '3', '4', '5']

while True:
  print("\n1) full students list")
  print("\n2) search student with id")
  print("\n3) update grade")
  print("\n4) add new student")
  print("\n5) exit\n")

  menu = input("select operation from menu: ")

  if menu in action_list:
    if menu == '1':
      student1 = Students()
      student1.full_list()

    elif menu =='2':
      input_id = int(input("enter id to search"))
      student2 = Students()
      student2.find(input_id)

    elif menu == '3':
      input_id = int(input("select id"))
      input_grade = input("input new grade to update: ").upper()
      student3 = Students()
      student3.update_grade(input_id, input_grade)

    elif menu == '4':
      new_id = int(input("Input ID: "))

    
      while True:
          exists = False 
          for record in data:
              if new_id == record['row_id']:
                  exists = True
                  print("ID already exists, enter another ID number")
                  new_id = int(input("Input ID: "))
                  break  
          if not exists:  
              break

      print(f"ID {new_id} is unique and can be used.")
        
      new_student_name = input("input student name:").upper()
      while True:
        new_student_grade = input("input grade").upper()
        if len(new_student_grade) > 1:
          print("grade must be one symbol: A, B, C, D, or E")
        else:
          break
        

      student4 = Students(new_id, new_student_name, new_student_grade)
      student4.add_student()
    elif menu == '5':
      print("exit")
      break
    
    
    else:
      print("wrong menu symbol")

