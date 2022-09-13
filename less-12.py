# задача №1
li = ["hello", 42, False, 5.79, ("yes", 542), {"Mama": 8654329}]
for el in li:
     print(f"{el}: {type(el)}")

# задача №2
li = input("Введите данные через пробел: ").split()
for s in range(1, len(li), 2):
     li[s - 1], li[s] = li[s], li[s - 1]
     print(li)

# задача №3
month = int(input("введите порядковый номер месяца: "))
season_di = {"Зима": [12, 1, 2], "Весна": [3, 4, 5], "Лето": [6, 7, 8], "Осень": [9, 10, 11]}
season_li = ["Зима", "Весна", "Лето", "Осень"]
for el in season_di:
     if month in season_di[el] and 0 < month < 13:
         print(f"{month} - это {el}")

# задача №4
x = input("введите данные через пробел: ").split()
for li, word in enumerate(x, 1):
    print(li, word[:10])

# задача №5
li = [7, 5, 3, 3, 2]
numb = int(input("введите число: "))
i = 0
for el in li:
    if numb <= el:
        i += 1
li.insert(i, numb)
print(li)



