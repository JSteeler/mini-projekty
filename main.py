# password = input("Zvolte si uživatelské heslo: ")
#
# contain_num = any(char.isdigit() for char in password)
# contain_upper = any(char.isupper() for char in password)
# contain_special = any(not char.isalnum() for char in password)
#
#
# if len(password) >= 6 and contain_num and contain_upper and contain_special :
#     password_again = input("Zadejte heslo znovu: ")
#     if password_again != password:
#         print("Hesla se neshodují!")
#     else:
#         print("Registrace proběhla úspěšně!")
# else:
#     print("Heslo musí mít aspoň 6 znaků a musí obsahovat aspoň 1 číslo, 1 velké písmeno a 1 speciální znak.")
#
# login = input("Zadejte heslo pro přihlášení: ")
# if login != password:
#     print("Zadané heslo není správné!")
# else:
#     print("Jste přihlášen!")
#
#
from locale import currency

# import random
#
# while True:
#     play = input("Chceš hodit kostkama? Ano/Ne ").lower()
#     if play != "ano":
#         break
#     dice_1 = random.randint(1, 6)
#     dice_2 = random.randint(1, 6)
#     result = dice_1 + dice_2
#     print(f"Hodil jsi {dice_1} a {dice_2}, tvůj celkový součet je {result}.")
#     play_pc = input("Teď bude házet počítač. Chceš pokračovat? Ano/Ne ").lower()
#     if play_pc != "ano":
#         break
#     dice_1_pc = random.randint(1, 6)
#     dice_2_pc = random.randint(1, 6)
#     result_pc = dice_1_pc + dice_2_pc
#     print(f"Počítač hodil {dice_1_pc} a {dice_2_pc}, jeho celkový součet je {result_pc}.")
#     if result > result_pc:
#         print("Vyhrál jsi!")
#     elif result < result_pc:
#         print("Počítač vyhrál!")
#     else:
#         print("Remíza!")
#
# print("Bye Bye!")
#

# import random
#
# nums = ["1","2","3","4","5","6","7","8","9"]
# letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# special_chars = ['!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']
#
# generate = input("Jaké chceš vygenerovat heslo? Weak/Medium/Strong ").lower()
#
# if generate == "weak":
#     number = 2
# elif generate == "medium":
#     number = 3
# elif generate == "strong":
#     number = 4
#
# rand_nums = random.sample(nums, number)
# rand_letters = random.sample(letters, number)
# rand_special = random.sample(special_chars, number)
# password = rand_nums + rand_letters + rand_special
# random.shuffle(password)
#
# print(f"Vaše heslo je '{"".join(password)}'")

# import requests
#
# print("Vítej v aplikaci na převod měn.")
#
# currency_1 = input("Zadej měnu, ze které chceš převést: ").upper()
# currency_2 = input("Zadej měnu, na kterou chceš převést: ").upper()
# amount = int(input(f"Zadej množství {currency_1}: "))
#
# response = requests.get(f"https://api.frankfurter.app/latest?amount={amount}&from={currency_1}&to={currency_2}")
# data = response.json()
#
# print(data)
# result = data["rates"][currency_2]
# print(f"{amount} {currency_1} je {result} {currency_2}")
#
#

