#if-else statement  ჩვენ ვხმარობთ მშინ რიდესაც გვინდა რომ თუ ერთი რამე კმაყოფილდება ამის შედეგად რამე სხვა მოხდეს 
num1 = float(input("შეიყვანეთ პირველი რიცხვი: "))
num2 = float(input("შეიყვანეთ მეორე რიცხვი: "))

if num1 > num2:
    print("პირველი მეტია")
else:
    print("მეორე მეტია")

num = float(input("შეიყვანეთ რიცხვი: "))

if num > 100:
    print("100-ზე მეტია")
elif num == 100:
    print("100-ის ტოლია")
else:
    print("100-ზე ნაკლებია")

name = input("შეიყვანეთ სახელი: ")

if name == "Nika":
    print("გამარჯობა, ნიკა!")
else:
    print("უცნობი მომხმარებელი")

temp = float(input("შეიყვანეთ ტემპერატურა: "))

if temp < 0:
    print("იყინება")
else:
    print("არ იყინება")

price = float(input("შეიყვანეთ პროდუქტის ფასი: "))

if price >= 100:
    print("გეკუთვნის ფასდაკლება")
else:
    print("ფასდაკლება არ გეკუთვნის")

number = float(input("შეიყვანეთ რიცხვი: "))

if number == 0:
    print("ნულია")
else:
    print("ნული არ არის")

balance = float(input("შეიყვანეთ ანგარიშზე არსებული თანხა: "))

if balance >= 50:
    print("საკმარისი ბალანსია")
else:
    print("ბალანსი არასაკმარისია")