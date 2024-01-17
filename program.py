import modules

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
            print (modules.division())
        elif menu_selector == 2:
            modules.randomnumber()
        elif menu_selector == 3:
            print("Avslutar programmet")
        elif menu_selector >= 4 or menu_selector <= 0:
            print("Ogiltigt menyval, val måste vara heltal mellan 1 - 3")
    except ValueError:
        print("Ogiltigt menyval, val måste vara heltal mellan 1 - 3")
