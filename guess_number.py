import random
from random import randint

random_number = randint(1, 100)
i = 0
while i <= 10:
  if i == 10:
    print("სამწუხაროდ თქვენ ვერ შეძელით რიცხვის გამოცნობა 10 ცდაში")
  else:
    try:
      user_number = int(input("შეიყვანეთ რიცხვი: "))
   
      
      if user_number == random_number:
        print(f"\nგილოცავთ, თქვენ გამოიცანით ჩაფიქრებული რიცხვი {random_number}")
        break
      elif user_number > random_number:
        print("\nთქვენ შეიყვანეთ ზედმეტად დიდი რიცხვი, სცადეთ შეიყვანოთ უფრო მცირე რიცხვი\n")
      elif user_number < random_number:
        print("\nთქვენ შეიყვანეთ ზედმეტად მცირე რიცხვი, სცადეთ შეიყვანოთ უფრო დიდი რიცხვი\n")
    except ValueError:
       print("უნდა შეიყვანოთ მხოლოდ მთელი რიცხვები")
  i += 1

print("\nთამაში დასრულებულია....")

    