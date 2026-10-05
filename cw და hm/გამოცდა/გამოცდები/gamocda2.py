#მომავალი ასაკი:

age1 = int(input("რამდენი წლის ხარ?: "))
age2 = age1 + 5
print(f"ხუთ წელიწადში შენ იქნები {age2}")

#ორი რიცხვის ჯამი:

num1 = int(input("ჩაწერე ნებისმიერი რიციხვი: "))
num2 = int(input("ჩაწერე ნებისმიერი რიციხვი: "))


print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
print(num1 ** num2)
print(num1 // num2)
print(num1 % num2)

#სტრინგების შეკრება

#print("50" + "20") შედეგი იქნება 5020 რადან სტრინგები არ იკრიბება როგორც ინტეგერები ანუ რიცხვები და მას კოდი როგორც ორ სიტყვად ისე აღიქვამს ამიტომად უბრალოდ ერთმანეთს აერთებს

#სრულწლოვანების შემოწმება:


age = 16

if age < 18:
    print("შენ ხარ არასრუწლოვანი")
else:
    print("შენ ხარ სრულწლოვანი")

# გამსვლელი ქულა

score = 65
attendance = 80

if score > 50 and attendance > 70:
    print("მეტია")

#ასაკის ფასდაკლება
user_age = 10

if user_age < 12 or user_age > 65:
    print("ture")
else:
    print("false")

#ავტორიზაციის სიმულაცია

correct_user = "admin"
correct_pass = "1234" 
entered_user = "admin" 
entered_pass = "1234"

if correct_user == entered_user and correct_pass == entered_pass :
    print("accses granted")
else:
    print("accses denied")

#ტიპების კონვერტაცია:
 # ტიპების შეცვლა შეგვიძლია   str(), int(), float() ეს მოქმედებები გვაძლევს იმის საშვალებას რომ str გადქავიყვანოთ int და int გადავიყვანოთ float ში რადგან მაგალითად თუ ჩვენ 
 #მომხმარებელს მოვთხოვთ ამთ ასაკს და ისინი მათ ამ ასაკს int სახით ანუ "15" შეიყვანენ ჩვენ მათზე მათემატიკურ მოქმედებას ვერ განვახორციელებთ რადგან int float და int არ ემატება
# მაგალითად:

age3 = int(input("ჩაწერე შენი წლოვანება"))
age4 = age3 + 1

print (f"შენ ერთ წელიწადში იქნები {age4} ")

#7 და 10 გადვახტი

print("10" == 10)

x = 14

if x > 0 and x % 2 == 0:
    print("true")
else:
    print("false")