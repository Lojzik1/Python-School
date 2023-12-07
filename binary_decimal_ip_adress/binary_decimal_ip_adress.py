def num_to_binary(number):
    if number > 1:
        return num_to_binary(number // 2) + str(number % 2)
    else:
        return str(number % 2)


def bin_to_dec(binary):
    decimal = 0
    x = 0
    while binary > 0:
        decimal += (binary % 10) * (2 ** x)
        binary //= 10
        x += 1
    return decimal


def bin_ip_to_dec_ip(bin_ip):
    oktety = str(bin_ip).split(".")
    dec_ip = []
    for oktet in oktety:
        dec_ip.append(str(bin_to_dec(int(oktet))))
    return ".".join(dec_ip)


def dec_ip_to_bin_ip(dec_ip):
    binary_ip = ""
    for oktet in str(dec_ip).split("."):
        binary_oktet = ""
        num = int(oktet)
        while num > 0:
            binary_oktet = str(num % 2) + binary_oktet
            num //= 2
        if len(binary_oktet) < 8:
            binary_oktet = "0" * (8 - len(binary_oktet)) + binary_oktet
        binary_ip += binary_oktet + "."
    return binary_ip[:-1]

while True:
    print("1 - Pokud chcete dec IP do bin IP")
    print("2 - Pokud chcete bin IP do dec IP")
    print( )

    výběr = int(input("Napište číslo: "))
    print( )
    if výběr == 1:
        dec_ip = input("Zadejte desítkovou ip: ")
        print()
        print("Výsledek:", dec_ip_to_bin_ip(dec_ip))
        print("----------------------------------------------------------")
        print()
    elif výběr == 2:
        bin_ip = input("Zadejte binární ip: ")
        print("Výsledek:", bin_ip_to_dec_ip(bin_ip))
        print("----------------------------------------------------------")
        print()
    else:
        print("Špatně, zkuste to znovu.")
        print()