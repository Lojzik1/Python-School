import math

def vypocet_obvodu_kruhu(polomer):
    return 2 * math.pi * polomer

def vypocet_obsahu_kruhu(polomer):
    return math.pi * polomer ** 2

def vypocet_obvodu_trojuhelniku(strana_a, strana_b, strana_c):
    return strana_a + strana_b + strana_c

def vypocet_obsahu_trojuhelniku(zakladna, vyska):
    return (zakladna * vyska) / 2

def vypocet_obvodu_obdelnika(strana_a, strana_b):
    return 2 * (strana_a + strana_b)

def vypocet_obsahu_obdelnika(strana_a, strana_b):
    return strana_a * strana_b

def vypocet_obvodu_ctverce(strana):
    return 4 * strana

def vypocet_obsahu_ctverce(strana):
        return strana ** 2

def vypocet_objemu_krychle(a):
    return a ** 3

def vypocet_objemu_kvadru(a, b, c):
    return a * b * c

def vypocet_objemu_kuzelu(r, v):
    return (1/3) * math.pi * r ** 2 * v

def vypocet_objemu_jehlanu(a, v):
    return (1/3) * a ** 2 * v

def vypocet_kvadraticke_rovnice(a, b, c):
    D = b ** 2 - 4 * a * c
    if D < 0:
        return
    elif D == 0:
        return (-b) / (2 * a)
    else:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        return x1, x2

print("1 - Obvod kruhu")
print("2 - Obsah kruhu")
print("3 - Obvod trojúhelníku")
print("4 - Obsah trojúhelníku")
print("5 - Obvod obdélníku")
print("6 - Obsah obdélníku")
print("7 - Obvod čtverce")
print("8 - Obsah čtverce")
print("9 - Objem krychle")
print("10 - Objem kvádru")
print("11 - Objem kuželu")
print("12 - Objem jehlanu")
print("13 - Výpočet kvadratické rovnice")

choose = int(input("Vyberte co chcete provést:"))

if choose == 1:
    polomer = int(input("Zadejte poloměr kruhu v cm: "))
    print("Obvod kruhu je: ", vypocet_obvodu_kruhu(polomer))
elif choose == 2:
    polomer = float(input("Zadejte poloměr kruhu v cm: "))
    print("Obsah kruhu je: ", vypocet_obsahu_kruhu(polomer))
elif choose == 3:
    strana_a = float(input("Zadejte délku strany a v cm: "))
    strana_b = float(input("Zadejte délku strany b v cm: "))
    strana_c = float(input("Zadejte délku strany c v cm: "))
    print("Obvod trojúhelníku je: ", vypocet_obvodu_trojuhelniku(strana_a, strana_b, strana_c), "cm")
elif choose == 4:
    zakladna = float(input("Zadejte délku základny trojúhelníku v cm: "))
    vyska = float(input("Zadejte délku výšky trojúhelníku v cm: "))
    print("Obsah trojúhelníku je: ", vypocet_obsahu_trojuhelniku(zakladna, vyska), "cm2")
elif choose == 5:
    strana_a = float(input("Zadejte délku strany a obdélníku v cm: "))
    strana_b = float(input("Zadejte délku strany b obdélníku v cm: "))
    print("Obvod obdélníku je: ", vypocet_obvodu_obdelnika(strana_a, strana_b), "cm")
elif choose == 6:
    strana_a = float(input("Zadejte délku strany a obdélníku: "))
    strana_b = float(input("Zadejte délku strany b obdélníku: "))
    print("Obsah obdélníku je: ", vypocet_obsahu_obdelnika(strana_a, strana_b), "cm2")
elif choose == 7:
    strana = float(input("Zadejte délku strany v cm:"))
    print("Obvod čtverce je:", vypocet_obvodu_ctverce(strana), "cm")
elif choose == 8:
    strana = float(input("Zadejte délku strany v cm:"), "cm2")
    print("Obsah čtverce je:", vypocet_obsahu_ctverce(strana))
elif choose == 9:
    a = float(input("Zadejte délku a v cm:"))
    print("Objem krychle je:", vypocet_objemu_krychle(a), "cm3")
elif choose == 10:
    a = float(input("Zadejte délku strany a obdélníku/čtverce v cm: "))
    b = float(input("Zadejte délku strany a obdélníku/čtverce v cm: "))
    c = float(input("Zadejte délku strany a obdélníku/čtverce v cm: "))
    print("Objem kvádru je:", vypocet_objemu_kvadru(a, b, c), "cm3")
elif choose == 11:
    r = float(input("Zadejte délku strany v cm:"))
    v = float(input("Zadejte délku strany v cm:"))
    print("Objem kuželu je:", vypocet_objemu_kuzelu(r, v), "cm3")
elif choose == 12:
    a = float(input("Zadejte délku strany v cm:"))
    v = float(input("Zadejte délku strany v cm:"))
    print("Objem jehlanu je:", vypocet_objemu_jehlanu(a, v), "cm3")
elif choose == 13:
    a = float(input("Zadejte délku strany v cm:"))
    b = float(input("Zadejte délku strany v cm:"))
    c = float(input("Zadejte délku strany v cm:"))
    print("Výpočet je:", vypocet_kvadraticke_rovnice(a, b, c), "cm")
