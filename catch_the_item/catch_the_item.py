import random

# Určení velikosti hracího pole
x = 5
y = 5

# Určení pozice hráče
position_y = 0
position_x = 0

# Určení pozice předmětu a vzhledu předmětu
predmet = "@"

# Skóre hráče
score = 0

# Funkce pro naplnění hracího pole
def fill_field(x, y, position_x, position_y):
    field = []
    while y > 0:
        row = []
        columns = x
        while columns > 0:
            row.append("o")
            columns -= 1
        field.append(row)
        y -= 1
        if y == 0:
            field[position_y][position_x] = "X"
    return field

# Funkce pro výpis hracího pole
def print_field(field, rows):
    n = 0
    while n < rows:
        print("".join(field[n]))
        n += 1

# Generování náhodné pozice předmětu
position_k = random.randint(0, x * y - 1)
row_index = position_k // x
col_index = position_k % x

# Naplnění hracího pole
field = fill_field(x, y, position_x, position_y)

# Umístění předmětu na vygenerovanou pozici
field[row_index][col_index] = predmet

# Výpis hracího pole
print_field(field, y)

# Herní smyčka
score_message = ""
while True:
    user_input = input("Zadej akci: ")
    if user_input == "q":
        break
    elif user_input == "d":
        if position_x + 1 < x:
            field[position_y][position_x] = "o"
            position_x = position_x + 1
    elif user_input == "a":
        if position_x - 1 >= 0:
            field[position_y][position_x] = "o"
            position_x = position_x - 1
    elif user_input == "w":
        if position_y - 1 >= 0:
            field[position_y][position_x] = "o"
            position_y = position_y - 1
    elif user_input == "s":
        if position_y + 1 < y:
            field[position_y][position_x] = "o"
            position_y = position_y + 1
    else:
        print("Zadej správný vstup")
        continue

    if field[position_y][position_x] == predmet:
        print("Gratuluji! Našel jsi předmět!")
        score += 1  # Zvýšení skóre o 1
        score_message = "Vaše skóre je: " + str(score)

        position_k = random.randint(0, x * y - 1)  # Generování nové pozice předmětu
        row_index = position_k // x
        col_index = position_k % x
        field[row_index][col_index] = predmet

    field[position_y][position_x] = "X"
    print_field(field, y)

    # Výpis aktuálního skóre
    print(score_message)




#----------------------------#
#Druhý postup herní smyčky
#----------------------------#
    # match user_input:
    #     case "q":
    #         break
    #     case "d":
    #         field[position_y][position_x] = "o"
    #         field[position_y][position_x+1] = "X"
    #         position_x = position_x+1
    #     case "a":
    #         field[position_y][position_x] = "o"
    #         field[position_y][position_x-1] = "X"
    #         position_x = position_x-1
    #     case "w":
    #         field[position_y][position_x] = "o"
    #         field[position_y-1][position_x] = "X"
    #         position_y = position_y-1
    #     case "s":
    #         field[position_y][position_x] = "o"
    #         field[position_y+1][position_x] = "X"
    #         position_y = position_y+1
    #     case _:
    #         print("Zadej správný vstup")
    #         continue
    # print_field(field, y)
