num1 = int(input("ჩაწერე ნებისმიერი რიცხვი: "))
if num1 > 0:
    print("დადებითია")
elif num1 == 0:
    print("ნულია")
else:
    print("უარყოფითია")


age = int(input("რამდენის წლის ხარ: "))
if age > 18:
    print("სრულწლოვანი ხარ")
else:
    print("არასრულწლოვანი ხარ")


point = int(input("ჩაწერე შენი ქულა: "))
if point > 50:
    print("ჩააბარე")
else:
    print("ჩაიჭერი")


password = "python123"

passwor123 = (input("ჩაწერე პაროლი"))

if password == passwor123:
    print("accses granted")
else:
    print("accses denied")