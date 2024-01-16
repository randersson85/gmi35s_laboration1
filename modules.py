import random
import statistics
# funktion för att skriva ut tal som är jämnt delbara med de två värden som anges av användaren.
def division():
        # https://stackoverflow.com/questions/3289601/null-object-in-python
        # Tar strängvärdet från input och konverterar detta till int istället för string.
        # Skapar list som innehåller samtliga nummer.
    division1 = 0
    division2 = 0
    list_of_numbers = []
    while division1 is 0:
        try:
            division1 = int(input("Ange det första talet: "))
            if division1 <= 0:
                print("Talet kan måste vara mer än 0")
        except ValueError:
            print("Det går endast att ange heltal, vänligen försök igen")
    while division2 is 0:
        try:
            division2 = int(input("Ange det andra talet: "))
            if division1 <= 0:
                print("Talet kan måste vara mer än 0")
        except ValueError:
            print("Det går endast att ange heltal, vänligen försök igen")

            # Skapar en forloop som loopar igenom samtliga heltal från 1 till 1600.
    for x in range(1, 1601):
    # Använder modulo för att hitta tal som inte lämnar någon heltalsrest.
        if x % division1 == 0:
        # Lägger till jämnt delbara tal i list_of_numbers med append.
            list_of_numbers.append(x)
        elif x % division2 == 0:
            list_of_numbers.append(x)
    print(list_of_numbers)
    # https://www.geeksforgeeks.org/find-median-of-list-in-python/
    mean = "{:.2f}".format(statistics.mean(list_of_numbers))
    print ("Medelvärdet på listan är " + mean)
# https://www.w3schools.com/python/gloss_python_for_range.asp
# https://stackoverflow.com/questions/64030305/is-there-a-way-to-accept-only-the-integer-values-after-dividing-a-list





#Funktion för att låta användaren gissa på ett tal mellan 1 - 60.


def randomnumber():
    # Tilldelar variabeln random_number ett slumpat tal mellan 1 - 60
    # https://www.w3schools.com/python/ref_random_randint.asp
    random_number = random.randint(1, 60)
    guess = 0
    while guess != random_number:
        # https://stackoverflow.com/questions/8075877/converting-string-to-int-using-try-except-in-python
        try:
            guess = int(input("Gissa på ett tal mellan 1 - 60: "))
            if guess > 60 or guess < 0 or guess == 0:
                print("Ogiltig gissning, talet är mellan 1 - 60")

            elif guess > random_number:
                print("Talet är lägre än din gissning")

            elif guess < random_number:
                print("Talet är högre än din gissning")

            elif guess == random_number:
                print("Rätt gissat")

        except ValueError:
            print("Det går endast att ange heltal, vänligen försök igen")


