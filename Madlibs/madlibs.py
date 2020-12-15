# Concatenação de Strings
#youtuber = "LetsCode"

#Três formas para se concaternar uma string
#print("Se inscrevar no canal: " + youtuber)
#print("Se inscreva no canal: {}".format(youtuber))
#print(f"Se inscreva no canal: {youtuber}")

adj = input("Adjetivo: ")
verb1 = input("Verbo1: ")
verb2 = input("Verbo2: ")
famoso = input("Pessoa Famosa: ")

madlib = f"Programar é tão...{adj}! Me faz tão bem pois \
    eu amo {verb1}. Continue focado e continue {verb2} pois nesse caminho, assim você será como {famoso}!"

print(madlib)