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
        # Logik för meny.
        if menu_selector == 1:
            #Skapar variabler som ska skickas till funktionen som argument.
            division1 = 0
            division2 = 0

            # Tar strängvärdet från input och konverterar detta till int istället för string.
            while division1 <= 0:
                try:
                    division1 = int(input("Ange det första talet: "))
                    if division1 <= 0:
                        print("Talet måste vara mer än 0")
                except ValueError:
                    print("Det går endast att ange heltal, vänligen försök igen")

            while division2 <= 0:
                try:
                    division2 = int(input("Ange det andra talet: "))
                    if division2 <= 0:
                        print("Talet kan måste vara mer än 0")
                except ValueError:
                    print("Det går endast att ange heltal, vänligen försök igen")
                print(modules.division(division1, division2))

        elif menu_selector == 2:
            modules.randomnumber()
        elif menu_selector == 3:
            print("Avslutar programmet")
        elif menu_selector >= 4 or menu_selector <= 0:
            print("Ogiltigt menyval, val måste vara heltal mellan 1 - 3")
    except ValueError:
        print("Ogiltigt menyval, val måste vara heltal mellan 1 - 3")
