age = int(input(" ჩაწერე შენი ასაკი: "))
if age >= 18:
    print("წვდომა დაშვებულია")
else:
    print("წვდომა უარყოფილია")

    score = 65
attendance = 80
print(score > 50 and attendance > 70)

user_age = 10
print(user_age < 12 or user_age > 65)

x = 14
print(x > 0 and x % 2 == 0)

correct_user = "admin"
correct_pass = "1234"

user_input1 = input("ჩაწერე სახელი: ")

user_input2 = input("ჩაწერე სახელი: ")

if user_input1 == correct_user and user_input2 == correct_pass:
    print("შესვა დაშვებულია")