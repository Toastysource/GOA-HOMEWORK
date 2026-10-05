foods = ["pizza", "burger", "pizza", "fries"]

foods.append("salad")

foods.insert(1, "cola")

foods.remove("fries")

pizza_count = foods.count("pizza")

burger_index = foods.index("burger")

fruits = ["apple", "banana", "orange", "apple", "kiwi"]

fruits.remove("orange")

fruits.insert(1, "grape")

fruits.append("melon")

apple_count = fruits.count("apple")

banana_index = fruits.index("banana")

items = ["pizza", "burger", "pizza", "pasta", "burger"]

items.append("salad")

items.insert(0, "pasta")

items.remove("burger")

pizza_count = items.count("pizza")

salad_index = items.index("salad")

games = ["Minecraft", "FIFA", "GTA", "Minecraft", "Fortnite"]

games.append("Roblox")

games.insert(2, "Valorant")

games.pop(3)

games.remove("Fortnite")

minecraft_count = games.count("Minecraft")

roblox_index = games.index("Roblox")

# .append
# ამატებს მითითებულ ელემენტს სიის ბოლოში

# .insert
# ამატებს ელემენტს მითითებულ ინდექსზე 

# .remove
# ამოშლის მითითებული ელემენტს სიიდან

# .pop(index)
# აგდებს ელემენტს სიდან

# .count(element)
# ითვლის 

# .index(element)
# იტანს რომელ იდნექსეა მითითებული სიტყვა თუ ასო