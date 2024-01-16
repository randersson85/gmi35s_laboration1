import modules
"""print("Uppgift 1: lista heltal utifrån användarinmatning")
division1 = input("ange värde 1: ")
division2 = input("Ange Värde 2: ")
modules.division(division1, division2)"""

#modules.randomnumber()

# https://www.geeksforgeeks.org/switch-case-in-python-replacement/

menu_selector = 0
while menu_selector != 3:
    print("----------------------------------------------------------------------\n"
          "1. Skapa lista med tal som är jämnt delbara med två av dina val\n"
          "2. Gissa på ett tal mellan 1 - 60\n"
          "3. Avsluta programmet\n"
          "----------------------------------------------------------------------")

    try:
        menu_selector = int(input(""))
        if menu_selector == 1:
            modules.division()
        elif menu_selector == 2:
            modules.randomnumber()
        elif menu_selector == 3:
            print("Avslutar programmet")

    except ValueError:
        print("Ogiltigt menyval, val måste vara heltal mellan 1 - 3")
