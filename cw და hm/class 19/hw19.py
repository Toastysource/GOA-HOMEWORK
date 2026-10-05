#ინდექსინგი ბოლოდან ნიშნავს ინექსიგის გამოყენებას ბოლოდანა ნუ დადებითი რიცხვების მაგივრად ხმარობ უარყოფითს

numbers = [10, 20, 30, 40, 50, 60, 70, 80]

out1 = numbers[:4]

out2 = numbers[-3:]

out3 = numbers[2:6]

out4 = numbers[::-1]


word = "PYTHONPROGRAMMING"

ans1 = word[:6]

ans2 = word[6:]

ans3 = word[:5]

ans4 = word[-5:]

ans5 = word[::-1]


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

ans1 = letters[-1] 

ans2 = letters[-4:]

ans3 = letters[:-2]

ans4 = letters[-5:-2]

ans5 = letters[::-1]

numbers = [1, 2, 3, 4, 5, 6]


numbers[2:5] = [30, 40]


numbers[:3] = [10, 20, 30]


numbers[6:] = [7, 8]

print(numbers)