# funktion för att skriva ut tal som är jämnt delbara med de två värden som anges av användaren.
def task1(division1, division2):
    #Tar strängvärdet från input och konverterar detta till int istället för string.
    division1 = int(division1)
    division2 = int(division2)
    #Skapar list som innehåller samtliga nummer.
    list_of_numbers = []
    #Skapar en forloop som loopar igenom samtliga heltal från 1 till 1600.
    for x in range(1, 1601):
        #Använder modulo för att hitta tal som inte lämnar någon heltalsrest.
        if x % division1 == 0:
            #Lägger till jämnt delbara tal i list_of_numbers med append.
            list_of_numbers.append(x)
        elif x % division2 == 0:
            list_of_numbers.append(x)
    print(list_of_numbers)
# https://www.w3schools.com/python/gloss_python_for_range.asp
# https://stackoverflow.com/questions/64030305/is-there-a-way-to-accept-only-the-integer-values-after-dividing-a-list

#Funktion för att låta användaren gissa på ett tal mellan 1 - 60.

#   def randomnumber():
#   print("Kvar att implementera")
