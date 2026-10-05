User_Date = int(input("ჩაწერე რიცხვი: "))

if User_Date == 1:
    print("ორშაბათია")
elif User_Date == 2:
    print("სამშაბათია")
elif User_Date == 3:
    print("ოთხშაბათია")
elif User_Date == 4:
    print("ხუთშაბათია")
elif User_Date == 5:
    print("პარასკევია")
elif User_Date == 6:
    print("შაბათია")
elif User_Date == 7:
    print("კვირა")
else:
    print("რავი მაგის შენ დაითვალე")

User_Num = int(input("ჩაწერე რიცხვი: "))

if User_Num > 50:
    print(User_Num * 5)
else:
    print(User_Num ** 2)

password = "Goa123"
User_Input = str(input("შეიყვანე პაროლი"))

if password == User_Input:
    print("Password is Correct")
else:
    print("Password is Incorrect")